import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "scripts")))

from extract_users import obtener_datos_usuarios
from load_data import guardar_en_db

if __name__ == "__main__":
    df = obtener_datos_usuarios()

    if not df.empty:
        print(df.head())
        guardar_en_db(df)
    else:
        print("No se obtuvieron datos.")
