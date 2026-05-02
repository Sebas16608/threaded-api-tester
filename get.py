import os

import requests
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("URL")
"""cambiar el token despues de cada login"""
header = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc3NjYwMDc3LCJpYXQiOjE3Nzc2NTY0NzcsImp0aSI6IjA2NjVjMzNmNmQ5ZTQxOWQ4ZTA2MjRmNDFiNWE3YzcwIiwidXNlcl9pZCI6IjE4In0.7j9U_yjRHj8I7ZAUvceXKjRLkalQb5VnyAVT5DIRTS0"
}


def getRequest():
    response = requests.get(str(url), headers=header)
    print(response.status_code)
