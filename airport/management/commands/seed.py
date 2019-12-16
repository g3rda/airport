from airoportinfo.models import Flight
from tickets.models import Ticket
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Seeds the database.'

    def add_arguments(self, parser):
        parser.add_argument('--users',
            default=10,
            type=int,
            help='The number of fake users to create.')

    def handle(self, *args, **options):
    	user=User.objects.get(id=8)
    	flight=Flight.objects.get(flight_id=3)
    	for _ in range(options['users']):
    		unique_id = get_random_string(length=10)
    		p = Ticket(buyer=user, passenger = unique_id, flightID=flight, travelClass='EC', buyPrLine=True, buyVIP = False, buyFood = 'EN', buyWaitRoom = False)
    		p.save()
