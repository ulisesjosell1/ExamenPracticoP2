from rest_framework import generics
from .models import Tenis
from .serializers import TenisSerializer

class TenisListCreate(generics.ListCreateAPIView):
    queryset = Tenis.objects.all()
    serializer_class = TenisSerializer

class TenisRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tenis.objects.all()
    serializer_class = TenisSerializer

