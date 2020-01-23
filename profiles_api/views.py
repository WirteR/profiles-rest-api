from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """Test API View"""
    def get(self, request, format=None):
        an_apiview = [
            'Uses HTTP method as function(get, post, path, put, delete)',
            'Is similar to traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'hello', 'an_apiview': an_apiview})