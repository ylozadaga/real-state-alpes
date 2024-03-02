from company_data_auditor.seedwork.aplicacion.comandos import Comando, ComandoHandler

@dataclass
class ComandoAutenticarUsuario(Comando):
    email: str
    password: str

class AutenticarUsuarioHandler(ComandoHandler):
    ...