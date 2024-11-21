import pymysql
import requests
import time
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

# Configuración de la base de datos desde el archivo .env
DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USERNAME'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_DATABASE'),
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

# URL para las peticiones
URL = "https://palmizador.sioma.app/plantizar"

# Función para realizar la consulta
def obtener_datos():
    try:
        connection = pymysql.connect(**DB_CONFIG)
        with connection.cursor() as cursor:
            query = """
                SELECT labor_id,persona_id, fecha
                from labores_dia_personas ldp 
                where finca_id =513 and labor_id in (232,233) and fecha>='2024-06-01' order by fecha desc;
            """
            cursor.execute(query)
            return cursor.fetchall()
    except Exception as e:
        print(f"Error al conectarse a la base de datos: {e}")
        return []
    finally:
        if connection:
            connection.close()

# Función para enviar peticiones a la API
def enviar_peticion(persona_id, fecha, labor_id):
    body = {
        "finca_id": 513,
        "labor_id": labor_id,
        "persona_id": persona_id,
        "fecha": fecha
    }
    try:
        response = requests.post(URL, json=body,verify=False)
        if response.status_code == 200:
            print(f"Éxito: Persona ID {persona_id} - {response.json()}")
        else:
            print(f"Error {response.status_code} para Persona ID {persona_id}: {response.text}")
    except Exception as e:
        print(f"Error al realizar la petición para Persona ID {persona_id}: {e}")

# Función principal
if __name__ == "__main__":
    datos = obtener_datos()
    if datos:
        for fila in datos:
            persona_id = fila['persona_id']
            fecha = fila['fecha'].strftime('%Y-%m-%d')
            labor_id=fila['labor_id']
            enviar_peticion(persona_id, fecha, labor_id)
            time.sleep(5)  # Espera entre peticiones para evitar sobrecargar el servidor (ajusta si es necesario)
    else:
        print("No se obtuvieron datos de la base de datos.")
