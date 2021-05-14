from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from purbeurre.models import ProductInfo


def home(request):
    return render(request, "pages/home.html")


def legal_notices(request):
    return render(request, "pages/mentions_legales.html")


def search_product(request):
    # je récupère l'input utilisateur
    research_user = request.GET.get("user_research")
    # je cherche les produits qui peuvent convenir à la demande
    get_product = ProductInfo.objects.filter(name_product__contains=research_user)
    products = get_product[:6]
    # afficher 6 produits sur la page
    paginate = Paginator(products, 6)
    # récupérer la page où l'on veut afficher
    page = request.GET.get('page')
    page_num = paginate.get_page(page)

    context = {
        "page_num": page_num,
        "paginate": True,
        "products": products
    }

    return render(request, "pages/search_product.html", context)


def search_substitute(request, product_id):
    # je récupère l'input utilisateur
    user_choice = request.GET.get(product_id)
    # je cherche les produits qui peuvent convenir à la demande
    get_product = ProductInfo.objects.filter(name_product__contains=user_choice)
    products = get_product[:6]
    # Je cherche les produits de même catégorie que mon 2eme produit demander
    # avec un nutriscore inferieur que je vais ranger dans l'ordre croissant.
    substitute = ProductInfo.objects.filter(
        category=products.category,
        nutrition_grade__lt=products.nutrition_grade) \
        .order_by("nutrition_grade")[:6]

    # afficher 6 produits sur la page
    paginate = Paginator(substitute, 6)
    # récupérer la page où l'on veut afficher
    page = request.GET.get('page')
    actual_page = paginate.get_page(page)

    context = {
        "acutal_page": actual_page,
        "paginate": True,
        "title": user_choice ,
        "image": products.image_product,
        "nutriscore": products.nutrition_grade,
    }

    return render(request, "pages/substitutes.html", context)


def product_info(request, substitute):
    product_infos = ProductInfo.objects.get(id=substitute)

    context = {
        "page_title": "Informations produit",
        "title": product_infos.name_product,
        "nutrition": product_infos.nutrition_grade,
        "image": product_infos.image_product,
        "image_nutrition": product_infos.image_nutrition,
        "url": product_infos.url_product
    }

    return render(request, "pages/infoprod.html", context)