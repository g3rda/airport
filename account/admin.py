from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.http import HttpResponse
import decimal, csv


def export_users(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'
    writer = csv.writer(response)
    writer.writerow(['Username', 'Email', 'First name', 'Last name', 'Is active?', 'Date joined', 'Is staff?'])
    users = queryset.values_list('username', 'email', 'first_name', 'last_name', 'is_active', 'date_joined', 'is_staff')
    for user in users:
        writer.writerow(user)
    return response

export_users.short_description = 'Export to csv'


UserAdmin.list_display = ('username', 'email', 'is_active', 'date_joined', 'is_staff')
UserAdmin.list_filter = ['is_active', 'is_staff']
UserAdmin.search_fields = ['first_name', 'last_name', 'username', 'email']
UserAdmin.date_hierarchy = 'date_joined'
UserAdmin.actions = [export_users,]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


