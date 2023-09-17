from django.shortcuts import render

from rest_framework import viewsets
from .models import ApiData
from .serializers import ApiDataSerializer
from datetime import datetime
from rest_framework.response import Response
from django.http import HttpResponse,JsonResponse

'''
class ApiDataViewSet(viewsets.ViewSet):
    def list(self, request):
        slack_name = request.GET.get('slack_name', '')
        track = request.GET.get('track', '')
        current_day = datetime.now().utcnow().strftime('%A')
        utc_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
        #current_day = datetime.now().utcnow().str

        # Implement logic to get current_day, utc_time, GitHub URLs, and status_code here
        # You can use datetime, pytz, and other libraries for date/time operations

        data = {
            "slack_name": slack_name,
            "current_day": current_day,  # Implement logic to get the current day
            "utc_time": utc_time,  # Implement logic to get UTC time
            "track": track,
            "github_file_url": "https://github.com/Cadeau1/API_Endpoint/blob/main/file_name.ext",  # Replace with actual URL
            "github_repo_url": "https://github.com/Cadeau1/API_Endpoint",  # Replace with actual URL
            "status_code": 200
        }

        serializer = ApiDataSerializer(data)
        return Response(serializer.data)

'''

def endpoint(request):
    current_day = datetime.now().utcnow().strftime('%A')
    utc_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
    track = request.GET.get('track', 'Backend')
    slack_name = request.GET.get('slack_name', 'Chiamaka Umunnakwe')
    
    response= {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": "https://github.com/Cadeau1/API_Endpoint.git",  # Replace with actual URL
        "github_repo_url": "https://github.com/Cadeau1/API_Endpoint",  # Replace with actual URL
        "status_code": 200
    }
    
    return render(request,"api.html",{'data':response})
