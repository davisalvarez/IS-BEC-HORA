from django.conf.urls import url
from django.contrib import admin

from core.views import *

import core


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
]