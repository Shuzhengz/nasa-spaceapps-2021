from django.urls import path
from .views import InitialApiView

urlpatterns = [
    path("hello/", InitialApiView.as_view()),
]
