from django.urls import path
from . import views

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
    path("search/results", views.search_results, name="search_results")
]
