from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url('^polls/', include('polls.urls')),
    url('^admin/', admin.site.urls),
]