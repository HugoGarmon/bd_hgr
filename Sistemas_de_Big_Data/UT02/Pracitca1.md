# Trabajo con redis CLI

## 1
SET usuario:nombre "Hugo"

## 2 
SET usuario:apellido "Garmon"

## 3 
GET usuario:nombre
GET usuario:apellido

## 4 
SET usuario:email "emailfalso123@falso.es"
GET usuario:email

## 5
SET usuario:nombre "HUGO"

## 6
SET contador:visitas 0

## 7
INCR contador:visitas
INCR contador:visitas
INCR contador:visitas

## 8
DECR contador:visitas

## 9
SET mensaje "Bienvenido a Redis"

## 10
EXPIRE mensaje 60

## 11
DEL usuario:apellido

## 12
DEL usuario:nombre usuario:email contador:visitas mensaje

# Trabajo con python


```python
import redis
import time

r = redis.Redis(
    host='redis',
    port=6379,
    db=0,
    decode_responses=True
)
r.ping()
```




    True




```python
# 1. Inserta la clave app:version con el valor "1.0".
r.set("app:version", "1.0")
```




    True




```python
 # 2. Recupera y muestra el valor de app:version.
version = r.get("app:version")
print(version)

```

    1.0



```python
# 3. Modifica el valor de app:version a "1.1".
r.set("app:version", "1.1")
version_actualizada = r.get("app:version")
print(version_actualizada)
```

    1.1



```python
# 4. Crea la clave contador:descargas con valor 0.
r.set("contador:descargas", 0)
```




    True




```python
# 5. Incrementa en 5 el valor de contador:descargas. (Usamos INCRBY)
r.incrby("contador:descargas", 5)
descargas_incrementadas = r.get("contador:descargas")
print(descargas_incrementadas)
```

    5



```python
# 6. Decrementa en 2 el valor de contador:descargas. (Usamos DECRBY)
r.decrby("contador:descargas", 2)
descargas_finales = r.get("contador:descargas")
print(descargas_finales)
```

    3



```python
# 7. Inserta la clave app:estado con el valor "activo".
r.set("app:estado", "activo")
```




    True




```python
# 8. Cambia el valor de app:estado a "mantenimiento".
r.set("app:estado", "mantenimiento")
estado_actual = r.get("app:estado")
print(estado_actual)
```

    mantenimiento



```python
# 9. Inserta la clave mensaje:bienvenida.
r.set("mensaje:bienvenida", "Hola alumno")
```




    True




```python
# 10. Establece un tiempo de expiración de 30 segundos para la clave app:estado.
r.expire("app:estado", 30)
ttl_inicial = r.ttl("app:estado")
print(ttl_inicial)
```

    30



```python
 # 11. Verifica si la clave app:estado todavía existe después de unos segundos.
time.sleep(5)
    
existe_estado = r.exists("app:estado")
ttl_despues = r.ttl("app:estado")

print(f"'app:estado' después de 5s? {bool(existe_estado)}")
print(f"TTL restante: {ttl_despues}")
```

    'app:estado' después de 5s? True
    TTL restante: 25



```python
# 12. Elimina la clave app:version y muestra un mensaje confirmando su eliminación.
num_eliminadas = r.delete("app:version")
if num_eliminadas > 0:
    print(" Clave 'app:version' eliminada con éxito.")
else:
    print("Clave 'app:version' no existía para ser eliminada.")
```

     Clave 'app:version' eliminada con éxito.

