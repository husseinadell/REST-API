from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import committe, member
from .serializers import committeSerializer, memberSerializer

# Create your views here.
class committeViewSet(viewsets.ModelViewSet):
    queryset = committe.objects.all()
    serializer_class = committeSerializer


class memberViewSet(viewsets.ModelViewSet):
    queryset = member.objects.all()
    serializer_class = memberSerializer
