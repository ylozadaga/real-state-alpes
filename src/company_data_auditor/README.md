# company_data_auditor


### Execute Server

To run flask server, execute the following command from the root directory:

```bash
flask --app src/company_data_auditor/api run
```

To run flask server on debug mode, execute the following command from the root directory:

```bash
flask --app src/company_data_auditor/api --debug run
```


### Create Docker Image

To create the docker image, execute the following command from the root directory:

```bash
docker build . -f company_data_auditor.Dockerfile -t rs-alpes/company_data_auditor
```


### Execute Container (without docker-compose)

To run the container, execute the following command from the root directory:

```bash
docker run -p 5000:5000 rs-alpes/company_data_auditor
```


### Deploy microservice with docker-compose

To run the microservice with docker-compose, execute the following command from the root directory:

```bash
docker-compose --profile company-data-auditor up
```


### Stop microservice with docker-compose

To stop the microservice with docker-compose, execute the following command from the root directory:

```bash
docker-compose stop
```
