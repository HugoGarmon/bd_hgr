# SISTEMAS DE BIG DATA - Examen 2ª Evaluación

### **Nombre**:

**INSTRUCCIONES**:

- Si realizas este examen desde tu ordenador debes **grabar la pantalla** con OBS Studio en formato MKV y entregar el vídeo junto con el examen. Para entregarlo, debes subirlo a OneDrive y adjuntar fichero de texto con la URL del recurso compartido.
- Si lo haces en un equipo del centro, grabaré yo la pantalla desde el ordenador del profesor.
- Debes contestar cada pregunta del examen en la celda del cuaderno Jupyter que hay después de cada pregunta. Si necesitas más celdas, puedes agregarlas a continuación de la que hay.
- Todo tu código **tiene que estár ejecutado**.
- La **entrega** del examen práctico se realizará en el canal de Teams habilitado a tal efecto y consistirá en:
  - Notebook de Jupyter (`.ipynb`).
  - Notebook exportado en formato Markdown (`.md`)
  - Fichero de texto (`.txt.`) con la URL al vídeo compartido en caso de haberlo hecho en tu ordenador.
  - Estos tres ficheros deberán entregarse en un único fichero comprimido en formato ZIP (`.zip`) con el nombre `{apellidos}, {nombre} - SBD Ev2`

Ejecuta la siguiente celda para generar el archivo `flota_rebelde.txt` con el que trabajás en este examen


```python
%%writefile flota_rebelde.txt
name~!~base_asignada~!~naves_disponibles
CR90 corvette~!~Base Yavin 4~!~15
X-wing~!~Base Echo (Hoth)~!~120
Y-wing~!~Base Echo (Hoth)~!~45 naves
Millennium Falcon~!~Flota Nómada~!~1
A-wing~!~Base Endor~!~Error de sensor
Rebel transport~!~Punto de encuentro~!~Ocho
B-wing~!~Astillero Sullust~!~30
EF76 Nebulon-B escort frigate~!~Flota Nómada~!~4
Calamari Cruiser~!~Órbita Mon Cala~!~Desconocido
Star Destroyer~!~Hangar Secreto (Capturado)~!~2
```

    Writing flota_rebelde.txt


## EXAMEN PRÁCTICO: Logística de la flota rebelde

Trabajas en el equipo de logística y suministros de la Alianza Rebelde. Recientemente, habéis recibido un archivo de texto con el inventario actual de naves espaciales disponibles en vuestras bases secretas. Sin embargo, este archivo fue generado por un sistema antiguo y contiene errores de formato.

Tu misión es extraer este inventario, limpiarlo y cruzarlo con el catálogo oficial de naves de la API de Star Wars (SWAPI) para calcular la capacidad de carga total de la flota.



### Apartado A: Ingesta y limpieza de la fuente estática (2.5 puntos)

El sistema legado ha exportado el inventario en el archivo `flota_rebelde.txt`. Al inspeccionarlo, notas que el separador de columnas es una secuencia extraña de caracteres (`~!~`) y que la columna numérica tiene datos corruptos.

1.  Carga el archivo `flota_rebelde.txt` en un DataFrame de Pandas. 
2.  La columna `naves_disponibles` contiene basura textual en algunas filas (ej. "5 naves", "Error"). Lee inicialmente esta columna como texto (cadena).
3.  Limpia la columna `naves_disponibles` forzando su conversión a tipo numérico. Asegúrate de transformar los textos irreconocibles en valores nulos (`NaN`).
4.  Elimina las filas que hayan quedado con valor nulo en dicha columna.


```python
%cd examen2
```

    /home/jovyan/work/examen2



```python
import pandas as pd 

df = pd.read_csv("flota_rebelde.txt",sep=("~!~"))

s = df["naves_disponibles"]

df["naves_disponibles"] = pd.to_numeric(s, errors="coerce")

df = df.dropna()

df
```

    /tmp/ipykernel_4234/3222233922.py:3: ParserWarning: Falling back to the 'python' engine because the 'c' engine does not support regex separators (separators > 1 char and different from '\s+' are interpreted as regex); you can avoid this warning by specifying engine='python'.
      df = pd.read_csv("flota_rebelde.txt",sep=("~!~"))





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>base_asignada</th>
      <th>naves_disponibles</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>CR90 corvette</td>
      <td>Base Yavin 4</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>X-wing</td>
      <td>Base Echo (Hoth)</td>
      <td>120.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Millennium Falcon</td>
      <td>Flota Nómada</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>B-wing</td>
      <td>Astillero Sullust</td>
      <td>30.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>EF76 Nebulon-B escort frigate</td>
      <td>Flota Nómada</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Star Destroyer</td>
      <td>Hangar Secreto (Capturado)</td>
      <td>2.0</td>
    </tr>
  </tbody>
</table>
</div>




### Apartado B: Extracción de datos desde API REST (2.5 puntos)

Necesitamos obtener las especificaciones técnicas oficiales de todas las naves del universo Star Wars.

