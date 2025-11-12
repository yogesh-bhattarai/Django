from django.urls import path, include
from . import views
urlpatterns = [
    # web application end points
    path("",views.students),

    path('api/v1/', include('api.urls')),
]
