# real-state-alpes

### Run Company Data Auditor
To run the auditor, check the auditor's **[README.md](./src/company_data_auditor/README.md)** file.

### Run Company Data Collector
To run the collector, check the auditor's **[README.md](./src/company_data_collector/README.md)** file.

### Run Company Data Presenter
To run the presenter, check the auditor's **[README.md](./src/company_data_presenter/README.md)** file.

### Run Company Data Processor
To run the processor, check the auditor's **[README.md](./src/company_data_processor/README.md)** file.


### Run Complete Architecture with docker-compose
Para desplegar toda la arquitectura en un solo comando, usamos `docker-compose`. Para ello, desde el directorio principal, ejecute el siguiente comando:

```bash
docker-compose up
```

### Stop Complete Architecture with docker-compose
To stop the complete architecture, execute the following command from the root directory:

```bash
docker-compose stop
```

### Deploy Only Apache Pulsar
To deploy only Apache Pulsar, execute the following command from the root directory:

```bash
docker-compose --profile pulsar up
```
