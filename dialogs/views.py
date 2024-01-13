from rest_framework import generics
from .models import Dialog
from .serializers import DialogSerializer


class DialogListView(generics.ListAPIView):
    serializer_class = DialogSerializer

    def get_queryset(self):
        amount = self.kwargs.get('amount', 10)

        queryset = Dialog.objects.all()

        queryset = queryset.order_by('?')

        return queryset[:amount]


class DialogCreateView(generics.CreateAPIView):
    queryset = Dialog.objects.all()
    serializer_class = DialogSerializer

