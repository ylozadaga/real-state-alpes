# real-state-alpes

### Ejecutar Aplicación

Desde el directorio principal ejecute el siguiente comando.

```bash
flask --app src/company_data_collector/api run
```

Siempre puede ejecutarlo en modo DEBUG:

```bash
flask --app src/company_data_collector/api --debug run
```


### Crear imagen Docker

Desde el directorio principal ejecute el siguiente comando.

```bash
docker build . -f rs-alpes.Dockerfile -t rs-alpes/flask
```

### Ejecutar contenedora (sin compose)

Desde el directorio principal ejecute el siguiente comando.

```bash
docker run -p 5000:5000 rs-alpes/flask
```

## Microservicio Notificaciones
### Ejecutar Aplicación

Desde el directorio principal ejecute el siguiente comando.

```bash
python src/notificator/main.py
```

### Crear imagen Docker

Desde el directorio principal ejecute el siguiente comando.

```bash
docker build . -f notificator.Dockerfile -t rs-alpes/notificator
```

### Ejecutar contenedora (sin compose)

Desde el directorio principal ejecute el siguiente comando.

```bash
docker run rs-alpe/notificator
```

## Docker-compose

Para desplegar toda la arquitectura en un solo comando, usamos `docker-compose`. Para ello, desde el directorio principal, ejecute el siguiente comando:

```bash
docker-compose up
```

Si desea detener el ambiente ejecute:

```bash
docker-compose stop
```


## Desplegar Solo Apache Pulsar

Para desplegar solo los servicios de Apache Pulsar, usamos:

```bash
docker-compose --profile pulsar up
```

## Desplegar Solo el Microservicio de recolección de datos

Para desplegar solo el microservicio de recoleccion de datos, usamos:

```bash
docker-compose --profile rs-alpes up
```

## Desplegar Solo el Microservicio de notificaciones

Para desplegar solo el microservicio de notificaciones, usamos:

```bash
docker-compose --profile notificator up
```