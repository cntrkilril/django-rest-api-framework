from rest_framework.serializers import ModelSerializer
from .models import Post, Profile, Groups


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class GroupsSerializer(ModelSerializer):
    class Meta:
        model = Groups
        fields = '__all__'