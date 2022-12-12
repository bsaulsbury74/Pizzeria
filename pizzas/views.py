from django.shortcuts import render,redirect
from .models import *
from .forms import CommentForm

def index(request):
    return render(request, 'pizzas/index.html')

def pizza_choices(request):
    pizza_choices=Pizza.objects.all()

    context={'pizza_choices':pizza_choices}
    return render(request, 'pizzas/pizza_choices.html',context)

def pizza(request, pizza_id):
    p = Pizza.objects.get(id=pizza_id)

    toppings = Topping.objects.filter(pizza=p)
    comment= Comment.objects.filter(pizza=p)
    pictures= Picture.objects.filter(pizza=p)

    context = {'pizza':p, 'toppings':toppings, 'comment':comment, 'pictures':pictures}
    return render(request, 'pizzas/pizza.html', context)


def comments (request, pizza_id):
    pizza= Pizza.objects.get(id=pizza_id)

    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)

        if form.is_valid():
            comments = form.save(commit=False)
            comments.pizza=pizza
            comments.save()
            return redirect('pizzas:pizza', pizza_id=pizza_id)
    context = {'form':form, 'pizza':pizza}
    return render(request, 'pizzas/comments.html', context)
    

