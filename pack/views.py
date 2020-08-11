from django.shortcuts import render
from .models import Order
from django.contrib import messages
from .forms import OrderUpdateForm
from django.http import HttpResponse
from urllib.parse import *
import io
import csv


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

        _, created = Order.objects.update_or_create(
            batch_id=column[105],
            order_number=column[63],
            sku=column[88],
            quantity=column[75],
        )

    context = {}
    return render(request, template, context)


def all_orders(request):
    sku_list = Order.objects.order_by('sku').values_list('sku', flat=True)
    unique_sku = sorted(set(Order.objects.values_list('sku', flat=True)))
    if len(unique_sku) > 0:
        first_sku = unique_sku[0]
    else:
        first_sku = 'skunotavailable'
    copy = []
    for item in range(len(sku_list)):
        copy.append(quote(sku_list[item], safe=''))

    context = {
        'all': zip(Order.objects.order_by('sku'), copy),
        'first': quote(first_sku, safe=''),
        # 'sku_link': sku_list
    }
    return render(request, 'pack/all.html', context)


def delete_all(request):
    Order.objects.all().delete()
    context = {
        'msg': '以删除所有订单'
    }
    return render(request, 'pack/delete.html', context)


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
    if unquote(sku) == 'skunotavailable':
        return HttpResponse("No Matching SKUs")

    sku = unquote(sku)

    sku_filter = Order.objects.filter(sku=sku)
    total_quantity = sum(sku_filter.values_list('quantity', flat=True))

    unique_sku = sorted(set(Order.objects.values_list('sku', flat=True)))

    if unique_sku.index(sku) == 0:
        if len(unique_sku) == 1:
            prev = unique_sku[0]
            after = unique_sku[0]
        else:
            prev = unique_sku[len(unique_sku)-1]
            after = unique_sku[1]

    elif unique_sku.index(sku) == len(unique_sku)-1:
        if len(unique_sku) == 1:
            prev = unique_sku[0]
            after = unique_sku[0]
        else:
            prev = unique_sku[len(unique_sku) - 2]
            after = unique_sku[0]
    else:
        prev = unique_sku[unique_sku.index(sku)-1]
        after = unique_sku[unique_sku.index(sku)+1]

    context = {
        'sku': sku_filter[0],
        'total': total_quantity,
        'prev': quote(prev, safe=''),
        'after': quote(after, safe=''),
        'sku_count': len(unique_sku),
        'sku_index': unique_sku.index(sku) + 1
    }

    return render(request, 'pack/sku.html', context)
