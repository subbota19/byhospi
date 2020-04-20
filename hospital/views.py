from django.shortcuts import render, redirect
from django.views import View
from service import hospital


class HospitalView(View):
    def post(self, request, id, *args, **kwargs):
        response = None
        if 'description' in request.POST:
            response = hospital.edit_description_form(id, message=request.POST['description'])
        if 'comment' in request.POST:
            try:
                response = hospital.create_comment(id, request.COOKIES['username'], comment=request.POST['comment'])
            except KeyError:
                redirect('sign')
        if response['error']:
            return redirect('map')
        return render(request, 'hospital/hospital.html')

    def get(self, request, id, *args, **kwargs):
        try:
            if not request.session.get(request.COOKIES['username'], None):
                return redirect('sign')
        except KeyError:
            return redirect('sign')
        response = hospital.get_info_about_hospital(id)
        response['is_admin'] = request.COOKIES['is_admin']
        if response['error']:
            return redirect('map')
        return render(request, 'hospital/hospital.html', response)
