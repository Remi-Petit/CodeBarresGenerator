from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("code-barre", views.codeBarre, name="codeBarre"),
]