from django.db import IntegrityError
from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError, ValidationError
from rest_framework.viewsets import ModelViewSet

from profiles.models import Profile

from profiles.serializers import ProfileSerializer


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    @action(methods=['GET'], detail=True, url_path='all')
    def get(self, request):
        return JsonResponse(
            Profile.objects.all()
        )

    @action(methods=['GET'], detail=True, url_path='list')
    def get(self, request):
        return JsonResponse(
            Profile.objects.all()
        )

    @action(methods=['PATCH'], detail=False, url_path='update')
    def update_profile(self, request):
        profile = Profile.objects.filter(username=request.data['username']).first()
        profile.first_name = request.data['first_name']
        profile.last_name = request.data['last_name']
        profile.bio = request.data['bio']
        profile.location = request.data['location']
        profile.save()
        return JsonResponse({"response": "change successful"})

    @action(methods=['POST'], detail=False, url_path='create')
    def create_profile(self, request):
        if 'username' not in request.data:
            raise ParseError({'message': 'Username cannot be empty'})
        try:
            bad_words = ["black", "white"]
            username = request.data['username']
            for word in bad_words:
                print(username.find(word))
                if username.find(word) == -1:
                    raise ValidationError(
                        {"username": 'contains an invalid word'}
                    )

            profile = Profile.objects.create(username=request.data['username'],
                                             first_name=request.data['first_name'],
                                             last_name=request.data['last_name'],
                                             bio=request.data['bio'],
                                             location=request.data['location']
                                             )
            profile.save()
            return JsonResponse({'message': 'success'})
        except IntegrityError:
            return JsonResponse({'message': 'User with this username already exist'})
