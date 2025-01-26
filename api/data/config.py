import os
from dotenv import load_dotenv

TORTOISE_ORM = {
    'connections': {
        'default': 'sqlite://./dev.db'
    },
    'apps': {
        'models': {
            'models': [
                'app.models.ModelUser'
                ],
            'default_connection': 'default',
        }
    }
}