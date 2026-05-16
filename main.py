from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from faker import Faker
from dotenv import load_dotenv
import os

# cargar variables del .env
load_dotenv()

# datos conexión
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
DATABASE = os.getenv("DB_NAME")

# conexión mysql
DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

engine = create_engine(DATABASE_URL)

# base modelo
Base = declarative_base()

# tabla
class Persona(Base):
    __tablename__ = "personas_jonathan"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))
    correo = Column(String(100))
    ciudad = Column(String(100))
    pais = Column(String(100))
    telefono = Column(String(50))
    profesion = Column(String(100))
    empresa = Column(String(100))
    fecha_nacimiento = Column(Date)

# crear tabla
Base.metadata.create_all(engine)

# sesión
Session = sessionmaker(bind=engine)
session = Session()

# faker
fake = Faker("es_ES")

# generar datos
def generar_personas(cantidad=100000):

    personas = []

    for _ in range(cantidad):

        persona = Persona(
            nombre=fake.name(),
            correo=fake.email(),
            ciudad=fake.city(),
            pais=fake.country(),
            telefono=fake.phone_number(),
            profesion=fake.job(),
            empresa=fake.company(),
            fecha_nacimiento=fake.date_of_birth(minimum_age=18, maximum_age=80)
        )

        personas.append(persona)

    return personas

# función principal
def main():

    print("Generando registros...")

    personas = generar_personas()

    print("Insertando en MySQL...")

    session.bulk_save_objects(personas)
    session.commit()

    print("100000 registros insertados correctamente")

# ejecutar
if __name__ == "__main__":
    main()