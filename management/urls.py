"""djangotry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from products import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home_view, name='home'),
    path("products/create/", views.product_create_view),
    path("about/", views.about_view),
    path("contact/", views.contact_view),
    path("products/", views.product_details_view),
    path("products/<int:id>/", views.product_details_id_view),
    path("orders/", views.order_details_view),
    path("orders/<int:id>/", views.order_details_id_view),
    path("orders/create/", views.order_create_view),
    path("orders/edit/<int:id>/",views.order_edit_id_view),
    path("products/edit/<int:id>/", views.product_edit_id_view),
    path("products/edit/", views.product_edit_view),
    path("orders/edit/", views.order_edit_view),
]
