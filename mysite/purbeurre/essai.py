from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
# from django.http import HttpResponse
# Create your views here.
from purbeurre.models import ProductInfo


def home(request):
    return render(request, 'pages/home.html')


def research(request):
    """
    The user is looking for a product.
    I'm trying to find it in the database.
    I search for substitutes in the same
    categories and post them on the page.
    """

    search = request.GET.get('search_user')
    user_research = search.capitalize()

    try:
        product = ProductInfo.objects.filter(name_product=user_research).first()
        substitutes = ProductInfo.objects.filter(
            category=product.category,
            nutrition_grade__lt=product.nutrition_grade).\
            order_by("nutrition_grade")

        paginator = Paginator(substitutes, 6)
        page = request.GET.get('page')
        alt_products = paginator.get_page(page)

        context = {
            'alt_products': alt_products,
            'paginate': True,
            'title': user_research,
            'image': product.picture_product,
            'nutri': product.nutrition_grade,
        }

    except AttributeError:
        messages.warning(request,
                         "Ce produit est introuvable. "
                         "Vérifiez l'orthographe de la "
                         "recherche.")
        return redirect('home')

    return render(request, 'search.html', context)


def detail(request, substitut_detail):
    """
    The user chooses to learn more
    about the surrogate. I show him the
    different information.
    """

    product_detail = ProductInfo.objects.get(id=substitut_detail)

    context_detail = {
        'title_page': 'Informations supplémentaires',
        'title': product_detail.name_product,
        'nutri': product_detail.nutrition_grade,
        'image': product_detail.picture_product,
        'image_nutri': product_detail.picture_nutrition,
        'url': product_detail.url_product,
    }

    return render(request, 'detail.html', context_detail)



from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'pages/home.html')

_________________________________________________________________________

from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
# from django.http import HttpResponse
# Create your views here.
from .models import ProductInfo


def home(request):
    return render(request, 'pages/home.html')


def research(request):
    """
    The user is looking for a product.
    I'm trying to find it in the database.
    I search for substitutes in the same
    categories and post them on the page.
    """

    search = request.GET.get('user_research')
    user_research = search.capitalize()

    try:
        product = ProductInfo.objects.filter(name_product=user_research).first()
        substitutes = ProductInfo.objects.filter(
            category=product.category,
            nutrition_grade=product.nutrition_grade).\
            order_by("nutrition_grade")

        paginator = Paginator(substitutes, 6)
        page = request.GET.get('page')
        alt_products = paginator.get_page(page)

        context = {
            'alt_products': alt_products,
            'paginate': True,
            'title': user_research,
            'image': product.picture_product,
            'nutri': product.nutrition_grade,
        }

    except AttributeError:
        messages.warning(request,
                         "Ce produit est introuvable. "
                         "Vérifiez l'orthographe de la "
                         "recherche.")
        return redirect('home')

    return render(request, 'search.html', context)


def detail(request, substitut_detail):
    """
    The user chooses to learn more
    about the surrogate. I show him the
    different information.
    """

    product_detail = ProductInfo.objects.get(id=substitut_detail)

    context_detail = {
        'title_page': 'Informations supplémentaires',
        'title': product_detail.name_product,
        'nutri': product_detail.nutrition_grade,
        'image': product_detail.picture_product,
        'image_nutri': product_detail.picture_nutrition,
        'url': product_detail.url_product,
    }

    return render(request, 'detail.html', context_detail)