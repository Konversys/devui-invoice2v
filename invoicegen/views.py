from django.shortcuts import render

from invoicegen.treatment import write


def invoice_send(request):
    try:
        if 'save' in request.POST:
            write(request.POST.getlist('data_table'), request.POST.getlist('data_invoice'))
    finally:
        pass
    return render(request, 'invoice.html', locals())