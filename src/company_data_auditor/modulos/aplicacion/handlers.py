from company_data_auditor.modulos.dominio.eventos.reservas import ReservaCreada
from company_data_auditor.seedwork.aplicacion.handlers import Handler

class HandlerReservaDominio(Handler):

    @staticmethod
    def handle_reserva_creada(evento):
        print('================ RESERVA CREADA ===========')
