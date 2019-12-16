from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Flight(models.Model):
	FlyingFrom = (
        ("KY", "Kyiv"),
        )
	FlyingTo = (
        ("Lviv", "Lviv"),
        ("Ternopil", "Ternopil"),
        ("Odesa", "Odesa"),
        ("Kharkiv", "Kharkiv"),
        ("Ivano-Frankivsk", "Ivano-Frankivsk"),
        )
	flight_id = models.AutoField(primary_key = True)
	departureDate = models.DateField()
	depatureTime = models.TimeField()
	departureFrom = models.CharField(max_length =100, choices = FlyingFrom)
	destination = models.CharField(max_length = 100, choices = FlyingTo)
	arrivalDate = models.DateField()
	arrivalTime = models.TimeField()
	gate = models.IntegerField()
	def statusNow(self):
		depart=datetime.datetime.combine( timezone.now().date(), self.depatureTime)
		now = datetime.datetime.now()
		timediff = depart - now
		differ = timediff.total_seconds()
		if differ<=900:
			return "Arrived"
		elif differ<1200 and differ>900:
			return "Arriving"
		else:
			return "Not arrived"




class News(models.Model):

	title = models.CharField(max_length = 200)
	text = models.TextField()
	published_date = models.DateTimeField(blank = True, null = True)
	newsImage = models.ImageField(upload_to="gallery")


	def published(self):
	 	self.published_date = timezone.now()
	 	self.save()


class Vacancies(models.Model):

	title = models.CharField(max_length = 100)
	text = models.TextField()
	published_date = models.DateTimeField(blank = True, null = True)

    
	def published(self):
	 	self.published_date = timezone.now()
	 	self.save()
