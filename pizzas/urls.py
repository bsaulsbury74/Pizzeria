from django.urls import path

from . import views

app_name = 'pizzas'

urlpatterns=[
    path('',views.index, name='index'),
    path('pizza_choices',views.pizza_choices, name='pizza_choices'),
    path('pizza_choices/<int:pizza_id>/',views.pizza, name ='pizza'),
    path('comments/<int:pizza_id>/',views.comments, name='comments'),

]