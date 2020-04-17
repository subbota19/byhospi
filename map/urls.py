from django.urls import path
from map import views

urlpatterns = [
    path('map', views.MapView.as_view(), name='map'),
    path('region/<slug:region>/<int:page>', views.RegionView.as_view(), name='region')

]
