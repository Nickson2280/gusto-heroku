from django.shortcuts import render
from main_gusto.models import Dish

# Create your views here.


def dish_info(request, pk):
    dish = Dish.objects.get(pk=pk)
    return render(request, 'dish.html', context={'dish': dish})
