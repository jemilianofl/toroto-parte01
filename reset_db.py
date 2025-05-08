# Solo usar en casos de emergencia para reiniciar la base de datos

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()
RAILWAY_URL = os.getenv("POSTGRES_URL")

# Conexión a PostgreSQL (Railway)
engine = create_engine(RAILWAY_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Confirmación del usuario
confirm = input("⚠️ Esto eliminará todos los datos de la base de datos. ¿Deseas continuar? (s/n): ")
if confirm.lower() != 's':
    print("⏹️ Operación cancelada.")
    exit()

# Eliminar y recrear las tablas
print("🧹 Eliminando todas las tablas existentes...")
Base.metadata.drop_all(engine)
print("✅ Tablas eliminadas.")

print("🛠️ Recreando todas las tablas...")
Base.metadata.create_all(engine)
print("🎉 Base de datos reiniciada correctamente y lista para usarse.")