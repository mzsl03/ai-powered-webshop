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
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/delete/<int:item_id>/', views.delete_cart_item, name='delete_cart_item'),
    path('user_update/', views.user_update, name='user_update'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html',
                                                                 email_template_name='registration/password_reset_email.txt',
                                                                 html_email_template_name='registration/password_reset_email.html',
                                                                 subject_template_name='registration/password_reset_subject.txt'),
                                                                 name='password_reset'),
    path(
        'password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html'
        ),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html'
        ),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
    path('orders/', views.user_order, name='user_order'),
    path('orders_all/', views.all_user_order, name='all_user_order'),
    path("checkout/", views.checkout, name="checkout"),
    path("orders/<int:user_id>/", views.user_order, name="user_order"),
    path("orders/<int:order_id>/update-status/", views.update_order_status, name="update_order_status"),
    path("product/<int:product_id>/update/", views.update_product, name="update_product"),
    path("specs/<int:specs_id>/update/", views.update_specs, name="update_specs"),
]
