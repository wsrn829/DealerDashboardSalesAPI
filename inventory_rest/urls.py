from django.urls import path

from .views import (
    api_automobile,
    api_automobiles,
    api_manufacturers,
    api_manufacturer,
    api_vehicle_models,
    api_vehicle_model,
    api_root,
)

urlpatterns = [
    path(
        "", 
        api_root, 
        name="api_root"),  # Use the new view for the root URL
    path(
        "automobiles/",
        api_automobiles,
        name="api_automobiles",
    ),
    path(
        "automobiles/<str:vin>/",
        api_automobile,
        name="api_automobile",
    ),
    path(
        "manufacturers/",
        api_manufacturers,
        name="api_manufacturers",
    ),
    path(
        "manufacturers/<int:pk>/",
        api_manufacturer,
        name="api_manufacturer",
    ),
    path(
        "models/",
        api_vehicle_models,
        name="api_vehicle_models",
    ),
    path(
        "models/<int:pk>/",
        api_vehicle_model,
        name="api_vehicle_model",
    ),
]
