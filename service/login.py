from client.models import Client
from client.models import HosAdmin
from client.models import Status


def login(request):
    is_created_user = False
    model = HosAdmin if request.POST["is_admin"] == "true" else Client
    if not model.objects.filter(
        username=request.POST["username"]
    ) and not model.objects.filter(email=request.POST["email"]):
        model(
            username=request.POST["username"],
            email=request.POST["email"],
            password=request.POST["password"],
            status=Status.objects.filter(id=request.POST["status"]).first(),
        ).save()
        is_created_user = True
    return is_created_user
