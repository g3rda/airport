from django.test import TestCase
from airoportinfo.models import Flight
from tickets.models import Ticket
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

class Ticket(TestCase):
    def entries(self):
    	user=User.objects.get(id=8)
    	flight=Flight.objects.get(flight_id=3)
    	
    	for i in range(1,10):
    		unique_id = get_random_string(length=10)
    		p = Ticket(buyer=user, passenger = unique_id, flightID=flight, travelClass='EC', buyPrLine=True, buyVIP = False, buyFood = 'EN', buyWaitRoom = False)
    		p.save()


    