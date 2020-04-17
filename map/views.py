from django.shortcuts import render, redirect
from django.views import View
from service import map


class MapView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'map/map.html', {'info': map.main_info_about_region()})


class RegionView(View):
    def get(self, request, page, region, *args, **kwargs):
        response = map.get_regions_by_name_and_id(page=page, region=region)
        if response['error']:
            return redirect('map')
        return render(request, 'map/region.html', response)