1.  Utilizando la librería `requests`, realiza peticiones `GET` al endpoint oficial de naves: `https://swapi.dev/api/starships/`.
2.  Carga la lista completa de naves en un único DataFrame de Pandas llamado `df_catalogo`.

*(Nota: Si no consigues hacer funcionar la petición a la API o la paginación, carga el archivo `swapi_starships_simulado.csv` en `df_catalogo` y continúa con el siguiente apartado).*


```python
%pip install requests
```

    Requirement already satisfied: requests in /opt/conda/lib/python3.11/site-packages (2.31.0)
    Requirement already satisfied: charset-normalizer<4,>=2 in /opt/conda/lib/python3.11/site-packages (from requests) (3.3.0)
    Requirement already satisfied: idna<4,>=2.5 in /opt/conda/lib/python3.11/site-packages (from requests) (3.4)
    Requirement already satisfied: urllib3<3,>=1.21.1 in /opt/conda/lib/python3.11/site-packages (from requests) (2.0.7)
    Requirement already satisfied: certifi>=2017.4.17 in /opt/conda/lib/python3.11/site-packages (from requests) (2023.7.22)
    Note: you may need to restart the kernel to use updated packages.



```python
import requests
import pandas as pd

url = "https://swapi.dev/api/starships/"

lista_dfs = [] 

while url:
    response = requests.get(url)
    data = response.json()

    df_pagina = pd.json_normalize(data["results"])
    lista_dfs.append(df_pagina)
    

    url = data["next"]

df_catalogo = pd.concat(lista_dfs, ignore_index=True)
df_catalogo
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>model</th>
      <th>manufacturer</th>
      <th>cost_in_credits</th>
      <th>length</th>
      <th>max_atmosphering_speed</th>
      <th>crew</th>
      <th>passengers</th>
      <th>cargo_capacity</th>
      <th>consumables</th>
      <th>hyperdrive_rating</th>
      <th>MGLT</th>
      <th>starship_class</th>
      <th>pilots</th>
      <th>films</th>
      <th>created</th>
      <th>edited</th>
      <th>url</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>CR90 corvette</td>
      <td>CR90 corvette</td>
      <td>Corellian Engineering Corporation</td>
      <td>3500000</td>
      <td>150</td>
      <td>950</td>
      <td>30-165</td>
      <td>600</td>
      <td>3000000</td>
      <td>1 year</td>
      <td>2.0</td>
      <td>60</td>
      <td>corvette</td>
      <td>[]</td>
      <td>[https://swapi.dev/api/films/1/, https://swapi...</td>
      <td>2014-12-10T14:20:33.369000Z</td>
      <td>2014-12-20T21:23:49.867000Z</td>
      <td>https://swapi.dev/api/starships/2/</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Star Destroyer</td>
      <td>Imperial I-class Star Destroyer</td>
      <td>Kuat Drive Yards</td>
      <td>150000000</td>
      <td>1,600</td>
      <td>975</td>
      <td>47,060</td>
      <td>n/a</td>
      <td>36000000</td>
      <td>2 years</td>
      <td>2.0</td>
      <td>60</td>
      <td>Star Destroyer</td>
      <td>[]</td>
      <td>[https://swapi.dev/api/films/1/, https://swapi...</td>
      <td>2014-12-10T15:08:19.848000Z</td>
      <td>2014-12-20T21:23:49.870000Z</td>
      <td>https://swapi.dev/api/starships/3/</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Sentinel-class landing craft</td>
      <td>Sentinel-class landing craft</td>
      <td>Sienar Fleet Systems, Cyngus Spaceworks</td>
      <td>240000</td>
      <td>38</td>
      <td>1000</td>
      <td>5</td>
      <td>75</td>
      <td>180000</td>
      <td>1 month</td>
      <td>1.0</td>
      <td>70</td>
      <td>landing craft</td>
      <td>[]</td>
      <td>[https://swapi.dev/api/films/1/]</td>
      <td>2014-12-10T15:48:00.586000Z</td>
      <td>2014-12-20T21:23:49.873000Z</td>
      <td>https://swapi.dev/api/starships/5/</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Death Star</td>
      <td>DS-1 Orbital Battle Station</td>
      <td>Imperial Department of Military Research, Sien...</td>
      <td>1000000000000</td>
      <td>120000</td>
      <td>n/a</td>
      <td>342,953</td>
      <td>843,342</td>
      <td>1000000000000</td>
      <td>3 years</td>
      <td>4.0</td>
      <td>10</td>
      <td>Deep Space Mobile Battlestation</td>
      <td>[]</td>
      <td>[https://swapi.dev/api/films/1/]</td>
      <td>2014-12-10T16:36:50.509000Z</td>
      <td>2014-12-20T21:26:24.783000Z</td>
      <td>https://swapi.dev/api/starships/9/</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Millennium Falcon</td>
      <td>YT-1300 light freighter</td>
      <td>Corellian Engineering Corporation</td>
      <td>100000</td>
      <td>34.37</td>
      <td>1050</td>
      <td>4</td>
      <td>6</td>
      <td>100000</td>
      <td>2 months</td>
      <td>0.5</td>
      <td>75</td>
      <td>Light freighter</td>
      <td>[https://swapi.dev/api/people/13/, https://swa...</td>
      <td>[https://swapi.dev/api/films/1/, https://swapi...</td>
      <td>2014-12-10T16:59:45.094000Z</td>
      <td>2014-12-20T21:23:49.880000Z</td>
      <td>https://swapi.dev/api/starships/10/</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Y-wing</td>
      <td>BTL Y-wing</td>
      <td>Koensayr Manufacturing</td>
      <td>134999</td>
      <td>14</td>
      <td>1000km</td>
      <td>2</td>
      <td>0</td>
      <td>110</td>
      <td>1 week</td>
      <td>1.0</td>
      <td>80</td>
      <td>assault starfighter</td>
      <td>[]</td>
      <td>[https://swapi.dev/api/films/1/, https://swapi...</td>
      <td>2014-12-12T11:00:39.817000Z</td>
      <td>2014-12-20T21:23:49.883000Z</td>
      <td>https://swapi.dev/api/starships/11/</td>
    </tr>
    <tr>
      <th>6</th>
      <td>X-wing</td>
      <td>T-65 X-wing</td>
      <td>Incom Corporation</td>
      <td>149999</td>
      <td>12.5</td>
      <td>1050</td>
      <td>1</td>
      <td>0</td>
      <td>110</td>
      <td>1 week</td>
      <td>1.0</td>
      <td>100</td>
      <td>Starfighter</td>
      <td>[https://swapi.dev/api/people/1/, https://swap...</td>
      <td>[https://swapi.dev/api/films/1/, https://swapi...</td>
      <td>2014-12-12T11:19:05.340000Z</td>
      <td>2014-12-20T21:23:49.886000Z</td>
      <td>https://swapi.dev/api/starships/12/</td>
    </tr>
    <tr>
      <th>7</th>
      <td>TIE Advanced x1</td>
      <td>Twin Ion Engine Advanced x1</td>
      <td>Sienar Fleet Systems</td>
      <td>unknown</td>
      <td>9.2</td>
      <td>1200</td>
      <td>1</td>
      <td>0</td>
      <td>150</td>
      <td>5 days</td>
      <td>1.0</td>
      <td>105</td>
      <td>Starfighter</td>
      <td>[https://swapi.dev/api/people/4/]</td>
      <td>[https://swapi.dev/api/films/1/]</td>
      <td>2014-12-12T11:21:32.991000Z</td>
      <td>2014-12-20T21:23:49.889000Z</td>
      <td>https://swapi.dev/api/starships/13/</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Executor</td>
      <td>Executor-class star dreadnought</td>
      <td>Kuat Drive Yards, Fondor Shipyards</td>
      <td>1143350000</td>
      <td>19000</td>
      <td>n/a</td>
      <td>279,144</td>
      <td>38000</td>
      <td>250000000</td>
      <td>6 years</td>
      <td>2.0</td>
      <td>40</td>
      <td>Star dreadnought</td>
      <td>[]</td>
      <td>[https://swapi.dev/api/films/2/, https://swapi...</td>
      <td>2014-12-15T12:31:42.547000Z</td>
      <td>2014-12-20T21:23:49.893000Z</td>
      <td>https://swapi.dev/api/starships/15/</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Rebel transport</td>
      <td>GR-75 medium transport</td>
      <td>Gallofree Yards, Inc.</td>
      <td>unknown</td>
      <td>90</td>
      <td>650</td>
      <td>6</td>
      <td>90</td>
      <td>19000000</td>
      <td>6 months</td>
      <td>4.0</td>
      <td>20</td>
      <td>Medium transport</td>
      <td>[]</td>
      <td>[https://swapi.dev/api/films/2/, https://swapi...</td>
      <td>2014-12-15T12:34:52.264000Z</td>
      <td>2014-12-20T21:23:49.895000Z</td>
      <td>https://swapi.dev/api/starships/17/</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Slave 1</td>
      <td>Firespray-31-class patrol and attack</td>
      <td>Kuat Systems Engineering</td>
      <td>unknown</td>
      <td>21.5</td>
      <td>1000</td>
      <td>1</td>
      <td>6</td>
      <td>70000</td>
      <td>1 month</td>
      <td>3.0</td>
      <td>70</td>
      <td>Patrol craft</td>
      <td>[https://swapi.dev/api/people/22/]</td>
      <td>[https://swapi.dev/api/films/2/, https://swapi...</td>
      <td>2014-12-15T13:00:56.332000Z</td>
      <td>2014-12-20T21:23:49.897000Z</td>
      <td>https://swapi.dev/api/starships/21/</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Imperial shuttle</td>
      <td>Lambda-class T-4a shuttle</td>
      <td>Sienar Fleet Systems</td>
      <td>240000</td>
      <td>20</td>
      <td>850</td>
      <td>6</td>
      <td>20</td>
      <td>80000</td>
      <td>2 months</td>
      <td>1.0</td>
      <td>50</td>
      <td>Armed government transport</td>
      <td>[https://swapi.dev/api/people/1/, https://swap...</td>
      <td>[https://swapi.dev/api/films/2/, https://swapi...</td>
      <td>2014-12-15T13:04:47.235000Z</td>
      <td>2014-12-20T21:23:49.900000Z</td>
      <td>https://swapi.dev/api/starships/22/</td>
    </tr>
    <tr>
      <th>12</th>
      <td>EF76 Nebulon-B escort frigate</td>
      <td>EF76 Nebulon-B escort frigate</td>
      <td>Kuat Drive Yards</td>
      <td>8500000</td>
      <td>300</td>
      <td>800</td>
      <td>854</td>
      <td>75</td>
      <td>6000000</td>
      <td>2 years</td>
      <td>2.0</td>
      <td>40</td>
      <td>Escort ship</td>
      <td>[]</td>
      <td>[https://swapi.dev/api/films/2/, https://swapi...</td>
      <td>2014-12-15T13:06:30.813000Z</td>
      <td>2014-12-20T21:23:49.902000Z</td>
      <td>https://swapi.dev/api/starships/23/</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Calamari Cruiser</td>
      <td>MC80 Liberty type Star Cruiser</td>
      <td>Mon Calamari shipyards</td>
      <td>104000000</td>
      <td>1200</td>
      <td>n/a</td>
      <td>5400</td>
      <td>1200</td>
      <td>unknown</td>
      <td>2 years</td>
      <td>1.0</td>
      <td>60</td>
      <td>Star Cruiser</td>
      <td>[]</td>
      <td>[https://swapi.dev/api/films/3/]</td>
      <td>2014-12-18T10:54:57.804000Z</td>
      <td>2014-12-20T21:23:49.904000Z</td>
      <td>https://swapi.dev/api/starships/27/</td>
    </tr>
    <tr>
      <th>14</th>
      <td>A-wing</td>
      <td>RZ-1 A-wing Interceptor</td>
      <td>Alliance Underground Engineering, Incom Corpor...</td>
      <td>175000</td>
      <td>9.6</td>
      <td>1300</td>
      <td>1</td>
      <td>0</td>
      <td>40</td>
      <td>1 week</td>
      <td>1.0</td>
      <td>120</td>
      <td>Starfighter</td>
      <td>[https://swapi.dev/api/people/29/]</td>
      <td>[https://swapi.dev/api/films/3/]</td>
      <td>2014-12-18T11:16:34.542000Z</td>
      <td>2014-12-20T21:23:49.907000Z</td>
      <td>https://swapi.dev/api/starships/28/</td>
    </tr>
    <tr>
      <th>15</th>
      <td>B-wing</td>
      <td>A/SF-01 B-wing starfighter</td>
      <td>Slayn &amp; Korpil</td>
      <td>220000</td>
      <td>16.9</td>
      <td>950</td>
      <td>1</td>
      <td>0</td>
      <td>45</td>
      <td>1 week</td>
      <td>2.0</td>
      <td>91</td>
      <td>Assault Starfighter</td>
      <td>[]</td>
      <td>[https://swapi.dev/api/films/3/]</td>
      <td>2014-12-18T11:18:04.763000Z</td>
      <td>2014-12-20T21:23:49.909000Z</td>
      <td>https://swapi.dev/api/starships/29/</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Republic Cruiser</td>
      <td>Consular-class cruiser</td>
      <td>Corellian Engineering Corporation</td>
      <td>unknown</td>
      <td>115</td>
      <td>900</td>
      <td>9</td>
      <td>16</td>
      <td>unknown</td>
      <td>unknown</td>
      <td>2.0</td>
      <td>unknown</td>
      <td>Space cruiser</td>
      <td>[]</td>
      <td>[https://swapi.dev/api/films/4/]</td>
      <td>2014-12-19T17:01:31.488000Z</td>
      <td>2014-12-20T21:23:49.912000Z</td>
      <td>https://swapi.dev/api/starships/31/</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Droid control ship</td>
      <td>Lucrehulk-class Droid Control Ship</td>
      <td>Hoersch-Kessel Drive, Inc.</td>
      <td>unknown</td>
      <td>3170</td>
      <td>n/a</td>
      <td>175</td>
      <td>139000</td>
      <td>4000000000</td>
      <td>500 days</td>
      <td>2.0</td>
      <td>unknown</td>
      <td>Droid control ship</td>
      <td>[]</td>
      <td>[https://swapi.dev/api/films/4/, https://swapi...</td>
      <td>2014-12-19T17:04:06.323000Z</td>
      <td>2014-12-20T21:23:49.915000Z</td>
      <td>https://swapi.dev/api/starships/32/</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Naboo fighter</td>
      <td>N-1 starfighter</td>
      <td>Theed Palace Space Vessel Engineering Corps</td>
      <td>200000</td>
      <td>11</td>
      <td>1100</td>
      <td>1</td>
      <td>0</td>
      <td>65</td>
      <td>7 days</td>
      <td>1.0</td>
      <td>unknown</td>
      <td>Starfighter</td>
      <td>[https://swapi.dev/api/people/11/, https://swa...</td>
      <td>[https://swapi.dev/api/films/4/, https://swapi...</td>
      <td>2014-12-19T17:39:17.582000Z</td>
      <td>2014-12-20T21:23:49.917000Z</td>
      <td>https://swapi.dev/api/starships/39/</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Naboo Royal Starship</td>
      <td>J-type 327 Nubian royal starship</td>
      <td>Theed Palace Space Vessel Engineering Corps, N...</td>
      <td>unknown</td>
      <td>76</td>
      <td>920</td>
      <td>8</td>
      <td>unknown</td>
      <td>unknown</td>
      <td>unknown</td>
      <td>1.8</td>
      <td>unknown</td>
      <td>yacht</td>
      <td>[https://swapi.dev/api/people/39/]</td>
      <td>[https://swapi.dev/api/films/4/]</td>
      <td>2014-12-19T17:45:03.506000Z</td>
      <td>2014-12-20T21:23:49.919000Z</td>
      <td>https://swapi.dev/api/starships/40/</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Scimitar</td>
      <td>Star Courier</td>
      <td>Republic Sienar Systems</td>
      <td>55000000</td>
      <td>26.5</td>
      <td>1180</td>
      <td>1</td>
      <td>6</td>
      <td>2500000</td>
      <td>30 days</td>
      <td>1.5</td>
      <td>unknown</td>
      <td>Space Transport</td>
      <td>[https://swapi.dev/api/people/44/]</td>
      <td>[https://swapi.dev/api/films/4/]</td>
      <td>2014-12-20T09:39:56.116000Z</td>
      <td>2014-12-20T21:23:49.922000Z</td>
      <td>https://swapi.dev/api/starships/41/</td>
    </tr>
    <tr>
      <th>21</th>
      <td>J-type diplomatic barge</td>
      <td>J-type diplomatic barge</td>
      <td>Theed Palace Space Vessel Engineering Corps, N...</td>
      <td>2000000</td>
      <td>39</td>
      <td>2000</td>
      <td>5</td>
      <td>10</td>
      <td>unknown</td>
      <td>1 year</td>
      <td>0.7</td>
      <td>unknown</td>
      <td>Diplomatic barge</td>
      <td>[]</td>
      <td>[https://swapi.dev/api/films/5/]</td>
      <td>2014-12-20T11:05:51.237000Z</td>
      <td>2014-12-20T21:23:49.925000Z</td>
      <td>https://swapi.dev/api/starships/43/</td>
    </tr>
    <tr>
      <th>22</th>
      <td>AA-9 Coruscant freighter</td>
      <td>Botajef AA-9 Freighter-Liner</td>
      <td>Botajef Shipyards</td>
      <td>unknown</td>
      <td>390</td>
      <td>unknown</td>
      <td>unknown</td>
      <td>30000</td>
      <td>unknown</td>
      <td>unknown</td>
      <td>unknown</td>
      <td>unknown</td>
      <td>freighter</td>
      <td>[]</td>
      <td>[https://swapi.dev/api/films/5/]</td>
      <td>2014-12-20T17:24:23.509000Z</td>
      <td>2014-12-20T21:23:49.928000Z</td>
      <td>https://swapi.dev/api/starships/47/</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Jedi starfighter</td>
      <td>Delta-7 Aethersprite-class interceptor</td>
      <td>Kuat Systems Engineering</td>
      <td>180000</td>
      <td>8</td>
      <td>1150</td>
      <td>1</td>
      <td>0</td>
      <td>60</td>
      <td>7 days</td>
      <td>1.0</td>
      <td>unknown</td>
      <td>Starfighter</td>
      <td>[https://swapi.dev/api/people/10/, https://swa...</td>
      <td>[https://swapi.dev/api/films/5/, https://swapi...</td>
      <td>2014-12-20T17:35:23.906000Z</td>
      <td>2014-12-20T21:23:49.930000Z</td>
      <td>https://swapi.dev/api/starships/48/</td>
    </tr>
    <tr>
      <th>24</th>
      <td>H-type Nubian yacht</td>
      <td>H-type Nubian yacht</td>
      <td>Theed Palace Space Vessel Engineering Corps</td>
      <td>unknown</td>
      <td>47.9</td>
      <td>8000</td>
      <td>4</td>
      <td>unknown</td>
      <td>unknown</td>
      <td>unknown</td>
      <td>0.9</td>
      <td>unknown</td>
      <td>yacht</td>
      <td>[https://swapi.dev/api/people/35/]</td>
      <td>[https://swapi.dev/api/films/5/]</td>
      <td>2014-12-20T17:46:46.847000Z</td>
      <td>2014-12-20T21:23:49.932000Z</td>
      <td>https://swapi.dev/api/starships/49/</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Republic Assault ship</td>
      <td>Acclamator I-class assault ship</td>
      <td>Rothana Heavy Engineering</td>
      <td>unknown</td>
      <td>752</td>
      <td>unknown</td>
      <td>700</td>
      <td>16000</td>
      <td>11250000</td>
      <td>2 years</td>
      <td>0.6</td>
      <td>unknown</td>
      <td>assault ship</td>
      <td>[]</td>
      <td>[https://swapi.dev/api/films/5/]</td>
      <td>2014-12-20T18:08:42.926000Z</td>
      <td>2014-12-20T21:23:49.935000Z</td>
      <td>https://swapi.dev/api/starships/52/</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Solar Sailer</td>
      <td>Punworcca 116-class interstellar sloop</td>
      <td>Huppla Pasa Tisc Shipwrights Collective</td>
      <td>35700</td>
      <td>15.2</td>
      <td>1600</td>
      <td>3</td>
      <td>11</td>
      <td>240</td>
      <td>7 days</td>
      <td>1.5</td>
      <td>unknown</td>
      <td>yacht</td>
      <td>[]</td>
      <td>[https://swapi.dev/api/films/5/]</td>
      <td>2014-12-20T18:37:56.969000Z</td>
      <td>2014-12-20T21:23:49.937000Z</td>
      <td>https://swapi.dev/api/starships/58/</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Trade Federation cruiser</td>
      <td>Providence-class carrier/destroyer</td>
      <td>Rendili StarDrive, Free Dac Volunteers Enginee...</td>
      <td>125000000</td>
      <td>1088</td>
      <td>1050</td>
      <td>600</td>
      <td>48247</td>
      <td>50000000</td>
      <td>4 years</td>
      <td>1.5</td>
      <td>unknown</td>
      <td>capital ship</td>
      <td>[https://swapi.dev/api/people/10/, https://swa...</td>
      <td>[https://swapi.dev/api/films/6/]</td>
      <td>2014-12-20T19:40:21.902000Z</td>
      <td>2014-12-20T21:23:49.941000Z</td>
      <td>https://swapi.dev/api/starships/59/</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Theta-class T-2c shuttle</td>
      <td>Theta-class T-2c shuttle</td>
      <td>Cygnus Spaceworks</td>
      <td>1000000</td>
      <td>18.5</td>
      <td>2000</td>
      <td>5</td>
      <td>16</td>
      <td>50000</td>
      <td>56 days</td>
      <td>1.0</td>
      <td>unknown</td>
      <td>transport</td>
      <td>[]</td>
      <td>[https://swapi.dev/api/films/6/]</td>
      <td>2014-12-20T19:48:40.409000Z</td>
      <td>2014-12-20T21:23:49.944000Z</td>
      <td>https://swapi.dev/api/starships/61/</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Republic attack cruiser</td>
      <td>Senator-class Star Destroyer</td>
      <td>Kuat Drive Yards, Allanteen Six shipyards</td>
      <td>59000000</td>
      <td>1137</td>
      <td>975</td>
      <td>7400</td>
      <td>2000</td>
      <td>20000000</td>
      <td>2 years</td>
      <td>1.0</td>
      <td>unknown</td>
      <td>star destroyer</td>
      <td>[]</td>
      <td>[https://swapi.dev/api/films/6/]</td>
      <td>2014-12-20T19:52:56.232000Z</td>
      <td>2014-12-20T21:23:49.946000Z</td>
      <td>https://swapi.dev/api/starships/63/</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Naboo star skiff</td>
      <td>J-type star skiff</td>
      <td>Theed Palace Space Vessel Engineering Corps/Nu...</td>
      <td>unknown</td>
      <td>29.2</td>
      <td>1050</td>
      <td>3</td>
      <td>3</td>
      <td>unknown</td>
      <td>unknown</td>
      <td>0.5</td>
      <td>unknown</td>
      <td>yacht</td>
      <td>[https://swapi.dev/api/people/10/, https://swa...</td>
      <td>[https://swapi.dev/api/films/6/]</td>
      <td>2014-12-20T19:55:15.396000Z</td>
      <td>2014-12-20T21:23:49.948000Z</td>
      <td>https://swapi.dev/api/starships/64/</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Jedi Interceptor</td>
      <td>Eta-2 Actis-class light interceptor</td>
      <td>Kuat Systems Engineering</td>
      <td>320000</td>
      <td>5.47</td>
      <td>1500</td>
      <td>1</td>
      <td>0</td>
      <td>60</td>
      <td>2 days</td>
      <td>1.0</td>
      <td>unknown</td>
      <td>starfighter</td>
      <td>[https://swapi.dev/api/people/10/, https://swa...</td>
      <td>[https://swapi.dev/api/films/6/]</td>
      <td>2014-12-20T19:56:57.468000Z</td>
      <td>2014-12-20T21:23:49.951000Z</td>
      <td>https://swapi.dev/api/starships/65/</td>
    </tr>
    <tr>
      <th>32</th>
      <td>arc-170</td>
      <td>Aggressive Reconnaissance-170 starfighte</td>
      <td>Incom Corporation, Subpro Corporation</td>
      <td>155000</td>
      <td>14.5</td>
      <td>1000</td>
      <td>3</td>
      <td>0</td>
      <td>110</td>
      <td>5 days</td>
      <td>1.0</td>
      <td>100</td>
      <td>starfighter</td>
      <td>[]</td>
      <td>[https://swapi.dev/api/films/6/]</td>
      <td>2014-12-20T20:03:48.603000Z</td>
      <td>2014-12-20T21:23:49.953000Z</td>
      <td>https://swapi.dev/api/starships/66/</td>
    </tr>
    <tr>
      <th>33</th>
      <td>Banking clan frigte</td>
      <td>Munificent-class star frigate</td>
      <td>Hoersch-Kessel Drive, Inc, Gwori Revolutionary...</td>
      <td>57000000</td>
      <td>825</td>
      <td>unknown</td>
      <td>200</td>
      <td>unknown</td>
      <td>40000000</td>
      <td>2 years</td>
      <td>1.0</td>
      <td>unknown</td>
      <td>cruiser</td>
      <td>[]</td>
      <td>[https://swapi.dev/api/films/6/]</td>
      <td>2014-12-20T20:07:11.538000Z</td>
      <td>2014-12-20T21:23:49.956000Z</td>
      <td>https://swapi.dev/api/starships/68/</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Belbullab-22 starfighter</td>
      <td>Belbullab-22 starfighter</td>
      <td>Feethan Ottraw Scalable Assemblies</td>
      <td>168000</td>
      <td>6.71</td>
      <td>1100</td>
      <td>1</td>
      <td>0</td>
      <td>140</td>
      <td>7 days</td>
      <td>6</td>
      <td>unknown</td>
      <td>starfighter</td>
      <td>[https://swapi.dev/api/people/10/, https://swa...</td>
      <td>[https://swapi.dev/api/films/6/]</td>
      <td>2014-12-20T20:38:05.031000Z</td>
      <td>2014-12-20T21:23:49.959000Z</td>
      <td>https://swapi.dev/api/starships/74/</td>
    </tr>
    <tr>
      <th>35</th>
      <td>V-wing</td>
      <td>Alpha-3 Nimbus-class V-wing starfighter</td>
      <td>Kuat Systems Engineering</td>
      <td>102500</td>
      <td>7.9</td>
      <td>1050</td>
      <td>1</td>
      <td>0</td>
      <td>60</td>
      <td>15 hours</td>
      <td>1.0</td>
      <td>unknown</td>
      <td>starfighter</td>
      <td>[]</td>
      <td>[https://swapi.dev/api/films/6/]</td>
      <td>2014-12-20T20:43:04.349000Z</td>
      <td>2014-12-20T21:23:49.961000Z</td>
      <td>https://swapi.dev/api/starships/75/</td>
    </tr>
  </tbody>
</table>
</div>



### Apartado C: Transformación y cruce de datos (2.5 puntos)

Ahora debes unificar la información local con la oficial y hacer los cálculos logísticos.

1.  Realiza un cruce entre tu DataFrame del inventario limpio (Apartado A) y el DataFrame del catálogo oficial (Apartado B), utilizando el nombre de la nave como clave de unión.
2.  Crea una nueva columna calculada llamada `capacidad_total_flota`. Esta debe ser el resultado de multiplicar las `naves_disponibles` (de tu inventario) por la carga especificada en la API oficial.


```python
df = df.set_index("name").join(df_catalogo.set_index("name"))

