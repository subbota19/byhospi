from hospital.models import Hospital
from map.models import Region


def main_info_about_region():
    regions = {"Br": {}, "Go": {}, "Gr": {}, "Vi": {}, "Mi": {}, "Mo": {}}
    for index, item in enumerate(regions, 1):
        region_object = Region.objects.filter(id=index).get()

        regions[item]["count"] = region_object.hospital_set.all().count()
        regions[item]["population"] = region_object.population
        regions[item]["name"] = region_object.name
        regions[item]["help"] = (
            region_object.hospital_set.all().filter(need_help=True).count()
        )
    return regions


def get_regions_by_name_and_id(region, page, obj_on_page=10):
    response = {}
    dict_for_transformation_name = {
        "br": "Брестская область",
        "vi": "Витебская область",
        "go": "Гомельская область",
        "gr": "Гродненская область",
        "mi": "Минская область",
        "mo": "Могилевская область",
    }
    try:
        hospitals = (
            Hospital.objects.filter(location__name=dict_for_transformation_name[region])
            .order_by("need_help")
            .order_by("need_help")
            .reverse()
        )
    except KeyError:
        response["error"] = True
    else:
        response["pages_count"] = range(hospitals.count() // obj_on_page + 1)
        response["hospitals"] = hospitals[(page - 1) * obj_on_page : page * obj_on_page]
        response["region_name"] = region
        response["error"] = False
    return response
