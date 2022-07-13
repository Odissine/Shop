from django.shortcuts import render, redirect, HttpResponse
from django.apps import apps
from django.contrib import messages


def index(request):
    context = {}
    return render(request, 'product/index.html', context)


def add_product_element(request, element=None):
    context = {}
    try:
        Model = apps.get_model('product', str(element).capitalize())
        context['element'] = element
    except:
        messages.error(request, "L'élément n'est pas valable ! Veuillez réessayer !")
        return redirect('product-index')

    return render(request, 'product/form_product_element.html', context)
    # return HttpResponse("AJOUTER UNE ESPECE")
