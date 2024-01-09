from django.urls import path
from .views import (
    FileCreate
)

urlpatterns = [
    path(
        "files/",
        FileCreate.as_view(),
        name="file_create",
    ),
]