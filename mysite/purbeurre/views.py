# coding: utf-8
from django.shortcuts import render
from django.core.paginator import Paginator
from purbeurre.models import ProductInfo


def home(request):
    return render(request, "pages/home.html")


def legal_notices(request):
    return render(request, "pages/mentions_legales.html")


def search_product(request):
    # je récupère l'input utilisateur
    research_user = request.GET.get("user_research")
    try:
        # je cherche les produits qui peuvent convenir à la demande
        result = ProductInfo.objects.filter(name_product__contains=research_user)[0]
        products = ProductInfo.objects.filter(
            category=result.category,
            nutrition_grade__lt=result.nutrition_grade) \
            .order_by("nutrition_grade")[:6]
        # afficher 6 produits sur la page
        paginate = Paginator(products, 6)
        # récupérer la page où l'on veut afficher
        page = request.GET.get('page')
        page_num = paginate.get_page(page)

        context = {
            "page_num": page_num,
            "paginate": True,
            "title": research_user,
            "image": result.image_product,
            "nutriscore": result.nutrition_grade,
            "products": products
        }

    except IndexError:
        return render(request, "pages/search_product.html", {"title": research_user})

    return render(request, "pages/search_product.html", context)


def product_info(request, description):
    product_infos = ProductInfo.objects.get(id=description)

    context = {
        "page_title": "Informations produit",
        "title": product_infos.name_product,
        "nutrition": product_infos.nutrition_grade,
        "image": product_infos.image_product,
        "image_nutrition": product_infos.image_nutrition,
        "url": product_infos.url_product
    }

    return render(request, "pages/infoprod.html", context)
