from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from service import login, sign

SESSION_TIME = 300


class LogIn(View):

    def post(self, request):
        if login.login(request):
            request.session.set_expiry(SESSION_TIME)
            request.session[request.POST['username']] = True
            response = HttpResponseRedirect('/map')
            response.set_cookie('username', request.POST['username'])
            response.set_cookie('is_admin', request.POST['is_admin'])
            return response
        return render(request, 'registration/login.html')

    def get(self, request):
        return render(request, 'registration/login.html')


class LogOut(View):
    def get(self, request):
        try:
            del request.session[request.COOKIES['username']]
        except KeyError:
            pass
        return redirect('sign')


class SignIn(View):
    def post(self, request):
        if sign.sign(request):
            request.session.set_expiry(SESSION_TIME)
            request.session[request.POST['username']] = True
            response = HttpResponseRedirect('/map')
            response.set_cookie('is_admin', request.POST['is_admin'])
            response.set_cookie('username', request.POST['username'])
            return response
        return redirect('sign')

    def get(self, request):
        return render(request, 'registration/signin.html')


def return_redirect(request):
    return redirect('sign')
