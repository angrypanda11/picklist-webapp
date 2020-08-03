from django.shortcuts import render
from .models import Order
from .resources import OrderResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse

# Create your views here.
def upload(request):
    if request.method == 'POST':
        order_resource = OrderResource()
        dataset = Dataset()
        new_order = request.FILES['myfile']

        if not new_order.name.endswith('xlsx'):
            messages.info(request, 'wrong format')
            return render(request, 'pack/upload.html')

        imported_orders = dataset.load(new_order.read(), format='xlsx')
        # with open(new_order, 'r') as imported_orders:
        for data in imported_orders:
            value = Order(
                data[0],
                data[106],
                data[64],
                data[89],
                data[76],

            )
            value.save()

    return render(request, 'pack/upload.html')
