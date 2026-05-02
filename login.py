import os

import requests
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("LOGIN")

login = {"email": os.getenv("EMAIL"), "password": os.getenv("PASSWORD")}

x = requests.post(str(url), json=login)

if x.status_code == 200:
    data3 = x.json()
    print(data3)
