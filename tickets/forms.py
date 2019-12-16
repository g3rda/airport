from django.forms import ModelForm
from django import forms
from .models import Ticket

class TicketForm(ModelForm):
	class Meta:
		model = Ticket
		widgets = {
            'travelClass': forms.Select(attrs={'class' : 'form-control'}),
            'buyAddLuggage' :forms.Select(attrs={'class' : 'form-control'}),
            'buyFood' :forms.Select(attrs={'class' : 'form-control'}),
            'passenger' :forms.TextInput(attrs={'class' : 'form-control'}),

        }
		fields = ['passenger', 'buyPrLine', 'buyVIP', 'buyWaitRoom', 'buyAddLuggage', 'buyFood', 'travelClass']

class SearchForm(forms.Form):
	FlyingFrom = (
        ("Kyiv", "Kyiv"),
        )
	flying_From = forms.ChoiceField(choices=FlyingFrom, widget=forms.Select(attrs={'class' : 'form-control'}))
	FlyingTo = (
        ("Lviv", "Lviv"),
        ("Ternopil", "Ternopil"),
        ("Odesa", "Odesa"),
        ("Kharkiv", "Kharkiv"),
        ("Ivano-Frankivsk", "Ivano-Frankivsk"),
        )
	flying_To = forms.ChoiceField(choices=FlyingTo, widget=forms.Select(attrs={'class' : 'form-control'}))
	departing = forms.DateField(widget=forms.DateInput(attrs={'class' : 'form-control'}))
	TravelClass = (
		("EC", "economy class"),
		("BC", "business class"),
		("FC", "first class")
		)
	travel_Class = forms.ChoiceField(choices=TravelClass, widget=forms.Select(attrs={'class' : 'form-control'}))



