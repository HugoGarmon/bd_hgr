# SISTEMAS DE BIG DATA - Examen 1ª Evaluación

**Instrucciones generales**

1.	Todas las sentencias deben ejecutarse desde la línea de comandos en las celdas que hay después del enunciado. No debes realizar ninguna tarea desde fuera de Jupyter.
2.	Puedes **añadir** todas las celdas que necesites siempre y cuando estén antes del siguiente enunciado.
3.	Todas las celdas **deben estar ejecutadas** y debe visualizarse el resultado de salida.
4.	**No es necesario documentar** las respuestas, simplemente debes hacer lo que se pide en el enunciado.
5.	Después de cada parte debes insertar una **captura de pantalla** del cliente gráfico de la base de datos correspondientes donde se vea que los datos se han cargado correctamente.
6.	Debes entregar tanto el **notebook** (fichero `.ipynb`) como el mismo fichero convertido a **PDF** (es muy probable que si intentas convertirlo en el propio contenedor te falle por no tener instalado `pandoc`, si es así descargalo en formato `.md` o `html` y conviértelo en tu máquina física).

---

**NOMBRE**: Hugo Garmón Rey

---

## Contexto del escenario

Has sido contratado por una fábrica inteligente que dispone de sensores de temperatura y vibración en sus máquinas críticas. La empresa necesita un sistema backend capaz de procesar los datos que llegan de los sensores en tiempo real.

El sistema debe cumplir dos objetivos simultáneos:

1.  **Monitorización en vivo (Dashboard):** los operarios necesitan saber el estado *actual* de cada máquina y si hay alguna alarma activa en este preciso instante. Para esto usarás **Redis**.
2.  **Histórico para mantenimiento predictivo:** el equipo de Data Science necesita almacenar todos los datos brutos a lo largo del tiempo para entrenar modelos de IA futuros. Para esto usarás **InfluxDB**.

## Los Datos de Entrada

Los datos con los que vas a trabajar los tienes en el *dataset* sintético adjunto llamado `sensores.csv`. Este *dataset* contiene lecturas simuladas con las siguientes columnas:

  - `timestamp`: fecha y hora del evento.
  - `machine_id`: identificador único de la máquina.
  - `zone`: zona de la fábrica.
  - `temperature`: temperatura en grados Celsius.
  - `vibration`: nivel de vibración (0-100).
  - `lat`, `lon`: coordenadas del robot.
  - `status`: estado reportado por la máquina ("OK", "WARNING", "ERROR").

**IMPORTANTE**

El desarrollo del examen debe de ser modular, con un programa principal que inicialice las conexiones a la base de datos y lea los datos del fichero y luego invocará **una función diferente para cargar cada tipo de dato** en la base de datos

Es decision tuya elegir los parámetros que recibirá cada función, aunque es altamente aconsejable **no utilizar variables globales**.

## Parte A: Persistencia histórica (InfluxDB)

`2 puntos`

En esta parte tienes que crear un script que lea el fichero CSV facilitado y almacene los datos en una base de datos InfluxDB.

Los aspectos que tienes que tener en cuenta son:

  - **Bucket:** `factory_logs`
  - **Measurement:** `maquinaria`
  - **Requisito clave:** debes modelar correctamente los datos usando adecuadamente *tags* o *fields* según el tipo de datos. Se debe respetar el `timestamp` del datos (no usar el tiempo de ingesta).


```python
# Función que carga los datos en InfluxDB

import influxdb_client
from datetime import datetime,timezone
from influxdb_client import Point, WriteOptions

writeoptions = WriteOptions(
        batch_size = 500,
        flush_interval = 1,
        write_type = "SYNCHRONOUS"
    )


writre_api = client.write_api(write_options=writeoptions)

def cargarDatos(csv_):
    with open(csv_) as f:
        lector = csv.reader(f)

        next(lector)

        for row in lector:
            date_ = row[0]
            dt = datetime.strptime(date_,"%Y-%m-%d %H:%M:%S")
            dt_utc = dt.replace(tzinfo=timezone.utc)
            time_date = dt_utc.isoformat().replace('+00:00','Z')
            machine_id = row[1]
            zone = row[2]
            temperature = float(row[3])
            vibration = float(row[4])
            lat = float(row[5])
            lon = float(row[6])
            status = row[7]
    
        
            p = Point("maquinaria").time(time_date).tag("machine_id",machine_id).tag("zone",zone).tag("status",status) \
            .field("lat",lat).field("lon",lon).field("temperature",temperature).field("vibration",vibration) \
        
        
            writre_api.write(bucket="factory_logs" , org="docs" , record=p)


writre_api.close()
```


