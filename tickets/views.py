from django.shortcuts import render, redirect
from .forms import TicketForm, SearchForm
from .models import Ticket
from airoportinfo.models import Flight
from django.utils import timezone


def buyticket(request, searchflightid):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticketbought = form.save(commit=False)
            ticketbought.flightID = Flight.objects.get(flight_id=searchflightid)
            ticketbought.buyer = request.user;
            ticketbought.price = ticketbought.calculatePrice()
            ticketbought.save()
            data = {"price":ticketbought.price}
            return render(request, "confirmation.html", data)
    else:
        form = TicketForm()
    return render(request, 'buyticket.html', {'form': form,
        "flight": Flight.objects.get(flight_id=searchflightid)})



def searchTickets(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            searchDestin = form.cleaned_data['flying_To']
            searchData = form.cleaned_data['departing']
            flights = Flight.objects.all().filter(destination=searchDestin).filter(departureDate=searchData).order_by('depatureTime')
            data={"flights": flights}
            return render(request, "showavailable.html", data)
    else:
        form = SearchForm()

    return render(request, 'searchticket/index.html', {'form': form})



def history(request):
	tickets = Ticket.objects.all().filter(buyer=request.user).order_by('flightID__departureDate')
	data = { "tickets" : tickets}
	return render(request,"showhistory.html", data)
	


def validtickets(request):
    tickets = Ticket.objects.all().filter(buyer=request.user).order_by('flightID__departureDate').filter(flightID__departureDate__gte=timezone.now().today())
    data = { "tickets" : tickets}
    return render(request,"validtickets.html", data)
    




def showTicket(request, TicketId):
    ticket = Ticket.objects.all().filter(ticket_id=TicketId)[0]
    return render(request, 'ticket.html', {'ticket': ticket})
