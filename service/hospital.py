from django.core import exceptions

from client.models import Client
from client.models import Comment
from hospital.models import Hospital


def get_info_about_hospital(id):
    dict_with_info = {}
    try:
        hospital = Hospital.objects.all().filter(id=id).get()
    except exceptions.ObjectDoesNotExist:
        dict_with_info["error"] = True
    else:
        dict_with_info["hospital"] = hospital
        dict_with_info["error"] = False
    return dict_with_info


def edit_description_form(id, message):
    dict_with_info = {}
    try:
        hospital = Hospital.objects.all().filter(id=id).get()
        hospital.description = message
        hospital.save()
    except exceptions.ObjectDoesNotExist:
        dict_with_info["error"] = True
    else:
        dict_with_info["hospital"] = hospital
        dict_with_info["error"] = False
    return dict_with_info


def create_comment(id, user, comment):
    dict_with_info = {}
    try:
        hospital = Hospital.objects.filter(id=id).get()
        client = Client.objects.filter(username=user).get()
        comment = Comment(
            description=comment, client_hospital=client, hospital_client=hospital
        )
        comment.save()
    except exceptions.ObjectDoesNotExist:
        dict_with_info["error"] = True
    else:
        dict_with_info["error"] = False
    return dict_with_info
