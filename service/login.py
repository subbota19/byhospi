from client.models import Client
from client.models import HosAdmin
from client.models import Status


def login(request):
    print(request.POST)
    is_created_user = False
    dict_with_model = {"true": HosAdmin, "false": Client}
    if not dict_with_model[request.POST["is_admin"]].objects.filter(
        username=request.POST["username"]
    ) and not dict_with_model[request.POST["is_admin"]].objects.filter(
        email=request.POST["email"]
    ):
        dict_with_model[request.POST["is_admin"]](
            username=request.POST["username"],
            email=request.POST["email"],
            password=request.POST["password"],
            status=Status.objects.get(id=request.POST["status"]),
        ).save()
        is_created_user = True
    return is_created_user
