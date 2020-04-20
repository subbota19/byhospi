from django.contrib import admin
from django.urls import path, include
from map import urls as map_urls
from hospital import urls as hospital_urls
from registration import urls as registration_urls
from registration.views import return_redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', return_redirect),
    path('', include(map_urls)),
    path('hospital/', include(hospital_urls)),
    path('registration/', include(registration_urls))
]
