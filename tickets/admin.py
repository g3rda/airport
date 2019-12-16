from django.contrib import admin
from django.http import HttpResponse
import decimal, csv
from .models import Ticket, bareTicketPrice, Food, Luggage


admin.site.site_header="ErvineAirport"
admin.site.site_title="ErvineAirport"
admin.site.index_title="Site administration"



def export_tickets(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="books.csv"'
    writer = csv.writer(response)
    writer.writerow(['Ticket ID', 'Fligth ID', 'Buyer', 'Passenger', 'Travel Class', 'Date of booking', 'Price'])
    books = queryset.values_list('ticket_id', 'flightID', 'buyer', 'passenger', 'travelClass', 'createdDate', 'price')
    for book in books:
        writer.writerow(book)
    return response
export_tickets.short_description = 'Export to csv'

class TicketAdmin(admin.ModelAdmin):
	list_filter = ['createdDate', 'buyer']
	list_editable = ['passenger']
	search_fields = ['ticket_id', 'buyer__username', 'passenger']
	actions = [export_tickets,]
	date_hierarchy = 'createdDate'
	list_display = ('ticket_id', 'flight_ID', 'buyer', 'passenger', 'travelClass', 'createdDate', 'price')
	def flight_ID(self, obj):
		return obj.flightID.flight_id

class bareTicketPriceAdmin(admin.ModelAdmin):
	search_fields = ['flightTo', 'priceOfFlight']
	list_display = ('flightTo', 'priceOfFlight')


class FoodAdmin(admin.ModelAdmin):
	search_fields = ['food_choices', 'priceOfFood']
	list_display = ('food_choices', 'priceOfFood')


class LuggageAdmin(admin.ModelAdmin):
	search_fields = ['luggage_choices', 'priceOfLuggage']
	list_display = ('luggage_choices', 'priceOfLuggage')



admin.site.register(Ticket, TicketAdmin)
admin.site.register(bareTicketPrice, bareTicketPriceAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Luggage, LuggageAdmin)


