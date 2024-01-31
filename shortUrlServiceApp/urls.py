from django.urls import path

from . import views

urlpatterns = [
    path("", views.default),
    path("urls", views.save_original_url_and_get_short_url),
    path("urls/<str:short_url>", views.get_original_url),
]
