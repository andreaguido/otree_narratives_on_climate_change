from os import environ

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []
USE_POINTS = False
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')
DEMO_PAGE_INTRO_HTML = """ """
SECRET_KEY = '5249757042491'
SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0.00,
    fill_auto=False,
    test=False
)
DEBUG = False

# oTree and wtforms have no Romanian locale: oTree runs in English,
# the questionnaire text is selected by SURVEY_LANGUAGE.
LANGUAGE_CODE = 'en'
SURVEY_LANGUAGE = 'ro'
REAL_WORLD_CURRENCY_CODE = 'MDL'
REAL_WORLD_CURRENCY_NAME = 'Moldovan Leu'
SESSION_CONFIGS = [
    dict(
        name = 'only_climate_change',
        app_sequence=['climate_questionnaire'],
        num_demo_participants=1,
        #prolific_link = "",
        prolific = False,
        url_validate = "",
        url_return = ""

)
]

ROOMS = [
    dict(
            name='moldova_lab',
            display_name='Moldova - Lab'
        )
]
