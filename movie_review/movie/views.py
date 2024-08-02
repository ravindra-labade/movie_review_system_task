from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie


def add_reviews(request):
    form = MovieForm()
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    return render(request, 'movie/add.html', {'form': form})


def show_reviews(request):
    movies = Movie.objects.all()
    return render(request, 'movie/show.html', {'movies': movies})


def update_reviews(request, pk):
    obj = Movie.objects.get(id=pk)
    form = MovieForm(instance=obj)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    return render(request, 'movie/add.html', {'form': form})


def delete_reviews(request, pk):
    obj = Movie.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    return render(request, 'movie/confirm.html')




