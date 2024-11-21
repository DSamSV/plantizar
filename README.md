https://chatgpt.com/share/673fb844-af2c-8012-8ba2-d6eb5bff25d2

# Script para Realizar Peticiones a la API de Plantizar

Este script permite realizar peticiones a la API de `https://palmizador.sioma.app/plantizar` utilizando datos provenientes de una base de datos. Los datos son extraídos y las peticiones son enviadas para cada persona registrada en la base de datos.

## Requisitos

- Python 3.x
- Paquetes de Python: `pymysql`, `requests`, `python-dotenv`

## Pasos para la Instalación

### 1. Instalar Python
Si aún no tienes Python instalado, puedes descargarlo desde la página oficial:
https://www.python.org/downloads/

### 2. Crear un Entorno Virtual (Opcional pero recomendado)
Para mantener tu proyecto aislado, puedes crear un entorno virtual:

```bash
python -m venv env
```

Activa el entorno virtual:

- En Windows: 
  ```bash
  env\Scriptsctivate
  ```
- En macOS/Linux:
  ```bash
  source env/bin/activate
  ```

### 3. Instalar las Dependencias

Instala las bibliotecas necesarias usando `pip`:

```bash
pip install pymysql requests python-dotenv
```

### 4. Configurar el Archivo `.env`

Crea un archivo llamado `.env` en la raíz del proyecto con las siguientes variables:

```
DB_HOST=localhost
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_NAME=tu_base_de_datos
```

Asegúrate de reemplazar los valores con las credenciales correctas de tu base de datos.

### 5. Modificar el Script

Descarga o copia el script proporcionado en un archivo llamado `peticiones.py`. Asegúrate de revisar y modificar el valor de `labor_id` en el script si es necesario.

### 6. Ejecutar el Script

Para ejecutar el script, abre una terminal y navega a la carpeta donde guardaste el archivo `peticiones.py`, luego ejecuta:

```bash
python peticiones.py
```

El script realizará consultas a la base de datos y enviará peticiones HTTP a la API con los datos de cada `persona_id` y `fecha`.

## Explicación del Script

### Base de Datos
El script se conecta a la base de datos utilizando los parámetros configurados en el archivo `.env`. La consulta SQL obtiene los valores de `persona_id` y `fecha` de la tabla configurada en el script.

### Envío de Peticiones
Por cada registro obtenido de la base de datos, se realiza una petición `POST` a la URL de la API, enviando un JSON con el formato:

```json
{
    "finca_id": 513,
    "labor_id": <valor_de_labor_id>,
    "persona_id": <persona_id_obtenido>,
    "fecha": <fecha_obtenida>
}
```

### Control de Velocidad
El script incluye un retraso de 0.5 segundos entre cada petición para evitar sobrecargar el servidor.

### Manejo de Errores
El script maneja errores de conexión a la base de datos y errores en las peticiones HTTP. Los resultados de cada petición son impresos en la consola.

## Personalización

Puedes modificar el valor de `labor_id` directamente en el script, o agregar más lógica para automatizarlo si es necesario.

## Licencia

Este script es de uso libre. Si tienes alguna duda o necesitas ayuda, no dudes en contactarnos.

