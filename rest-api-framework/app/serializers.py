from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Post, Profile, Groups


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def validate(self, attrs):
        likes = attrs['likes']
        dislikes = attrs['dislikes']
        if likes != 0 or dislikes != 0:
            raise serializers.ValidationError({'likes': "Кол-во лайков не может быть больше 0 при создании",
                                               'dislikes': "Кол-во лайков не может быть больше 0 при создании"})


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class GroupsSerializer(ModelSerializer):
    class Meta:
        model = Groups
        fields = '__all__'
