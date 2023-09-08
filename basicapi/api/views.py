
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from api.serializers import UserSerializer
from api.models import User


from datetime import datetime

# Create your views here.

class UserDetail(APIView):

    def get(self, request, *args, **kwargs):
        queryset = User.objects.all()

        print('REQUEST PARAMS',request.query_params)
        
        check_slack_name = request.query_params.get('slack_name')
        check_track = request.query_params.get('track')

        print('check_slack_name:', check_slack_name, ' check_track: ', check_track)
        
        if check_slack_name:
            queryset = queryset.filter(slack_name=check_slack_name)
        if check_track:
            queryset = queryset.filter(track=check_track)
        
        for user in queryset:
            user.current_day = user.current_day.strftime('%A')
            user.status_code = str(status.HTTP_200_OK)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    
   