from django.urls import path
from . import views
urlpatterns = [
    path('', views.product_list, name='product_list'),  # Page d'accueil avec les produits
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  # Ajouter au panier
    path('cart/', views.cart_view, name='cart'),  # Voir le panier
    path('profile/', views.profile_view, name='profile'),  # Profil utilisateur (modal)
    path("profile/update/", views.update_profile, name="update_profile"),
    path('create-product/', views.create_product, name='create_product'),
    path('product/<int:product_id>/', views.product_detail_view, name='product_detail'),
    path("cart/remove/<int:cart_id>/", views.remove_from_cart, name="remove_from_cart"),
    path("produit/modifier/<int:produit_id>/", views.modifier_produit, name='modifier_produit'),
]