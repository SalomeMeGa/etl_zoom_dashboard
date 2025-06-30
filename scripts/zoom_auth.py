import requests
from requests.auth import HTTPBasicAuth

CLIENT_ID = "Id Client"
CLIENT_SECRET = "Id Secret"
ACCOUNT_ID = "ID account"

def obtener_token_zoom():
    url = f"https://zoom.us/oauth/token?grant_type=account_credentials&account_id={ACCOUNT_ID}"

    try:
        response = requests.post(url, auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET))
        response.raise_for_status()

        data = response.json()
        access_token = data.get("access_token")

        if not access_token:
            raise ValueError("No se recibió token de acceso")

        return access_token

    except requests.RequestException as e:
        print(f"[ERROR] Falló la autenticación con Zoom: {e}")
        return None
