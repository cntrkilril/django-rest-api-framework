from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.http import HttpResponse


router = routers.DefaultRouter()


def trigger_error(request):
    division_by_zero = 1/0
    return HttpResponse('error')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('sentry-debug/', trigger_error),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
