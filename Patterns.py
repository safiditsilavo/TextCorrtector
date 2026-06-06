HOMOPHONE_PATTERNS = {
    'ces': {
        'alternatives': ["c'est", "s'est"],
        'rules': [
            {
                'name': 'reflexive_past_participle',
                'conditions': [
                    lambda ctx: any(s in ctx['words_before'][-3:] for s in ['il', 'elle', 'on', "'il", "'elle"]),
                    lambda ctx: ctx['next_word'].endswith(('é', 'i', 'u', 'is', 'it', 'us', 'ut'))
                ],
                'suggestion': "s'est"
            },
            {
                'name': 'sentence_start',
                'conditions': [
                    lambda ctx: not ctx['context_before'].strip() or ctx['context_before'].endswith(('.', '!', '?', ';')),
                    lambda ctx: ctx['next_word'] and not ctx['next_word'].endswith('s')
                ],
                'suggestion': "c'est"
            }
        ]
    },
    'sait': {
        'alternatives': ["s'est", "sais"],
        'rules': [
            {
                'name': 'reflexive_past',
                'conditions': [
                    lambda ctx: any(s in ctx['words_before'][-2:] for s in ['il', 'elle', 'on']),
                    lambda ctx: ctx['next_word'].endswith(('é', 'i', 'u'))
                ],
                'suggestion': "s'est"
            },
            {
                'name': 'verb_first_person',
                'conditions': [
                    lambda ctx: any(s in ctx['words_before'][-2:] for s in ['je', 'tu']),
                ],
                'suggestion': "sais"
            }
        ]
    },
    'ses': {
        'alternatives': ["c'est", "s'est", "sait"],
        'rules': [
            {
                'name': 'reflexive_verb',
                'conditions': [
                    lambda ctx: any(s in ctx['words_before'][-3:] for s in ['il', 'elle', 'on']),
                    lambda ctx: ctx['next_word'].endswith(('é', 'i', 'u'))
                ],
                'suggestion': "s'est"
            },
            {
                'name': 'sentence_start',
                'conditions': [
                    lambda ctx: not ctx['context_before'].strip() or ctx['context_before'].endswith(('.', '!', '?')),
                    lambda ctx: ctx['next_word'] and not ctx['next_word'].endswith('s')
                ],
                'suggestion': "c'est"
            }
        ]
    },
    'son': {
        'alternatives': ['sont', 'sons'],
        'rules': [
            {
                'name': 'plural_verb',
                'conditions': [
                    lambda ctx: ctx['next_word'] in ['pas', 'plus', 'jamais', 'rien', 'guère'],
                ],
                'suggestion': 'sont'
            },
            {
                'name': 'plural_subject',
                'conditions': [
                    lambda ctx: any(d in ctx['words_before'][-2:] for d in ['ils', 'elles', 'les']),
                ],
                'suggestion': 'sont'
            }
        ]
    },
    'sont': {
        'alternatives': ['son', 'sons'],
        'rules': [
            {
                'name': 'possessive',
                'conditions': [
                    lambda ctx: any(d in ctx['words_before'][-3:] for d in ['mon', 'ton', 'son', 'ma', 'ta', 'sa', 'notre', 'votre', 'leur']),
                ],
                'suggestion': 'son'
            }
        ]
    },
    'a': {
        'alternatives': ['à', 'as', 'ah'],
        'rules': [
            {
                'name': 'preposition_before_article',
                'conditions': [
                    lambda ctx: ctx['next_word'] in ['un', 'une', 'le', 'la', 'des', 'mon', 'ma', 'mes', 'ton', 'ta', 'tes'],
                ],
                'suggestion': 'à'
            },
            {
                'name': 'verb_second_person',
                'conditions': [
                    lambda ctx: any(s in ctx['words_before'][-2:] for s in ['tu', 'vous']),
                ],
                'suggestion': 'as'
            }
        ]
    },
    'ou': {
        'alternatives': ['où', 'ouf'],
        'rules': [
            {
                'name': 'interrogative_adverb',
                'conditions': [
                    lambda ctx: '?' in ctx['context_after'] or any(q in ctx['context_before'] for q in ['quel', 'quelle', 'quoi']),
                ],
                'suggestion': 'où'
            }
        ]
    },
    'ce': {
        'alternatives': ["c'est", 'se'],
        'rules': [
            {
                'name': 'demonstrative_before_verb',
                'conditions': [
                    lambda ctx: ctx['next_word'] in ['est', 'sont', 'sera', 'serait', 'fut'],
                ],
                'suggestion': "c'est"
            },
            {
                'name': 'reflexive_verb',
                'conditions': [
                    lambda ctx: ctx['next_word'].endswith(('ant', 'er')) and any(v in ctx['words_before'][-2:] for v in ['je', 'tu', 'nous', 'vous']),
                ],
                'suggestion': 'se'
            }
        ]
    },
    'se': {
        'alternatives': ['ce', 'sé'],
        'rules': [
            {
                'name': 'reflexive_pronoun',
                'conditions': [
                    lambda ctx: ctx['next_word'].endswith(('ant', 'er', 'e')) and any(v in ctx['words_before'][-3:] for v in ['il', 'elle', 'elles', 'ils']),
                ],
                'suggestion': 'ce'
            }
        ]
    },
    'et': {
        'alternatives': ['est', 'è', 'ès'],
        'rules': [
            {
                'name': 'verb_conjugation',
                'conditions': [
                    lambda ctx: any(s in ctx['words_before'][-3:] for s in ['il', 'elle', 'on']) and not ctx['next_word'].endswith(('ent', 'oir', 'ant')),
                ],
                'suggestion': 'est'
            }
        ]
    },
    'la': {
        'alternatives': ["l'a", 'là'],
        'rules': [
            {
                'name': 'past_tense_object',
                'conditions': [
                    lambda ctx: any(v in ctx['context_before'] for v in ['a ', 'as ', 'ai ', 'avez ', 'ont ', 'avoir']),
                ],
                'suggestion': "l'a"
            },
            {
                'name': 'demonstrative_adverb',
                'conditions': [
                    lambda ctx: ctx['next_word'] in ['bas', 'haut', 'bas', 'dedans', 'dehors'] or '...' in ctx['context_after'],
                ],
                'suggestion': 'là'
            }
        ]
    },
    'ai': {
        'alternatives': ['ais', 'est'],
        'rules': [
            {
                'name': 'verb_first_person_plural',
                'conditions': [
                    lambda ctx: any(s in ctx['words_before'][-2:] for s in ['je', 'nous']),
                    lambda ctx: ctx['next_word'].endswith(('é', 'i', 'u', 'is', 'it'))
                ],
                'suggestion': 'ais'
            }
        ]
    },
    'au': {
        'alternatives': ['aux', 'eau'],
        'rules': [
            {
                'name': 'plural_preposition',
                'conditions': [
                    lambda ctx: ctx['next_word'].endswith('s') or ctx['next_next_word'].endswith('s'),
                ],
                'suggestion': 'aux'
            }
        ]
    },
    'ç': {
        'alternatives': ['c', 'ss'],
        'rules': [
            {
                'name': 'cedilla_before_vowel',
                'conditions': [
                    lambda ctx: ctx['next_word'][0] if ctx['next_word'] else '' in 'aeiouy',
                ],
                'suggestion': 'c'
            }
        ]
    }
}