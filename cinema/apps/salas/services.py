

def cadastrar_sala():
    ...


def verificar_disponibilidade(id_sala):
    if id_sala % 2 == 0:
        return "DISPONIVEL"
    return "INDISPONÍVEL"


def gravar_reserva(id_sala):
    print(f"Reserva da sala {id_sala} registrada")


def reservar_sala(id_sala):
    if verificar_disponibilidade(id_sala) == "DISPONIVEL":
        gravar_reserva(id_sala)
        return "RESERVADA"
    raise PermissionError("Sala indisponível")


def listar_reservas(id_sala):
    return [
        "2020-10-01",
        "2020-10-03",
        "2020-10-04",
        "2020-10-06",
        "2020-10-07",
    ]


def inativar_sala():
    ...


def listar_salas():
    ...
