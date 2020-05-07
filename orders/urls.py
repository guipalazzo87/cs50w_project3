from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
#    path("add/<str:name>/<str:price>", views.add, name="add"),

]
