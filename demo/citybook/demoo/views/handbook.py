from rest_framework import generics
from ..models import Handbook
from ..serializers import HandbookSerializer


class HandbookCreate(generics.ListCreateAPIView):
    queryset = Handbook.objects.all()
    serializer_class = HandbookSerializer


class HandbookUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Handbook.objects.all()
    serializer_class = HandbookSerializer
