from django.shortcuts import render
from .models import Book
from .models import Author

# Create your views here.

def list_books(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})

def list_authors(request):
    authors = Author.objects.all()
    return render(request, 'books.html', {'authors': authors})
