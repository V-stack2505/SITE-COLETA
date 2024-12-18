from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
path('', views.index, name='index'),
path('cadastro/', views.cadastro, name='cadastro'),
path('parceiros/', views.parceiros, name='parceiros'),
path('login/', auth_views.LoginView.as_view(), name='login'),
path('logout/', auth_views.LogoutView.as_view(), name='logout'),
path('dicas/', views.dicas, name='dicas'),
]