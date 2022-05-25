from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from profiles.views import ProfileViewSet

router = routers.DefaultRouter()
router.register(r'profile', ProfileViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path("authors/<int:user>/", ProfileViewSet.as_view(actions={"get": "list"})),
]
