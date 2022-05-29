from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, GroupsViewSet, GetPostView, GetProfileView, ProfileViewSet, GetPostFromGroupView

router = DefaultRouter()
router.register('post', PostViewSet, )
router.register('group', GroupsViewSet, )
router.register('profile', ProfileViewSet, )

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/post/f', GetPostView.as_view()),
    path('api/profile/f', GetProfileView.as_view()),
    re_path('^api/group/host/(?P<username>.+)/$', GetPostFromGroupView.as_view())
]
