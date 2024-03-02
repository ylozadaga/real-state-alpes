# notificator


### Execute Server

To run flask server, execute the following command from the root directory:

```bash
python src/notificator/main.py
```


### Create Docker Image

To create the docker image, execute the following command from the root directory:

```bash
docker build . -f notificator.Dockerfile -t rs-alpes/notificator
```


### Execute Container (without docker-compose)

To run the container, execute the following command from the root directory:

```bash
docker run rs-alpe/notificator
```

    
### Deploy microservice with docker-compose

To run the microservice with docker-compose, execute the following command from the root directory:

```bash
docker-compose --profile notificator up
```


### Stop microservice with docker-compose

To stop the microservice with docker-compose, execute the following command from the root directory:

```bash
docker-compose stop
```
