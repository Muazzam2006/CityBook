from rest_framework import serializers
from ..models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Contact
