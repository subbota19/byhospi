from django.shortcuts import render, redirect
from django.views import View
from service import hospital


class HospitalView(View):
    def get(self, request, id, *args, **kwargs):
        response = hospital.get_info_about_hospital(id)
        if response['error']:
            return redirect('map')
        return render(request, 'hospital/hospital.html', response)
