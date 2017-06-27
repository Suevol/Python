from django.conf.urls import url
from django.contrib import admin
from main_app.views import contacts
from main_app.views import goods
from main_app.views import main

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main, name = 'main'),
    url(r'^contacts/$', contacts, name = 'contacts'),
    url(r'^goods/$', goods, name = 'goods'),
]
