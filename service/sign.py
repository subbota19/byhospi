from client.models import HosAdmin, Client


def sign(request):
    is_confirmed_user = False
    dict_with_model = {'true': HosAdmin, 'false': Client}
    if dict_with_model[request.POST['is_admin']].objects.filter(username=request.POST['username'],
                                                                password=request.POST['password']):
        is_confirmed_user = True
    return is_confirmed_user
