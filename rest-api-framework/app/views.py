from urllib.request import Request
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer, GroupsSerializer, ProfileSerializer
from .models import Profile, Post, Groups
from rest_framework.generics import ListAPIView
import django_filters.rest_framework
from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.response import Response


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class GetProfileView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['username', 'location']


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class GetPostView(ListAPIView):
    queryset = Post.objects.filter(Q(likes__gt=230) | Q(title='Пост 1'))
    serializer_class = PostSerializer

class GroupsViewSet(ModelViewSet):
    queryset = Groups.objects.all()
    serializer_class = GroupsSerializer

    @action(methods=['Delete'], detail=True, url_path='delete')
    def delGroup(self, request, pk=None):
        group = self.queryset.get(id=pk)
        group.delete()
        return Response('Succses')

    @action(methods=['Post'], detail=False, url_path='post')
    def delGroup(self, request, pk=None):
        group = self.queryset.create(group_name=request.data.get('group_name'))
        group.save()
        return Response('Succses')

class GetPostFromGroupView(ListAPIView):
    serializer_class = GroupsSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        username = self.kwargs['username']
        return Groups.objects.filter(host=username)
