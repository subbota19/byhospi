from client.models import HosAdmin, Client


def sign(request):
    is_created_user = False
    dict_with_model = {'true': HosAdmin, 'false': Client}
    if dict_with_model[request.POST['is_admin']].objects.filter(username=request.POST['username'],
                                                                password=request.POST['password']):
        is_created_user = True
    return is_created_user
