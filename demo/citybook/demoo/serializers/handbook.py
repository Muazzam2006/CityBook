from rest_framework import serializers
from ..models import Handbook
from ..serializers import CategorySerializer, ContactSerializer, CitySerializer, HandbookSerializer


class HandbookSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    city = CitySerializer()
    category = CategorySerializer()

    class Meta:
        fields = ('__all__')
        model = Handbook
