# company_data_collector


### Execute Server

To run flask server, execute the following command from the root directory:

```bash
flask --app src/company_data_collector/api run
```

To run flask server on debug mode, execute the following command from the root directory:

```bash
flask --app src/company_data_collector/api --debug run
```


### Create Docker Image

To create the docker image, execute the following command from the root directory:

```bash
docker build . -f company_data_collector.Dockerfile -t rs-alpes/company_data_collector
```


### Execute Container (without docker-compose)

To run the container, execute the following command from the root directory:

```bash
docker run -p 5000:5000 rs-alpes/company_data_collector
```


### Deploy microservice with docker-compose

To run the microservice with docker-compose, execute the following command from the root directory:

```bash
docker-compose --profile company-data-collector up
```


### Stop microservice with docker-compose

To stop the microservice with docker-compose, execute the following command from the root directory:

```bash
docker-compose stop
```
