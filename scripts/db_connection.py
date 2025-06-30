from sqlalchemy import create_engine

DB_HOST = "Host"
DB_PORT = "Port"
DB_NAME = "database"
DB_USER = "user"
DB_PASSWORD = "Password"

def conectar_db():
    connection_string = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    return create_engine(connection_string)
