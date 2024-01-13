from rest_framework import generics
from .models import Quote
from .serializers import QuoteSerializer


class QuoteListView(generics.ListAPIView):
    serializer_class = QuoteSerializer

    def get_queryset(self):
        amount = self.kwargs.get('amount', 10)

        queryset = Quote.objects.all()

        queryset = queryset.order_by('?')

        return queryset[:amount]


class QuoteCreateView(generics.CreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
