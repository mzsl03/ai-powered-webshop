from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path("home/", views.home, name="home"),
    path('register/', views.register_view, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path("add_product/", views.add_product, name="add_product"),
    path('product/<int:product_id>/add_specs/', views.add_specs, name='add_specs'),
    path('product/<str:name>/', views.product_detail, name='product-name'),
    path('cart/', views.cart, name="cart"),
    path('cart/delete/<int:item_id>/', views.delete_cart_item, name='delete_cart_item'),
    path('user_update/', views.user_update, name='user_update'),

]