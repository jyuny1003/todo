from  . import views
from django.urls import path, include

urlpatterns = [
    path('',views.index, name='index'),
    path('favorite', views.favorite, name='favorite'),
    path('favorite/<int:id>', views.favorite_detail, name='favorite'),
    path('todo', views.todo, name='todo'),
    path('todo/<int:id>', views.todo_detail, name='todo')

]