from django.shortcuts import render
from .models import Order

# Create your views here.
def first_page(request):
    all_orders = Order.objects.all()
    return render(request, './index.html', {
        'objects_list': all_orders
    })
