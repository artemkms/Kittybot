# test_work_with_secrets.py

import os

from dotenv import load_dotenv

load_dotenv()
# Теперь переменная TOKEN, описанная в файле .env,
# доступна в пространстве переменных окружения

token = os.getenv('TOKEN')
print(token)  # 1896714192:AAFmXXXXPEn6KqewJ13kKKtlnBYqVC_XXXX
