from django.shortcuts import render, redirect
from .models import Deposit, DepositProduct, CIF, Financing, Collateral
from django.http import JsonResponse
from django.template.loader import render_to_string
# Create your views here.

def front_page(request):
    return render(request, 'datas/front_page.html')

# Deposit List View
def dep_list(request):
    
    query = request.GET.get('q')
    if query:
        deposits = Deposit.objects.filter(field__icontains=query) | Deposit.objects.filter(description__icontains=query)
    else:
        deposits = Deposit.objects.all()
    
    # Check if the request is AJAX
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # Render a separate template for AJAX
        html = render_to_string('datas/partial_deposit_list.html', {'deposits': deposits})
        return JsonResponse({'html': html})

    return render(request, 'datas/dep_list.html', {'deposits': deposits})
# Deposit Product List View
def depro_list(request):
    query = request.GET.get('q')
    if query:
        depros = DepositProduct.objects.filter(field__icontains=query) | DepositProduct.objects.filter(descriptiom__icontains=query)
    else:
        depros = DepositProduct.objects.all()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('datas/partial_deposit_product_list.html', {'depros': depros})
        return JsonResponse({'html': html})
    
    return render(request, 'datas/depro_list.html', {'depros': depros})

# CIF List View
def cif_list(request):
    query = request.GET.get('q')
    if query:
        cifs = CIF.objects.filter(field__icontains=query) | CIF.objects.filter(field_name__icontains=query) | CIF.objects.filter(description__icontains=query)
    else:
        cifs = CIF.objects.all()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('datas/partial_cif_list.html', {'cifs': cifs})
        return JsonResponse({'html': html})
    
    return render(request, 'datas/cif_list.html', {'cifs': cifs})

# Financing List View
def fin_list(request):
    query = request.GET.get('q')
    if query:
        fins = Financing.objects.filter(field__icontains=query) | Financing.objects.filter(field_name__icontains=query) | Financing.objects.filter(description__icontains=query)
    else:
        fins = Financing.objects.all()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('datas/partial_financing_list.html', {'fins': fins})
        return JsonResponse({'html': html})
    
    return render(request, 'datas/fin_list.html', {'fins': fins})

# Collateral List View
def col_list(request):
    query = request.GET.get('q')
    if query:
        cols = Collateral.objects.filter(field__icontains=query) | Collateral.objects.filter(field_name__icontains=query) | Collateral.objects.filter(description__icontains=query)
    else:
        cols = Collateral.objects.all()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('datas/partial_collateral_list.html', {'cols': cols})
        return JsonResponse({'html': html})
    
    return render(request, 'datas/col_list.html', {'cols': cols})


