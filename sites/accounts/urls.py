from django.urls import path, include
from accounts.views import home, signup_views, profil_views , logout_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
	path('accounts/', include('django.contrib.auth.urls')),
    path('', home, name='home'),
    path('inscription/', signup_views, name='signup'),
    path('logout/', logout_views, name='logout'),
    path('accounts/profile/', profil_views, name='profil'),
]
