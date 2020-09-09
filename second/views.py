from django.shortcuts import render
from django.http import HttpResponse
from .models import Favorite, FavoriteGroup, Todo
# Create your views here.

def index(request):
    
    print(request.GET)
    
    return render(request, 'second/index.html') 


def favorite(request):

    favorite = Favorite.objects.all()
    """
        SELECT *
            FROM favorite
    """
    return render(request, 'second/favorite.html', {
        'text' : '즐겨찾기',
        'favorite' : favorite
        
    }) 

def favorite_detail(request, id):
    print('한번찍어보기', id)
    favorite = Favorite.objects.get(pk=id)

    return render(request, 'second/favorite_detail.html', {
        'favorite': favorite
    })

def todo(request):

    data = Todo.objects
    
    if 'group' in request.GET:
        data = data.filter(group__name=request.GET['group'])
    
    if 'end_date' in request.GET:
        data = data.filter(end_date__gte=request.GET['end_date'])

    end = data.filter(status='end')
    pending = data.filter(status='pending')
    inprogress = data.filter(status='inprogress')


    return render(request, 'second/todo.html', {
        'text' : '내가할일',
        'end' : end.all(),
        'inprogress' : inprogress.all(),
        'pending' : pending.all()
        
        
    }) 


def todo_detail(request, id):
    print('한번찍어보기', id)
    todo = Todo.objects.get(pk=id)

    return render(request, 'second/todo_detail.html', {
        'todo': todo
    })