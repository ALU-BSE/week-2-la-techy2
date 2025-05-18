from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Book

def book_list(request):
    book_list = Book.objects.all().order_by('id')  # Fetch all books ordered by ID
    paginator = Paginator(book_list, 10)  # Show 10 books per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'books/book_list.html', {'page_obj': page_obj})
