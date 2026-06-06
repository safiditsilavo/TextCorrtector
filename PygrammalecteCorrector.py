import re
import json
import sys
from pygrammalecte import grammalecte_text
from spellchecker import SpellChecker
from Patterns import HOMOPHONE_PATTERNS

spell = SpellChecker(language='fr')

def build_context(text, word, start):
    """Build a context dictionary for pattern matching."""
    end = start + len(word)
    context_before = text[max(0, start-100):start].lower().strip()
    context_after = text[end:min(len(text), end+100)].lower().strip()
    
    words_before = context_before.split()
    words_after = context_after.split()
    
    next_word = re.sub(r'[,.!?;:\'"()]', '', words_after[0]) if words_after else ""
    next_next_word = re.sub(r'[,.!?;:\'"()]', '', words_after[1]) if len(words_after) > 1 else ""
    
    return {
        'word_low': word.lower(),
        'context_before': context_before,
        'context_after': context_after,
        'words_before': words_before,
        'words_after': words_after,
        'next_word': next_word,
        'next_next_word': next_next_word,
        'prev_word': words_before[-1] if words_before else "",
    }

def apply_pattern_rules(ctx):
    """Apply pattern-based rules to get suggestions."""
    suggestions = []
    word = ctx['word_low']
    
    if word not in HOMOPHONE_PATTERNS:
        return suggestions
    
    patterns = HOMOPHONE_PATTERNS[word]
    
    for rule in patterns.get('rules', []):
        try:
            if all(condition(ctx) for condition in rule['conditions']):
                suggestions.append(rule['suggestion'])
        except (IndexError, AttributeError):
            continue
    
    return suggestions

def get_custom_suggestions(word, text, start):
    """Enhanced context-aware homophone detection using pattern matching."""
    ctx = build_context(text, word, start)
    return apply_pattern_rules(ctx)

def full_proofreader(text):
    corrections = []
    errors = list(grammalecte_text(text))
    
    if not errors:
        return []
    
    for error in errors:
        start = error.start
        end = error.end
        wrong_word = text[start:end]
        message = getattr(error, 'message', "Erreur")
        
        # Grammalecte suggestions
        suggestions = list(getattr(error, 'suggestions', []))
        
        # Custom logic
        custom_hints = get_custom_suggestions(wrong_word, text, start)
        
        # PySpellChecker for unknown words
        if not suggestions and not custom_hints and "Mot inconnu" in message:
            clean = wrong_word.strip(",.!?;:")
            candidates = spell.candidates(clean)
            suggestions = list(candidates) if candidates else []
            suggestions = suggestions[:10]
        
        # Combine and deduplicate (prioritize custom hints)
        final_suggestions = list(dict.fromkeys(custom_hints + suggestions))[:10]
        
        # Output
        if wrong_word not in [item['word'] for item in corrections]:
            corrections.append({
                'word': wrong_word,
                'start': start,
                'end': end,
                'message': message,
                'suggestions': final_suggestions
            })

    return corrections

def main():
    # text = "pouvez-vous me dit ce que s'est?"
    # corrections = full_proofreader(text)
    # print(corrections)

    if len(sys.argv) > 1:
        text = sys.argv[1]
        corrections = full_proofreader(text)
        result = {
            "status": "success" if corrections else "error",
            "errors": corrections if corrections else [],
            "message": "No errors found" if not corrections else f"Found {len(corrections)} error(s)",
            "data": corrections
        }
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        error_result = {
            "status": "error",
            "message": "Usage: python3 PygrammalecteCorrector.py 'text to check'"
        }
        print(json.dumps(error_result, ensure_ascii=False, indent=2))
        sys.exit(1)

if __name__ == "__main__":
    main()