import pulsar
from pulsar.schema import *

from company_data_auditor.seedwork.infraestructura import utils

class Despachador:
    def __init__(self):
        ...

    def publicar_mensaje(self, mensaje, topico):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(mensaje.__class__))
        publicador.send(mensaje)
        print(f'mensaje publicado: {mensaje} {topico}')
        cliente.close()
