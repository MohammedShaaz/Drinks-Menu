from django.urls import path

from . import views

urlpatterns = [
    path("drinks/", views.DrinksApi.as_view(), name="drinks"),
    path("drink/<int:id>/",views.DrinksDetails.as_view(),name="drink")
]