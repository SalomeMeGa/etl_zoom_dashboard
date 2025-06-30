import requests
import pandas as pd
from scripts.zoom_auth import obtener_token_zoom

def obtener_datos_usuarios():
   
    token = obtener_token_zoom()

    if not token:
        print("[ERROR] No se pudo obtener el token de autenticación.")
        return pd.DataFrame()

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    url = 'https://api.zoom.us/v2/phone/users?page_size=100'
    usuarios = []

   
    while url:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"[ERROR] Error al obtener usuarios: {response.status_code}")
            break

        data = response.json()
        usuarios.extend(data.get('users', []))
        next_token = data.get('next_page_token')
        url = f"https://api.zoom.us/v2/phone/users?page_size=100&next_page_token={next_token}" if next_token else None

    
    if not usuarios:
        return pd.DataFrame()

    usuarios_df = pd.json_normalize(usuarios)
    id_name_map = dict(zip(usuarios_df['id'], usuarios_df['name']))

    resultados = []

    for user_id in usuarios_df['id']:
        try:
            url_presencia = f"https://api.zoom.us/v2/users/{user_id}/presence_status"
            r = requests.get(url_presencia, headers=headers)
            r.raise_for_status()
            status = r.json().get("status", "desconocido")

            resultados.append({
                "user_id": user_id,
                "name": id_name_map.get(user_id, ""),
                "presence_status": status
            })

        except requests.RequestException as e:
            print(f"[ERROR] No se pudo obtener presencia de {user_id}: {e}")
            continue

    return pd.DataFrame(resultados)
