from . import views
from django.urls import path

urlpatterns = [
    path('',views.indexView,name='index'),
    path('new/',views.addTodo,name='add_new'),
    path('finish/<todo_id>/',views.completedTodo,name='finish'),
    path('delete_completed/',views.deleteCompleted,name='delete_completed'),
    path('delete_all/',views.deleteAll,name='delete_all'),

]
