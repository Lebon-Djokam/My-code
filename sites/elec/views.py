from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, Profile
from .forms import ProfileForm, ProductForm, ProduitForm

# 🔹 Liste des produits disponibles à la vente
def product_list(request):
    products = Product.objects.all()
    if request.method == 'GET':
        name = request.GET.get('recherche')
        if name is not None:
            products = Product.objects.filter(name__icontains=name)
    return render(request, "products/product_list.html", {"products": products})

# 🔹 Ajout d'un produit au panier
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    return redirect("cart")

# 🔹 Affichage du panier avec les produits ajoutés
@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, "cart/cart.html", {"cart_items": cart_items})

# 🔹 Affichage et mise à jour du profil utilisateur dans un modal
@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    products = Product.objects.filter(seller=request.user)
    products = Product.objects.all()
    form = ProfileForm(instance=profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile")

    return render(request, "users/profile_modal.html", {"profile": profile,
                                                        "form": form,
                                                        'products':products})

# Profil utilisateur (mis à jour via le modal Bootstrap)
@login_required
def update_profile(request):
    if request.method == "POST":
        request.user.username = request.POST.get("username")
        request.user.email = request.POST.get("email")
        request.user.save()
        return redirect("product_list")
    return render(request, "users/profile_modal.html")

@login_required
def create_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/create_product.html', {'form': form})

def product_detail_view(request, product_id):
    product =  get_object_or_404(Product, id=product_id)
    return render(request, "products/product_detail.html", {
		'product':product
	})


# Suppression d'un article du panier
@login_required
def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
    cart_item.delete()
    return redirect("cart")

#Créez une vue pour modifier un produit spécifique :
@login_required
def modifier_produit(request, produit_id):
    produit = get_object_or_404(Product, id=produit_id, user=request.user)
    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirige vers le profil après modification
    else:
        form = ProduitForm(instance=produit)
    return render(request, 'modifier_produit.html', {'form': form})

# from django.shortcuts import render
# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required
# from .models import Product, Cart
# from .forms import ProductForm, SignUpForm
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import AuthenticationForm

# # Page d'accueil avec la liste des produits
# def product_list(request):
#     products = Product.objects.all()
#     return render(request, "products/product_list.html", {"products": products})

# # Détails d'un produit
# def product_detail(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     return render(request, "products/product_detail.html", {"product": product})

# # Inscription
# def signup(request):
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect("product_list")
#     else:
#         form = SignUpForm()
#     return render(request, "users/signup.html", {"form": form})

# # Connexion
# def user_login(request):
#     if request.method == "POST":
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect("product_list")
#     else:
#         form = AuthenticationForm()
#     return render(request, "users/login.html", {"form": form})

# # Ajout au panier
# @login_required
# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
#     if not created:
#         cart_item.quantity += 1
#         cart_item.save()
#     return redirect("cart")

# # Affichage du panier
# @login_required
# def cart(request):
#     cart_items = Cart.objects.filter(user=request.user)
#     return render(request, "cart/cart.html", {"cart_items": cart_items})

# # Suppression d'un article du panier
# @login_required
# def remove_from_cart(request, cart_id):
#     cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
#     cart_item.delete()
#     return redirect("cart")

# # Profil utilisateur (mis à jour via le modal Bootstrap)
# @login_required
# def update_profile(request):
#     if request.method == "POST":
#         request.user.username = request.POST.get("username")
#         request.user.email = request.POST.get("email")
#         request.user.save()
#         return redirect("product_list")
#     return render(request, "users/profile_modal.html")
