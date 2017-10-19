from rest_framework import serializers
from .models import committe, member


class committeSerializer(serializers.ModelSerializer):

    class Meta:
        model = committe
        fields =('name', 'members_no','value')


class memberSerializer(serializers.ModelSerializer):

    class Meta:
        model = member
        fields = ('name','committe','tasks')