df["cargo_capacity"] = pd.to_numeric(df["cargo_capacity"])

df["capacidad_total_flota"] = df["naves_disponibles"] * df["cargo_capacity"]

df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>base_asignada</th>
      <th>naves_disponibles</th>
      <th>model</th>
      <th>manufacturer</th>
      <th>cost_in_credits</th>
      <th>length</th>
      <th>max_atmosphering_speed</th>
      <th>crew</th>
      <th>passengers</th>
      <th>cargo_capacity</th>
      <th>consumables</th>
      <th>hyperdrive_rating</th>
      <th>MGLT</th>
      <th>starship_class</th>
      <th>pilots</th>
      <th>films</th>
      <th>created</th>
      <th>edited</th>
      <th>url</th>
      <th>capacidad_total_flota</th>
    </tr>
    <tr>
      <th>name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>CR90 corvette</th>
      <td>Base Yavin 4</td>
      <td>15.0</td>
      <td>CR90 corvette</td>
      <td>Corellian Engineering Corporation</td>
      <td>3500000</td>
      <td>150</td>
      <td>950</td>
      <td>30-165</td>
      <td>600</td>
      <td>3000000</td>
      <td>1 year</td>
      <td>2.0</td>
      <td>60</td>
      <td>corvette</td>
      <td>[]</td>
      <td>[https://swapi.dev/api/films/1/, https://swapi...</td>
      <td>2014-12-10T14:20:33.369000Z</td>
      <td>2014-12-20T21:23:49.867000Z</td>
      <td>https://swapi.dev/api/starships/2/</td>
      <td>45000000.0</td>
    </tr>
    <tr>
      <th>X-wing</th>
      <td>Base Echo (Hoth)</td>
      <td>120.0</td>
      <td>T-65 X-wing</td>
      <td>Incom Corporation</td>
      <td>149999</td>
      <td>12.5</td>
      <td>1050</td>
      <td>1</td>
      <td>0</td>
      <td>110</td>
      <td>1 week</td>
      <td>1.0</td>
      <td>100</td>
      <td>Starfighter</td>
      <td>[https://swapi.dev/api/people/1/, https://swap...</td>
      <td>[https://swapi.dev/api/films/1/, https://swapi...</td>
      <td>2014-12-12T11:19:05.340000Z</td>
      <td>2014-12-20T21:23:49.886000Z</td>
      <td>https://swapi.dev/api/starships/12/</td>
      <td>13200.0</td>
    </tr>
    <tr>
      <th>Millennium Falcon</th>
      <td>Flota Nómada</td>
      <td>1.0</td>
      <td>YT-1300 light freighter</td>
      <td>Corellian Engineering Corporation</td>
      <td>100000</td>
      <td>34.37</td>
      <td>1050</td>
      <td>4</td>
      <td>6</td>
      <td>100000</td>
      <td>2 months</td>
      <td>0.5</td>
      <td>75</td>
      <td>Light freighter</td>
      <td>[https://swapi.dev/api/people/13/, https://swa...</td>
      <td>[https://swapi.dev/api/films/1/, https://swapi...</td>
      <td>2014-12-10T16:59:45.094000Z</td>
      <td>2014-12-20T21:23:49.880000Z</td>
      <td>https://swapi.dev/api/starships/10/</td>
      <td>100000.0</td>
    </tr>
    <tr>
      <th>B-wing</th>
      <td>Astillero Sullust</td>
      <td>30.0</td>
      <td>A/SF-01 B-wing starfighter</td>
      <td>Slayn &amp; Korpil</td>
      <td>220000</td>
      <td>16.9</td>
      <td>950</td>
      <td>1</td>
      <td>0</td>
      <td>45</td>
      <td>1 week</td>
      <td>2.0</td>
      <td>91</td>
      <td>Assault Starfighter</td>
      <td>[]</td>
      <td>[https://swapi.dev/api/films/3/]</td>
      <td>2014-12-18T11:18:04.763000Z</td>
      <td>2014-12-20T21:23:49.909000Z</td>
      <td>https://swapi.dev/api/starships/29/</td>
      <td>1350.0</td>
    </tr>
    <tr>
      <th>EF76 Nebulon-B escort frigate</th>
      <td>Flota Nómada</td>
      <td>4.0</td>
      <td>EF76 Nebulon-B escort frigate</td>
      <td>Kuat Drive Yards</td>
      <td>8500000</td>
      <td>300</td>
      <td>800</td>
      <td>854</td>
      <td>75</td>
      <td>6000000</td>
      <td>2 years</td>
      <td>2.0</td>
      <td>40</td>
      <td>Escort ship</td>
      <td>[]</td>
      <td>[https://swapi.dev/api/films/2/, https://swapi...</td>
      <td>2014-12-15T13:06:30.813000Z</td>
      <td>2014-12-20T21:23:49.902000Z</td>
      <td>https://swapi.dev/api/starships/23/</td>
      <td>24000000.0</td>
    </tr>
    <tr>
      <th>Star Destroyer</th>
      <td>Hangar Secreto (Capturado)</td>
      <td>2.0</td>
      <td>Imperial I-class Star Destroyer</td>
      <td>Kuat Drive Yards</td>
      <td>150000000</td>
      <td>1,600</td>
      <td>975</td>
      <td>47,060</td>
      <td>n/a</td>
      <td>36000000</td>
      <td>2 years</td>
      <td>2.0</td>
      <td>60</td>
      <td>Star Destroyer</td>
      <td>[]</td>
      <td>[https://swapi.dev/api/films/1/, https://swapi...</td>
      <td>2014-12-10T15:08:19.848000Z</td>
      <td>2014-12-20T21:23:49.870000Z</td>
      <td>https://swapi.dev/api/starships/3/</td>
      <td>72000000.0</td>
    </tr>
  </tbody>
</table>
</div>



### Apartado D: Almacenamiento y salida (2.5 puntos)

El sistema de Inteligencia de Negocio y el Data Lake requieren que exportes los resultados en dos formatos distintos.

1.  **Capa de consumo (analistas):** exporta el DataFrame final resultante del Apartado C a un archivo CSV llamado `reporte_logistico.csv`. Debes asegurarte de utilizar coma (`,`) como separador y excluir explícitamente el índice numérico de Pandas.
2.  **Capa Plata (Data Lake):** para almacenar el histórico de forma eficiente para la CPU y en almacenamiento en frío, exporta el mismo DataFrame a formato **Apache Parquet**. Llama al archivo `historico_flota.parquet` y aplica compresión `gzip`.


```python
df.to_csv("reporte_logistico.csv",sep=",")
df.to_parquet("historico_flota.parquet",compression="gzip")
```
