# company_data_processor


### Execute Server

To run flask server, execute the following command from the root directory:

```bash
flask --app src/company_data_processor/api run
```

To run flask server on debug mode, execute the following command from the root directory:

```bash
flask --app src/company_data_processor/api --debug run
```


### Create Docker Image

To create the docker image, execute the following command from the root directory:

```bash
docker build . -f company_data_processor.Dockerfile -t rs-alpes/company_data_processor
```


### Execute Container (without docker-compose)

To run the container, execute the following command from the root directory:

```bash
docker run -p 5000:5000 rs-alpes/company_data_processor
```


### Deploy microservice with docker-compose

To run the microservice with docker-compose, execute the following command from the root directory:

```bash
docker-compose --profile company-data-processor up
```


### Stop microservice with docker-compose

To stop the microservice with docker-compose, execute the following command from the root directory:

```bash
docker-compose stop
```
