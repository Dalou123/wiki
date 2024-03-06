from django.views.generic import RedirectView

from django.urls import path
from . import views

app_name = "wiki"

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.display_entry, name="title"),
    path("random", views.random_page, name="random"),
    path("search", views.search, name="search"),
    path("create", views.create, name="create"),
    path("edit/<str:title>", views.edit, name="editing"),

    path('favicon.ico',
         RedirectView.as_view(url='/static/favicon/favicon.ico')),
]
