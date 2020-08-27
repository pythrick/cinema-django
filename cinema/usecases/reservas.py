from cinema.apps.salas import services as _sala_services
from cinema.apps.notificacoes import services as _notificacoes_services


def _notificar_gerencia(titulo, msg=None):
    numero = "41999999999"
    email = "gerencia@email.com"
    _notificacoes_services.enviar_whatsapp(numero, msg)
    _notificacoes_services.enviar_email([email], titulo, msg)


def reservar_sala(id_sala):
    try:
        _sala_services.reservar_sala(id_sala)
        _notificar_gerencia(f"A sala {id_sala} acaba de ser reservada.")
    except PermissionError as e:
        raise e


def listar_reservas(id_sala):
    return _sala_services.listar_reservas(id_sala)
