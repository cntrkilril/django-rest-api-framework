from rest_framework.serializers import ModelSerializer
from profiles import models
from rest_framework import serializers

from profiles.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='get_username')
    # followers_count = serializers.IntegerField(source='get_followers_count')
    # following_count = serializers.IntegerField(source='get_following_count')
    # follow_status = serializers.CharField(source='get_follow_status')

    class Meta:
        model = Profile
        fields = ('id', 'username', 'first_name', 'last_name', 'bio', 'location')
        # fields = ('username', 'user_id', 'followers_count', 'following_count',
