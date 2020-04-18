from client.models import Client, HosAdmin


def login(request):
    is_created_user = False
    dict_with_model = {'true': HosAdmin, 'false': Client}
    if not dict_with_model[request.POST['is_admin']].objects.filter(username=request.POST['username']) and \
            not dict_with_model[request.POST['is_admin']].objects.filter(email=request.POST['email']):
        dict_with_model[request.POST['is_admin']](username=request.POST['username'],
                                                  email=request.POST['email'],
                                                  password=request.POST['password']).save()
        is_created_user = True
    return is_created_user
