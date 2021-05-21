from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from purbeurre.models import UserSavingProduct, ProductInfo
from .forms import SignInForm


def sign_in(request):
    """Method to allow the user to create an account"""
    form = SignInForm()
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,
                             'Compte ustilisateur créé pour '
                             + user
                             )
            return redirect('login')

    context = {'form': form}

    return render(request, 'userpage/sign_in.html', context)


def log_in(request):
    """Method to allow the user to log in to his account"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,
                            username=username,
                            password=password
                            )

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.info(request,
                          'Identifiant ou mot de passe incorrect'
                          )

    return render(request, 'userpage/login.html')


def log_out(request):
    """django method to log out from your user account"""
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def my_account(request):
    """Method To render the user account information's template"""
    return render(request, 'userpage/my_account.html')


@login_required(login_url='login')
def save_in_favorite(request, product_id):
    """
    Method to save a product inside the user favorite's area.
    This method insert the product into the database
    """
    user = request.user
    try:
        UserSavingProduct.objects.get(
            username_id=user.id, product_id=product_id)
        messages.info(request,
                      'CE PRODUIT EST DEJA ENREGISTRE DANS VOS FAVORIS!'
                      )

        return redirect('home')

    except ObjectDoesNotExist:
        UserSavingProduct.objects.create(
            username_id=request.user.id,
            product_id=product_id
        )

        return redirect('my_favorites_view')


@login_required(login_url='login')
def my_favorites_view(request):
    """
    Method to render the favorite template
    that the user can see his saved substitutes
    """
    user = request.user
    favorite = ProductInfo.objects.filter(
        usersavingproduct__username=user.id)
    if favorite:
        fav_product = ProductInfo.objects.filter(
            pk__in=favorite)
    else:
        fav_product = []

    context = {'fav_product': fav_product}

    return render(request,
                  'userpage/my_favorites.html',
                  context
                  )
