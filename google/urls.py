from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("gsearch/", views.gsearch, name="gsearch"),
    path("gimgsearch/", views.gimgsearch, name="gimgsearch"),
    path("gadvsearch/", views.gadvsearch, name="gadvsearch")
]
