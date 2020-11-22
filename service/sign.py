from django.contrib.auth.models import User

from client.models import Client
from client.models import HosAdmin


def sign(request):
    is_confirmed_user = False
    model = HosAdmin if request.POST["is_admin"] == "true" else Client

    if model.objects.filter(
        username=request.POST["username"], password=request.POST["password"]
    ) or User.objects.filter(
        username=request.POST["username"], password=request.POST["password"]
    ):
        is_confirmed_user = True
    return is_confirmed_user
