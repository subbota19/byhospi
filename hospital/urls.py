from django.urls import path

from hospital import views

urlpatterns = [path("<int:id>", views.HospitalView.as_view(), name="hospital")]
