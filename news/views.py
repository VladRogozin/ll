from rest_framework import generics
from .models import New
from .serializers import NewSerializer


class NewListView(generics.ListAPIView):
    serializer_class = NewSerializer

    def get_queryset(self):
        amount = self.kwargs.get('amount', 10)

        queryset = New.objects.all()

        queryset = queryset.order_by('?')

        return queryset[:amount]


class NewCreateView(generics.CreateAPIView):
    queryset = New.objects.all()
    serializer_class = NewSerializer
