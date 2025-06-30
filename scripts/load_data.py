import pandas as pd
from db_connection import conectar_db

def guardar_en_db(df: pd.DataFrame, tabla="zoom_users"):
    try:
        if df.empty:
            print("⚠️ El DataFrame está vacío. No se insertó nada.")
            return

        engine = conectar_db()
        df.to_sql(name=tabla, con=engine, if_exists="replace", index=False)
        print(f"✅ Datos insertados correctamente en la tabla `{tabla}`.")
    except Exception as e:
        print(f"❌ Error al insertar en la base de datos: {e}")
