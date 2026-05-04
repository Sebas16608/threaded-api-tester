import argparse
import json

import httpx


def login(endpoint, data):
    try:
        data_dict = json.loads(data)
    except json.JSONDecodeError:
        print("json invalido")
        return

    response = httpx.post(endpoint, json=data_dict)

    print("Status code", response.status_code)

    try:
        print(response.json())
    except Exception as e:
        print(response.text, e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--endpoint", required=True)
    parser.add_argument("--data", required=True)

    args = parser.parse_args()

    login(args.endpoint, args.data)
