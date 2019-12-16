"""airport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from account import views as va
from tickets import views as vt
from airoportinfo import views as vi
from django.views.generic.base import TemplateView
from django.conf.urls import url




urlpatterns = [
    url(r'^signup/$', va.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', va.activate, name='activate'),
    path('admin/', admin.site.urls),
    path("signup/", va.signup, name="signup"), 
    path('account/', include('django.contrib.auth.urls')),
    path('', vi.home, name='home'),
    path("profile/", va.profile, name="profile"), 
    path("search/", vt.searchTickets, name="search"), 
    path("search/<int:searchflightid>/", vt.buyticket, name="buyticket"), 
    path("contacts/", vi.contacts, name ="contacts"),
    path("showhistory/", vt.history, name ="showhistory"),
    path("validtickets/", vt.validtickets, name="validtickets"),
    path("vacancies/", vi.vacancies, name="vacancies"),
    path("news/<int:newsid>/", vi.news, name="news"),
    path("aboutus/", vi.aboutus, name = "aboutus"),
    path("ticket/<int:TicketId>/", vt.showTicket, name='showTicket')

]


from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 
 
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)