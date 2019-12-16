from django.contrib import admin
from django.http import HttpResponse
import decimal, csv
from .models import Flight, News, Vacancies


def export_flights(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="flights.csv"'
    writer = csv.writer(response)
    writer.writerow(['Fligth ID', 'Departure Date', 'Departure Time', 'Departure From', 'Destination', 'Arrival Date', 'Arrival Time', 'Gate'])
    flights = queryset.values_list('flight_id', 'departureDate', 'depatureTime', 'departureFrom', 'destination', 'arrivalDate', 'arrivalTime', 'gate')
    for flight in flights:
        writer.writerow(flight)
    return response
export_flights.short_description = 'Export to csv'

class FlightAdmin(admin.ModelAdmin):
	list_filter = ['departureDate', 'destination']
	list_editable = ['gate']
	search_fields = ['destination', 'departureDate', 'depatureTime']
	actions = [export_flights,]
	list_display = ('flight_id', 'departureDate', 'depatureTime', 'destination', 'gate')


class NewsAdmin(admin.ModelAdmin):
	search_fields = ['title', 'text']
	list_display = ('title', 'text')

class VacanciesAdmin(admin.ModelAdmin):
	search_fields = ['title', 'text']
	list_display = ('title', 'text')




admin.site.register(Flight, FlightAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Vacancies, VacanciesAdmin)

