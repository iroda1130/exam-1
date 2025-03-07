from django.shortcuts import render
from .models import Meal


def home_page_view(request):
    return render(request, 'home.html')


def meals_page_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        ingredients = request.POST.get('ingredients')
        price = request.POST.get('price')
        type_ = request.POST.get('type')
        cuisine = request.POST.get('cuisine')
        Meal.objects.create(name=name, ingredient=ingredients, price=price, type=type_, cuisine=cuisine)
    else:
        name = request.GET.get('name')
        ingredients = request.GET.get('ingredients')
        price = request.GET.get('price')
        type_ = request.GET.get('type')
        cuisine = request.GET.get('cuisine')
    meals = Meal.objects.all()
    context = {'meals': meals}
    return render(request, 'meals/meals.html', context)
