from django.shortcuts import render
from django.views import View


class MapView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'map/map.html')
