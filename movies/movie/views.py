from django.shortcuts import render_to_response
from django.http import HttpResponse
from movie.models import Movie
from movie.forms import AddMovieForm

def add_movie(request):
    form = AddMovieForm(request.POST or None)
    if form.is_valid():
        movie = form.save()
        return HttpResponse('Successfully added!')

    return render_to_response('add_movie_form.html', dict(form=form))

def show_movies(request):
    movies = Movie.objects.all()
    return render_to_response('show_movies.html', dict(movies=movies))