from django.core.management.base import BaseCommand, CommandError

from cinema.usecases.reservas import reservar_sala


class Command(BaseCommand):
    help = 'Cadastra nova reserva de sala'

    def add_arguments(self, parser):
        parser.add_argument('id_sala', type=int)

    def handle(self, *args, **options):
        id_sala = options['id_sala']
        try:
            reservar_sala(id_sala)
            self.stdout.write(self.style.SUCCESS(f'Sala {id_sala} reservada.'))
        except PermissionError as e:
            raise CommandError(f'Reserva não concluída para sala {id_sala}') from e
