from django.shortcuts import render, redirect
from django.views import View
from service import login, sign

SESSION_TIME = 30


class LogIn(View):

    def post(self, request):
        if login.login(request):
            request.session.set_expiry(SESSION_TIME)
            request.session[request.POST['username']] = True
            return render(request, 'map/map.html')
        return render(request, 'registration/login.html')

    def get(self, request):
        return render(request, 'registration/login.html')


class LogOut(View):
    def get(self, request):
        del request.session[request.GET['username']]
        return render(request, 'registration/signin.html')


class SignIn(View):
    def post(self, request):
        print(request.POST)
        if sign.sign(request):
            request.session.set_expiry(SESSION_TIME)
            request.session[request.POST['username']] = True
            return redirect('map')
        return redirect('sign')

    def get(self, request):
        return render(request, 'registration/signin.html')
