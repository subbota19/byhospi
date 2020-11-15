from client.models import Client
from client.models import HosAdmin
from client.models import Status


def login(request):
    is_created_user = False
    dict_with_model = {"HosAdmin": HosAdmin, "Client": Client}
    if not dict_with_model[request.POST["is_admin"]].objects.filter(
        username=request.POST["username"]
    ) and not dict_with_model[request.POST["is_admin"]].objects.filter(
        email=request.POST["email"]
    ):
        dict_with_model[request.POST["is_admin"]](
            username=request.POST["username"],
            email=request.POST["email"],
            password=request.POST["password"],
            status=Status.objects.filter(id=request.POST["status"]).first(),
        ).save()
        is_created_user = True
    return is_created_user
