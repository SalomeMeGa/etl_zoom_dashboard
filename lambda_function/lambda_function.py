import requests
import pandas as pd
from requests.auth import HTTPBasicAuth
from sqlalchemy import create_engine
import json


client_id = "Id Client"
client_secret = "ID secret"
account_id = "Id account"

DB_HOST = "host"
DB_PORT = "port"
DB_NAME = "data base"
DB_USER = "user"
DB_PASSWORD = "Passwordd"


def zoom_connect():
    url = f"https://zoom.us/oauth/token?grant_type=account_credentials&account_id={account_id}"
    response = requests.post(url, auth=HTTPBasicAuth(client_id, client_secret))
    if response.status_code == 200:
        access_token = response.json().get("access_token")
        return {"Authorization": f"Bearer {access_token}"}
    else:
        raise Exception("No se pudo obtener el token de Zoom.")


def obtener_usuarios():
    headers = zoom_connect()
    url = "https://api.zoom.us/v2/phone/users?page_size=100"
    users = []

    while url:
        r = requests.get(url, headers=headers)
        data = r.json()
        users.extend(data.get("users", []))
        token = data.get("next_page_token")
        url = f"https://api.zoom.us/v2/phone/users?page_size=100&next_page_token={token}" if token else None

    df = pd.json_normalize(users)
    result = []

    for user_id, name in zip(df["id"], df["name"]):
        r = requests.get(f"https://api.zoom.us/v2/users/{user_id}/presence_status", headers=headers)
        presence = r.json().get("status")
        result.append({"user_id": user_id, "name": name, "presence_status": presence})

    return pd.DataFrame(result)

def guardar_en_rds(df):
    engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    df.to_sql(name="zoom_users", con=engine, if_exists="replace", index=False)


def lambda_handler(event, context):
    try:
        df = obtener_usuarios()
        if df.empty:
            return {"statusCode": 200, "body": json.dumps("No hay datos.")}
        guardar_en_rds(df)
        return {"statusCode": 200, "body": json.dumps("Datos guardados en RDS.")}
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps(str(e))}
