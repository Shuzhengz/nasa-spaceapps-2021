from django.urls import path, include

urlpatterns = [
    path('api/', include('space_app.api.urls')),
]
