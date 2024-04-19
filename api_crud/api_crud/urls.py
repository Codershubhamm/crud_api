from django.contrib import admin
from django.urls import path
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("products/",views.products),
    path("sproducts/<int:id>",views.s_products),
    path("recproducts/",views.recproducts),
    path("patproducts/<int:id>",views.patproducts),
    path("delproduct/<int:id>",views.deletep),
]
