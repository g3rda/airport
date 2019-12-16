from django.shortcuts import render, render_to_response
from .models import Flight, News, Vacancies
from django.utils import timezone
from django.template import Context, loader, RequestContext




def contacts(request):
    return render(request, 'contacts.html')

def home(request):
    news=News.objects.all().order_by('id')[:5]
    flights = Flight.objects.all().filter(departureDate=timezone.now().today()).order_by('depatureTime').filter(depatureTime__gte=timezone.now())[:7]
    context = {"flights" : flights,
    "news" : news}
    return render(request, "home.html", context)

def vacancies(request):
    vacancies = Vacancies.objects.all()
    data = {"vacancies" : vacancies}
    resp =  render(request, "vacancies.html", data)
    return resp

def news(request, newsid):
    news1 = News.objects.all().filter(id=newsid)[0]
    return render(request, 'news.html', {'news': news1})


def aboutus(request):
    return render(request, 'aboutUs.html')
