from django.shortcuts import get_object_or_404, render
from .models import Order
from django.contrib import messages
from .forms import OrderUpdateForm
from django.http import HttpResponse
import io
import csv
# from django.views import generic
# from tablib import Dataset
# from .resources import OrderResource


def upload(request):
    template = "pack/upload.html"
    prompt = {
        'ID': 'Please only submit .csv files'
    }

    if request.method == 'GET':
        return render(request, template, prompt)

    csv_file = request.FILES['myfile']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Not a csv file')

    order_list = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(order_list)
    next(io_string)
    for column in csv.reader(io_string, delimiter=','):
        # print(column[76])
        _, created = Order.objects.update_or_create(
            batch_id=column[105],
            order_number=column[63],
            sku=column[88],
            quantity=column[75],
        )
        # print(column[76])
    context = {}
    return render(request, template, context)


def all_orders(request):
    sku_sorted = Order.objects.order_by('sku')
    # first_item = sku_sorted.values_list('sku', flat=True)[0]

    context = {
        'sorted': sku_sorted,
        # 'first': first_item
    }
    return render(request, 'pack/all.html', context)


def detail(request, number):
    number = int(number)
    sku_sorted = Order.objects.order_by('sku')

    if sku_sorted.count() < number or number < 1:
        return HttpResponse("Invalid page, return to last page")
    sku_index = sku_sorted[number-1]

    form = OrderUpdateForm(request.POST or None, instance=sku_index)

    if form.is_valid():
        form.save()
        form = OrderUpdateForm()

    context = {
        'order': sku_index,
        'next': number+1,
        'prev': number-1,
        'number': number,
        'total': sku_sorted.count(),
        'form': form
    }
    return render(request, 'pack/detail.html', context)


def sku_view(request, sku):
    sku_sorted = Order.objects.order_by('sku')
    return None
