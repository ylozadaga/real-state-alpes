# real-state-alpes

### Run Complete Architecture with docker-compose
Para desplegar toda la arquitectura en un solo comando, usamos docker-compose. Para ello, desde el directorio principal, ejecute el siguiente comando:

```bash
docker-compose --profile pulsar up -d 
```
y luego 

```bash
docker-compose --profile rs-alpes up -d 
```

### Stop Complete Architecture with docker-compose
To stop the complete architecture, execute the following command from the root directory:

```bash
 docker-compose --profile rs-alpes down
```
