# taller3-bases-de-datos
Taller 3 Base de Datos
# Actividad 3 - Bases de Datos

Proyecto desarrollado en Python utilizando SQLAlchemy y Faker para crear y poblar una base de datos MySQL con 100.000 registros falsos.

## Tecnologías utilizadas

- Python
- SQLAlchemy
- Faker
- MySQL
- python-dotenv

## Instalación

1. Clonar el repositorio

```bash
git clone https://github.com/davidtimana0327-dotcom/actividad3_bd.git
```

2. Crear entorno virtual

```bash
python3 -m venv .venv
```

3. Activar entorno virtual

```bash
source .venv/bin/activate
```

4. Instalar dependencias

```bash
pip install -r requirements.txt
```

## Configuración

Crear un archivo `.env` con las siguientes variables:

```env
DB_USER=root
DB_PASSWORD=tu_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=taller3
```

## Ejecución

Ejecutar el script con:

```bash
python3 main.py
```

## Resultado

El script crea automáticamente la tabla `personas_jonathan` e inserta 100.000 registros en MySQL.
