from django.urls import path
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="index"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('profile/', views.profile, name="profile"),
    path('editprofile/', views.editprofile, name="editprofile"),
    
    path("404/", views.error404, name="error"),
    path("add/", views.add_offer, name="add"),
    path("offer/<int:id>", views.view, name="view"),
    path("offer/<int:id>/edit", views.edit_offer, name="edit"),
    path("category/choose", views.category_list, name="category_list"),
    path("category/cars/", views.category,
        {"category": "cars"}, name="cars",),
    path("category/atv/", views.category, {"category": "atv"}, name="atv"),
    path("category/scooter/", views.category, {"category": "scooter"}, name="scooter"),
    path("category/automobile/", views.category,
        {"category": "automobile"}, name="automobile"),
    path("cart/", views.cart, name="cart"),
    path("user/<int:id>", views.user_view, name="view"),
    path("search/results", views.search_results, name="search_results"),
    
    path('payment/', views.payment, name="payment"),
    
     
    #password reset
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),

]