```python
import os 
import csv


from influxdb_client.client.write_api import ASYNCHRONOUS
from influxdb_client.client.exceptions import InfluxDBError
from urllib3.exceptions import NewConnectionError


data = os.listdir("./pro206/data/crypto_files")

INFLUX_URL = "http://influxdb2:8086"
INFLUX_TOKEN = "MyInitialAdminToken0=hola"

client = None
try:
    client = influxdb_client.InfluxDBClient(
        url=INFLUX_URL,
        token=INFLUX_TOKEN,
        org="docs"
    )

    print(f"Verificando estado de salud de InfluxDB en {INFLUX_URL}...")
    health = client.health()

    if health.status == "pass":
        print("Conexión exitosa")
    else:
        print("Conexión fallida")

except(InfluxDBError,NewConnectionError) as e:
    print("Error")
    print(e)


cargarDatos("./examen/telemetria_agv.csv")
```

    Verificando estado de salud de InfluxDB en http://influxdb2:8086...
    Conexión exitosa


## Parte B - Analítica en tiempo real con Redis

Debes crear un script que alimente las siguientes estructuras en Redis por cada dato procesado:

### 1.- Estadísticas agregadas

`1 punto`

Al procesar masivamente datos de telemetría, es costoso consultar la base de datos histórica (InfluxDB) para preguntas simples como "¿Cuál ha sido la temperatura máxima hoy en el Almacén A?". Vamos a usar Redis Hashes para mantener un marcador actualizado de estadísticas por zona.

Para cada fila procesada del CSV, debes actualizar un Hash correspondiente a la Zona (zone) donde se encuentra el robot.

- **Clave:** `stats:zone:{nombre_zona}` (Ej: stats:zone:Almacen_A, stats:zone:Recepcion...).
- **Campos:**:
    - `total_lecturas`: contador total de datos recibidos de esa zona.
    - `total_errores`: contador de cuántas veces el status ha sido "ERROR".
    - `max_temp`: La temperatura más alta registrada hasta el momento en esa zona.


```python
# Función que genera las estadísticas agregadas

import os 
import csv

def estadisticasZona(csv_):
   

    cont = 0
    cont_error = 0
    max_temp = 0.0
    zona_actual = None

    with open(csv_) as f:
        lector = csv.reader(f)

        next(lector)

        for row in lector:
            zone = row[2]
            temperature = float(row[3])
            status = row[7]

            if zona_actual == None:
                zona_actual = zone
                zone_key = f"stats:zone:{zona_actual}"

            if zone == zona_actual:
                zone_key = f"stats:zone:{zona_actual}"
                cont = cont+1
                if temperature >= max_temp:
                    max_temp = temperature
                if status == "ERROR":
                    cont_error = cont_error+1

                dic = {
                    "Total_lecturas" : cont,
                    "Total_errores" : cont_error,
                    "Max_temp" : max_temp
                }   

            if zone != zona_actual:
                r.hset(zone_key,mapping=dic)
                
                
                zona_actual = zone 
            
    
    

   
    


```

### 2.- Ranking de "puntos calientes" (Sorted Set)

`1 punto`

El jefe de planta quiere ver en una pantalla un "Top de Máquinas con mayor temperatura" ordenado de mayor a menor en tiempo real.

- **Estructura:** `Sorted Set` (ZSET)
- **Clave:** `dashboard:hottest_machines`
- **Score:** La temperatura actual (`temperature`).
- **Member:** El ID de la máquina (`machine_id`).


```python
# Función que carga el sorted set

def cargarSorted():
    zonas = ["Almacen_A","Almacen_B","Recepción","Expediciones","Ensamblaje"]

    for i in zonas:
        zone_key = f"stats:zone:{i}"
        zone_data = r.hgetall(zone_key)
        
        for k , v in zone_data.items():
            leaderboard_key = "dashboard:hottest_machines"
            r.zadd(leaderboard_key,{zone_key : float(v)})
        


        
        


```

