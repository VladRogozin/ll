from rest_framework import generics
from .models import Word
from .serializers import WordSerializer
from django.http import JsonResponse


class WordListView(generics.ListAPIView):
    serializer_class = WordSerializer

    def get_queryset(self):
        level = self.kwargs.get('level', None)
        amount = self.kwargs.get('amount', 10)

        queryset = Word.objects.all()

        if level and level != 'None':
            queryset = queryset.filter(word_level=level)

        if not queryset.exists():
            # Если нет данных, возвращаем JSON-ответ с информацией
            return JsonResponse({"detail": "No matching data found"}, status=404)

        queryset = queryset.order_by('?')

        return queryset[:amount]


class WordCreateView(generics.CreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

