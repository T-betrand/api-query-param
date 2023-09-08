from rest_framework import serializers
from api.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'slack_name', 'current_day', 'utc_time', 'track', 'github_file_url', 'github_repo_url', 'status_code']
         