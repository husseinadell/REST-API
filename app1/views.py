from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import committe, member
from .serializers import committeSerializer, memberSerializer
from rest_framework import generics
# Create your views here.
class committeList(generics.ListCreateAPIView):
    queryset = committe.objects.all()
    serializer_class = committeSerializer

class committeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = committe.objects.all()
    serializer_class = committeSerializer

class memberList(generics.ListCreateAPIView):
    queryset = member.objects.all()
    serializer_class = memberSerializer

class memberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = member.objects.all()
    serializer_class = memberSerializer
