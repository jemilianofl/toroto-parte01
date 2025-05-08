from sqlalchemy import create_engine
from models import Base
import os
from dotenv import load_dotenv

load_dotenv()
POSTGRES_URL = os.getenv("POSTGRES_URL")

engine = create_engine(POSTGRES_URL)
Base.metadata.create_all(engine)
print("✅ Tablas creadas correctamente.")