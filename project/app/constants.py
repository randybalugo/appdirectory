'''
Constant values.
'''

CURRENCY_CODES = (('aus', 'Australia'),
                    ('aut', 'Austria'),
                    ('bel', 'Belgium'),
                    ('can', 'Canada'),
                    ('dnk', 'Denmark'),
                    ('fin', 'Finland'),
                    ('fra', 'France'),
                    ('deu', 'Germany'),
                    ('grc', 'Greece'),
                    ('irl', 'Ireland'),
                    ('ita', 'Italy'),
                    ('jpn', 'Japan'),
                    ('lux', 'Luxembourg'),
                    ('mex', 'Mexico'),
                    ('nld', 'Netherlands'),
                    ('nzl', 'New Zealand'),
                    ('nor', 'Norway'),
                    ('prt', 'Portugal'),
                    ('esp', 'Spain'),
                    ('swe', 'Sweden'),
                    ('che', 'Switzerland'),
                    ('gbr', 'United Kingdom'),
                    ('usa', 'United States'),)

#Note this has the categories hardcoded to optimize the db querys. Could break if genre ids change.
CATEGORIES = {  'Lifestyle' : [6012L, 12008L],
                'Finance' : [6015L, 12005L],
                'Business' : [6000L, 12001L],
                'Entertainment' : [6016L, 12004L],
                'Navigation' : [6010L],
                'Medical' : [6020L, 12010L],
                'Utilities' : [6002L, 12019L],
                'Music' : [6011L, 7011L, 12011L, 12211L],
                'Sports' : [7016L, 6004L, 12017L, 12216L],
                'Book' : [6018L],
                'Games' : [6014L, 12006L],
                'News' : [6009L, 12012L],
                'Productivity' : [6007L, 12014L],
                'Travel' : [6003L, 12018L],
                'Education' : [6017L, 12003L],
                'Social Networking' : [6005L, 12016L],
                'Reference' : [6006L, 12015L],
                'Photography' : [12013L],
                'Healthcare & Fitness' : [12007L],}

LANGUAGE_CODES = {'ab' : 'Abkhazian',
'aa' : 'Afar',
'af' : 'Afrikaans',
'sq' : 'Albanian',
'am' : 'Amharic',
'ar' : 'Arabic',
'an' : 'Aragonese',
'hy' : 'Armenian',
'as' : 'Assamese',
'ay' : 'Aymara',
'az' : 'Azerbaijani',
'ba' : 'Bashkir',
'eu' : 'Basque',
'bn' : 'Bengali (Bangla)',
'dz' : 'Bhutani',
'bh' : 'Bihari',
'bi' : 'Bislama',
'br' : 'Breton',
'bg' : 'Bulgarian',
'my' : 'Burmese',
'be' : 'Byelorussian (Belarusian)',
'km' : 'Cambodian',
'ca' : 'Catalan',
'zh' : 'Chinese (Simplified)',
'zh' : 'Chinese (Traditional)',
'co' : 'Corsican',
'hr' : 'Croatian',
'cs' : 'Czech',
'da' : 'Danish',
'nl' : 'Dutch',
'en' : 'English',
'eo' : 'Esperanto',
'et' : 'Estonian',
'fo' : 'Faeroese',
'fa' : 'Farsi',
'fj' : 'Fiji',
'fi' : 'Finnish',
'fr' : 'French',
'fy' : 'Frisian',
'gl' : 'Galician',
'gd' : 'Gaelic (Scottish)',
'gv' : 'Gaelic (Manx)',
'ka' : 'Georgian',
'de' : 'German',
'el' : 'Greek',
'kl' : 'Greenlandic',
'gn' : 'Guarani',
'gu' : 'Gujarati',
'ht' : 'Haitian Creole',
'ha' : 'Hausa',
'he' : 'Hebrew',
'hi' : 'Hindi',
'hu' : 'Hungarian',
'is' : 'Icelandic',
'io' : 'Ido',
'in' : 'Indonesian',
'ia' : 'Interlingua',
'ie' : 'Interlingue',
'iu' : 'Inuktitut',
'ik' : 'Inupiak',
'ga' : 'Irish',
'it' : 'Italian',
'ja' : 'Japanese',
'jv' : 'Javanese',
'kn' : 'Kannada',
'ks' : 'Kashmiri',
'kk' : 'Kazakh',
'rw' : 'Kinyarwanda (Ruanda)',
'ky' : 'Kirghiz',
'rn' : 'Kirundi (Rundi)',
'ko' : 'Korean',
'ku' : 'Kurdish',
'lo' : 'Laothian',
'la' : 'Latin',
'lv' : 'Latvian (Lettish)',
'li' : 'Limburgish ( Limburger)',
'ln' : 'Lingala',
'lt' : 'Lithuanian',
'mk' : 'Macedonian',
'mg' : 'Malagasy',
'ms' : 'Malay',
'ml' : 'Malayalam',
'mt' : 'Maltese',
'mi' : 'Maori',
'mr' : 'Marathi',
'mo' : 'Moldavian',
'mn' : 'Mongolian',
'na' : 'Nauru',
'ne' : 'Nepali',
'no' : 'Norwegian',
'oc' : 'Occitan',
'or' : 'Oriya',
'om' : 'Oromo (Afan, Galla)',
'ps' : 'Pashto (Pushto)',
'pl' : 'Polish',
'pt' : 'Portuguese',
'pa' : 'Punjabi',
'qu' : 'Quechua',
'rm' : 'Rhaeto-Romance',
'ro' : 'Romanian',
'ru' : 'Russian',
'sm' : 'Samoan',
'sg' : 'Sangro',
'sa' : 'Sanskrit',
'sr' : 'Serbian',
'sh' : 'Serbo-Croatian',
'st' : 'Sesotho',
'tn' : 'Setswana',
'sn' : 'Shona',
'ii' : 'Sichuan Yi',
'sd' : 'Sindhi',
'si' : 'Sinhalese',
'ss' : 'Siswati',
'sk' : 'Slovak',
'sl' : 'Slovenian',
'so' : 'Somali',
'es' : 'Spanish',
'su' : 'Sundanese',
'sw' : 'Swahili (Kiswahili)',
'sv' : 'Swedish',
'tl' : 'Tagalog',
'tg' : 'Tajik',
'ta' : 'Tamil',
'tt' : 'Tatar',
'te' : 'Telugu',
'th' : 'Thai',
'bo' : 'Tibetan',
'ti' : 'Tigrinya',
'to' : 'Tonga',
'ts' : 'Tsonga',
'tr' : 'Turkish',
'tk' : 'Turkmen',
'tw' : 'Twi',
'ug' : 'Uighur',
'uk' : 'Ukrainian',
'ur' : 'Urdu',
'uz' : 'Uzbek',
'vi' : 'Vietnamese',
'vo' : 'Volapuk',
'wa' : 'Wallon',
'cy' : 'Welsh',
'wo' : 'Wolof',
'xh' : 'Xhosa',
'yi' : 'Yiddish',
'yo' : 'Yoruba',
'zu' : 'Zulu',}