from airoportinfo.models import Flight
from tickets.models import Ticket
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Seeds the database.'

    def add_arguments(self, parser):
        parser.add_argument('--users',
            default=5,
            type=int,
            help='The number of fake users to create.')

    def handle(self, *args, **options):
        destin=["Lviv", "Odesa", "Kharkiv", "Ternopil", "Ivano-Frankivsk"]
        flight=Flight.objects.get(flight_id=55)
        depMinutes = 5
        g=1
        for _ in range(options['users']):
            for d in destin:
                p = Flight(departureDate='2019-12-16', depatureTime='13:' + str(depMinutes%60), departureFrom='Kyiv', destination=d,gate=g%5+1, arrivalDate='2019-12-19', arrivalTime='13:00')
                p.save()
                depMinutes = depMinutes + 12 +g%8
                g = g+1


