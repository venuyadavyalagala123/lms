from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from .models import Book
from django import forms



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')
        field_classes = {'username':UsernameField}

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'publication_date', 'author', 'price', 'pages', 'book_type', )

