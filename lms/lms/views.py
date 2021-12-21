from django.shortcuts import render
from django.views.generic import ListView,TemplateView,View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accounts.models import CrudUser
from django.http import JsonResponse
from django.template.loader import render_to_string
# from accounts.forms import CustomUserCreationForm



@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name='home/index.html'

class CrudView(ListView):
    model = CrudUser
    template_name = 'home/crud.html'
    context_object_name = 'users'

class CreateCrudUser(View):
    def get(self, request):
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = CrudUser.objects.create(
            name = name1,
            address = address1,
            age = age1
        )

        user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)

class UpdateCrudUser(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        name1 = request.POST.get('name', None)
        address1 = request.POST.get('address', None)
        age1 = request.POST.get('age', None)

        print(id1)

        obj = CrudUser.objects.get(id=id1)
        obj.name = name1
        obj.address = address1
        obj.age = age1
        obj.save()

        user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)

class DeleteCrudUser(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        CrudUser.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)




