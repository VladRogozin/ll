from rest_framework import generics
from .models import Fact
from .serializers import FactSerializer
from django.http import JsonResponse


class FactListView(generics.ListAPIView):
    serializer_class = FactSerializer

    def get_queryset(self):
        amount = self.kwargs.get('amount', 10)

        queryset = Fact.objects.all()

        queryset = queryset.order_by('?')

        return queryset[:amount]


class FactCreateView(generics.CreateAPIView):
    queryset = Fact.objects.all()
    serializer_class = FactSerializer
