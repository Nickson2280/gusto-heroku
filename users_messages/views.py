from django.shortcuts import render
from main_gusto.models import UserMessages
from django.core.paginator import Paginator
# Create your views here.


def messages_view(request):
    messages = UserMessages.objects.filter(is_checked=False).order_by('send_date')
    paginator = Paginator(messages, 10)
    page = request.GET.get('page')
    messages_page = paginator.get_page(page)
    return render(request, 'messages_view.html', context={'messages': messages_page})
