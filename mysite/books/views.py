from django.shortcuts import render_to_response
from django.http import HttpResponse
from books.models import Publisher, Book

def show_publishers(request):
    publishers = Publisher.objects.all()
    return render_to_response("show_publishers.html",dict(publishers=publishers))

def search_book(request):
    error = None
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = "Search string must not be empty!"
        elif len(q) > 20:
            error = "Search strings is too long!"
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',dict(books=books, query=q))

    return render_to_response("search_form.html", dict(error=error))