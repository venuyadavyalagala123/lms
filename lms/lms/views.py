from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accounts.models import Book



@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name='home/index.html'

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

