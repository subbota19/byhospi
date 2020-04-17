from django.shortcuts import render
from django.views import View


class LogIn(View):

    def post(self, request):
        pass

    def get(self, request):
        return render(request, 'registration/login.html')


class LogOut(View):
    def get(self, request):
        pass


class SignIn(View):
    def post(self, request):
        pass
