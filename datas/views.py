from django.shortcuts import render, redirect
from .models import Deposit, CIF, Financing, Collateral
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.db.models import Q
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
# def depro_list(request):
#     query = request.GET.get('q')
#     if query:
#         depros = DepositProduct.objects.filter(field__icontains=query) | DepositProduct.objects.filter(description__icontains=query)
#     else:
#         depros = DepositProduct.objects.all()

#     if request.headers.get('x-requested-with') == 'XMLHttpRequest':
#         html = render_to_string('datas/partial_deposit_product_list.html', {'depros': depros})
#         return JsonResponse({'html': html})
    
#     return render(request, 'datas/depro_list.html', {'depros': depros})

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


def search_view(request):
    query = request.GET.get('q', '')
    results=[]

    if query:
        deposit_matches = Deposit.objects.filter(Q(field__icontains=query) | Q(description__icontains=query))
        # product_matches = DepositProduct.objects.filter(Q(field__icontains=query) | Q(description__icontains=query))
        cif_matches = CIF.objects.filter(Q(field__icontains=query) | Q(description__icontains=query))
        financing_matches = Financing.objects.filter(Q(field__icontains=query) | Q(description__icontains=query))
        collateral_matches = Collateral.objects.filter(Q(field__icontains=query) | Q(description__icontains=query))

        results.extend([{'data': result, 'model': 'Deposit'} for result in deposit_matches])
        # results.extend([{'data': result, 'model': 'Deposit Product'} for result in product_matches])
        results.extend([{'data': result, 'model': 'CIF'} for result in cif_matches])
        results.extend([{'data': result, 'model': 'Financing'} for result in financing_matches])
        results.extend([{'data': result, 'model': 'Collateral'} for result in collateral_matches])

    return render(request, 'search_results.html', {'results': results, 'query': query})