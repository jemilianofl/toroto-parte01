from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, String, Integer, Float, Date, ForeignKey
import uuid

Base = declarative_base()

def generate_uuid():
    return str(uuid.uuid4())

class Proyecto(Base):
    __tablename__ = 'proyectos'
    id = Column(String, primary_key=True, default=generate_uuid)
    nombre = Column(String, unique=True, nullable=False)

class Cuadrilla(Base):
    __tablename__ = 'cuadrillas'
    id = Column(String, primary_key=True, default=generate_uuid)
    nombre = Column(String, unique=True, nullable=False)

class Responsable(Base):
    __tablename__ = 'responsables'
    id = Column(String, primary_key=True, default=generate_uuid)
    nombre = Column(String, nullable=False)
    correo = Column(String, unique=True, nullable=False)
    rol = Column(String, nullable=False)

class Obra(Base):
    __tablename__ = 'obras'
    id = Column(String, primary_key=True)
    obra_excel_id = Column(String, unique=True, nullable=False)
    proyecto_id = Column(String, ForeignKey('proyectos.id'))
    cuadrilla_id = Column(String, ForeignKey('cuadrillas.id'))
    responsable_id = Column(String, ForeignKey('responsables.id'))
    fase = Column(String)
    actividad = Column(String)
    tipo_obra = Column(String)
    nombre_obra = Column(String)
    estado = Column(String)
    fecha_inicio = Column(Date)
    fecha_fin = Column(Date)
    coordenadas = Column(String)
    geometria = Column(String)
    base_mayor_m = Column(Float)
    base_menor_m = Column(Float)
    alto_m = Column(Float)
    largo_m = Column(Float)
    largo_azolve_m = Column(Float)
    volumen_construccion_m3 = Column(Float)
    volumen_almacenamiento_m3 = Column(Float)
    area_m2 = Column(Float)
    observaciones = Column(String)

class Evidencia(Base):
    __tablename__ = 'evidencias'
    id = Column(String, primary_key=True, default=generate_uuid)
    obra_id = Column(String, ForeignKey('obras.id'))
    url = Column(String)