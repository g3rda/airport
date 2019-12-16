from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.timezone import datetime


class bareTicketPrice(models.Model):
	FlyingTo = (
        ("Lviv", "Lviv"),
        ("Ternopil", "Ternopil"),
        ("Odesa", "Odesa"),
        ("Kharkiv", "Kharkiv"),
        ("Ivano-Frankivsk", "Ivano-Frankivsk"),
        )
	flightTo = models.CharField(choices = FlyingTo, max_length=50)
	priceOfFlight = models.FloatField(default=100)

class Food(models.Model):

    Food_choices =(
    ("SN", "a cocktail snack"),
    ("AP", "appetizer"),
    ("SP", "soup"),
    ("SL", "salad"),
    ("EN", "entree(chicken, beef, fish, or pasta"),
    ("CH", "cheeses with fruits"),
    ("IC", "ice cream"),
    ("NO", "no food"),
    )
    food_choices=models.CharField(choices = Food_choices, max_length = 50)
    priceOfFood = models.FloatField(default=100)

class Luggage(models.Model):
	Luggage_choices =(
		("CB", "checked baggage"),
		("CO", "carry-on"),
		("NL", "no baggage")
		)
	luggage_choices=models.CharField(choices = Luggage_choices, max_length=50)
	priceOfLuggage = models.FloatField(default=100)


# Create your models here.
class Ticket(models.Model):

	food_choices =(
		("SN", "a cocktail snack"),
		("AP", "appetizer"),
		("SP", "soup"),
		("SL", "salad"),
		("EN", "entree(chicken, beef, fish, or pasta"),
		("CH", "cheeses with fruits"),
		("IC", "ice cream"),
		("NO", "no food"),
		)
	luggage_choices = (
		("CB", "checked baggage"),
		("CO", "carry-on"),
		("NL", "no baggage")
		)
	class_choices = (
		("economy class", "economy class"),
		("business class", "business class"),
		("first class", "first class")
		)

	ticket_id = models.AutoField(primary_key=True)
	passenger = models.CharField(max_length=50)
	flightID = models.ForeignKey('airoportinfo.Flight', related_name = '%(class)s_flight_id', on_delete=models.CASCADE, default = 0)
	travelClass = models.CharField(max_length=20, choices = class_choices)
	createdDate = models.DateTimeField(default = timezone.now)
	buyPrLine = models.BooleanField(blank=False)
	buyVIP = models.BooleanField(blank=False)
	buyFood = models.CharField(max_length=100, choices = food_choices, default="NO" )
	buyWaitRoom = models.BooleanField(blank=False)
	buyAddLuggage=models.CharField(max_length=50, choices = luggage_choices, default="CO")
	buyer = models.ForeignKey(User, on_delete=models.CASCADE)
	price = models.FloatField(default=100)
	def calculatePrice(self):
		destin = self.flightID.destination;
		food=self.buyFood;
		luggage=self.buyAddLuggage;
		multipl=1;
		if self.travelClass == "economy class":
			multipl=1
		elif self.travelClass == "business class":
			multipl = 1.5
		else:
			multipl = 2
		barePrice = bareTicketPrice.objects.all().filter(flightTo=destin)[0].priceOfFlight
		addPrice = Food.objects.all().filter(food_choices=food)[0].priceOfFood
		addPrL = Luggage.objects.all().filter(luggage_choices=luggage)[0].priceOfLuggage
		price = multipl*barePrice+ int(self.buyPrLine)*5 + int(self.buyWaitRoom)*13 + int(self.buyVIP)*20+addPrL+addPrice
		return price
	
    





