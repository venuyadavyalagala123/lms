from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, login

# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect('/form')
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)


def signup(request):
    return render(request,'accounts/login.html')
