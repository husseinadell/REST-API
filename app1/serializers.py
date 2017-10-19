from rest_framework import serializers
from .models import committe, member


class committeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = committe
        fields =('__all__')


class memberSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = member
        fields = ('__all__')
