import os
from dotenv import load_dotenv

load_dotenv('data/settings.env')

token = os.getenv('token')

async def validate_env_var(var_name, var_value):
    if not var_value:
        raise ValueError(f'Перменная окружения {var_name} не может быть пустой. Проверьте файл settings.env')
    
validate_env_var('token', token)