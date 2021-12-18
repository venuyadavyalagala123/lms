from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.contrib.auth import logout

from .forms import CustomUserCreationForm
 


# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, "accounts/login.html")

    def post(self, request):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        print(username, password)
        user = authenticate (username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect('/')
            else:
                    return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)



def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            print('user not created')
    form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})

def userlogout(request):
    logout(request)
    return redirect('home')