### 3.- Seguimiento de flota (Geospatial)

`1 punto`

Las máquinas de este escenario son AGVs (robots móviles) que se mueven por la planta. Necesitamos saber su ubicación exacta.

- **Estructura:** `Geo`
- **Clave:** `factory:map`
- **Datos:** Usa la latitud y longitud que vienen en el CSV para posicionar el `machine_id`.


```python
# Función que carga los datos geoespaciales

def cargarDatosGeo(csv_):
    with open(csv_) as f:
        lector = csv.reader(f)

        next(lector)

        for row in lector:
            machine_id = row[1]
            lat = float(row[5])
            lon = float(row[6])
            
            r.geoadd("factory:map",(lon,lat,machine_id))
            

        
        
          

```

### 4.- Contadores globales atómicos (String)

`1 punto`

Necesitamos estadísticas rápidas que no requieran contar filas en una base de datos histórica.

- **Estructura:** `String` (Contador)
- **Clave:** `stats:total_processed` -\> Incrementar en 1 por cada fila procesada.
- **Clave:** `stats:total_errors` -\> Incrementar en 1 solo si el `status` es "ERROR".
- **Clave:** `stats:total_warnings` -\> Incrementar en 1 solo si el `status` es "WARNING".




```python
def contadores(csv_):
    
    cont = 0
    error = 0
    war = 0
    
    with open(csv_) as f:
        lector = csv.reader(f)

        next(lector)

        for row in lector:
            status = row[7]            
            if status == "ERROR":
                error = error + 1
            if status == "WARNING":
                war = war + 1 

            cont = cont + 1
    
    r.set("stats:total_processed", cont)
    r.set("stats:total_errors", error)
    r.set("stats:total_warning", war)

```

### 5.- Cola de anomalías críticas (List)

`1 punto`

Queremos tener también una cola de anomalías críticas. Por cada registro cuyo `status` sea `ERROR` deberás crear un JSON y almacenarlo en una estructura tipo FIFO:

- **Estructura:** `List`
- **Clave:** `alerts:queue`
- **Datos:**: el JSON debe incluir: `machine_id`, `timestamp` y un mensaje: *"Critical failure at [Lat, Lon]"*.


```python
# Función que carga los datos en la cola
import json

def anomalias(csv_):
    
    cont = 0
    error = 0
    war = 0
    
    with open(csv_) as f:
        lector = csv.reader(f)

        next(lector)

        for row in lector:
            date_ = row[0]
            dt = datetime.strptime(date_,"%Y-%m-%d %H:%M:%S")
            dt_utc = dt.replace(tzinfo=timezone.utc)
            time_date = dt_utc.isoformat().replace('+00:00','Z')   
            machine_id = row[1]
            status = row[7]    
            lat = float(row[5])
            lon = float(row[6])  

            if status == "ERROR":
                dic = {
                    "machine_id" : machine_id,
                    "timestamp" : time_date,
                    "msg" : f"Critical failuere at {lat} {lon}"
                }  

                dic_json = json.dumps(dic)    

                r.rpush("alerts:queue",dic_json)
            

       
```

## Programa principal


```python
# Aquí debes insertar el programa principal que llama al resto de funciones
import redis 

r = redis.Redis(
    host='redis',
    port=6379,
    db=0,
    decode_responses=True)
r.ping()

estadisticasZona("./examen/telemetria_agv.csv")
cargarSorted()
cargarDatosGeo("./examen/telemetria_agv.csv")
contadores("./examen/telemetria_agv.csv")
anomalias("./examen/telemetria_agv.csv")
```

## Capturas de pantalla

A partir de aquí tienes que insertar las capturas de pantalla correspondientes a cada punto. Las capturas de pantalla corresponderán a la interfaz gráfica de la base de datos correspondiente y se debe mostrar que los datos se han cargado correctamente. Los apartados que no tengan la captura de pantalla correspondiente **se considerarán no realizados**.

### Captura de InfluxDB

![alt text](1.png)

### Captura de estadísticas agregadas

![alt text](2.png)

### Captura de ranking de puntos calientes

![alt text](3.png)

### Captura de seguimiento de flota

![alt text](4.png)

### Captura de contadores globales atómicos

![alt text](5.png)
![alt text](6.png)
![alt text](7.png)

### Captura de cola de anomalías críticas

![alt text](8.png)
