from django.shortcuts import render
from .models import Order, Export
from django.contrib import messages
from .forms import OrderUpdateForm
from django.http import HttpResponse
from urllib.parse import *
import io
import csv
import xlwt


# ******** PICKLIST VIEWS **********
def upload(request):
    template = "pack/upload.html"
    if request.method == 'GET':
        return render(request, template)

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

    }
    return render(request, 'pack/all.html', context)


def delete_all(request):
    Order.objects.all().delete()
    context = {
        'msg': '以删除所有订单'
    }
    return render(request, 'pack/delete.html', context)


def detail(request, number):

    sku_sorted = Order.objects.order_by('sku')
    sku_sorted_order = list(sku_sorted.values_list('order_number', flat=True))

    if number not in sku_sorted_order:
        return HttpResponse("Invalid page, return to last page")
    order_number_query = Order.objects.filter(order_number=number)
    sku_index = order_number_query[0]

    form = OrderUpdateForm(request.POST or None, instance=sku_index)

    if form.is_valid():
        form.save()
        form = OrderUpdateForm()

    if sku_sorted_order.index(number) == 0:
        if len(sku_sorted_order) == 1:
            prev = sku_sorted_order[0]
            after = sku_sorted_order[0]
        else:
            prev = sku_sorted_order[len(sku_sorted_order)-1]
            after = sku_sorted_order[1]

    elif sku_sorted_order.index(number) == len(sku_sorted_order)-1:
        if len(sku_sorted_order) == 1:
            prev = sku_sorted_order[0]
            after = sku_sorted_order[0]
        else:
            prev = sku_sorted_order[len(sku_sorted_order) - 2]
            after = sku_sorted_order[0]
    else:
        prev = sku_sorted_order[sku_sorted_order.index(number)-1]
        after = sku_sorted_order[sku_sorted_order.index(number)+1]

    context = {
        'order': sku_index,
        'sku': quote(sku_index.sku, safe=''),
        'next': after,
        'prev': prev,
        'number': sku_sorted_order.index(number)+1,
        'total': sku_sorted.count(),
        'form': form
    }
    return render(request, 'pack/detail.html', context)


def sku_view(request, sku):
    if unquote(sku) == 'skunotavailable':
        return HttpResponse("No Matching SKUs")

    sku = unquote(sku)

    sku_filter = Order.objects.filter(sku=sku)
    order_numbers = list(sku_filter.values_list('order_number', flat=True))
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
        'order_numbers': order_numbers,
        'sku_count': len(unique_sku),
        'sku_index': unique_sku.index(sku) + 1
    }

    return render(request, 'pack/sku.html', context)


# ******** DICTIONARY VIEWS **********



def dictionary(request):
    # unique_sku = sorted(set(Order.objects.values_list('sku', flat=True)))
    # registered = []
    #
    # for sku in unique_sku:
    #     if Dictionary.objects.filter(sku=sku).count() != 0:
    #         registered.append(Dictionary.objects.get(sku=sku))
    # registered = Entry.objects.order_by('sku')

    context = {
        # 'registered': registered,
    }

    return render(request, 'pack/dictionary.html', context)


def dictionary_update(request):

    # unique_sku = sorted(set(Order.objects.values_list('sku', flat=True)))
    # unregistered = []
    #
    # for sku in unique_sku:
    #     if Entry.objects.filter(sku=sku).count() == 0:
    #         unregistered.append(sku)
    # for sku in unregistered:
    #     if Entry.objects.filter(sku=sku).count() != 0:
    #         unregistered.remove(sku)

    context = {
        # 'unregistered': unregistered,
    }
    return render(request, 'pack/dict_update.html', context)


def download_update(request):
    template = 'pack/download_update.html'
    # unique_sku = sorted(set(Order.objects.values_list('sku', flat=True)))
    #
    # unregistered = []
    #
    # for sku in unique_sku:
    #     if Entry.objects.filter(sku=sku).count() == 0:
    #         unregistered.append(sku)
    # for sku in unregistered:
    #     if Entry.objects.filter(sku=sku).count() != 0:
    #         unregistered.remove(sku)

    # list_a = Entry.objects.order_by('sku')[0]
    # list_b = Product.objects.all()
    # for i in list_a:
    #     i.additional_data = [b for b in list_b if b.model_link_id == i.id]
    context = {
        # 'unregistered': unregistered,

    }
    return render(request, template, context)


def export_update(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="updates.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Updates')  # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['product_code', 'price', 'discount', 'quantity']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Export.objects.all().values_list('product_code', 'price', 'discount', 'quantity')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response
