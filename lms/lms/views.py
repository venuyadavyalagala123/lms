from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accounts.models import Book
from django.http import JsonResponse
from django.template.loader import render_to_string
from accounts.forms import BookForm



@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name='home/index.html'

def book_list(request):
    books = Book.objects.all()
    return render(request, 'home/book_list.html', {'books': books})

def book_create(request):
    form = BookForm()
    context = {'form': form}
    html_form = render_to_string('home/partial_book_create.html',
        context,
        request=request,
    )
    return JsonResponse({'html_form': html_form})

