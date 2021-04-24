import datetime
from django.shortcuts import render, redirect
from .models import Category, Dish, Event, Banner
from .forms import UserMessagesForm
# Create your views here.


def main(request):
    if request.method == 'POST':
        form = UserMessagesForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    special_categories = Category.objects.filter(is_visible=True).filter(is_special=True).order_by('category_order')
    for item in special_categories:
        item.dishes = Dish.objects.filter(category=item.pk)

    categories = Category.objects.filter(is_visible=True).filter(is_special=False).order_by('category_order')
    for item in categories:
        item.dishes = Dish.objects.filter(category=item.pk)

    events = Event.objects.filter(event_date__gte=datetime.date.today())

    banner = Banner.objects.filter(is_visible=True)

    user_messages_form = UserMessagesForm()

    return render(request, 'index.html', context={'categories': categories,
                                                  'special_categories': special_categories,
                                                  'events': events,
                                                  'banner': banner,
                                                  'form': user_messages_form})
