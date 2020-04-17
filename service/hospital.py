from hospital.models import Hospital
from django.core import exceptions


def get_info_about_hospital(id):
    dict_with_info = {}
    try:
        hospital = Hospital.objects.all().filter(id=id).get()
    except exceptions.ObjectDoesNotExist:
        dict_with_info['error'] = True
    else:
        dict_with_info['hospital'] = hospital
        dict_with_info['error'] = False
    return dict_with_info
