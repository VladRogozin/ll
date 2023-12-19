from django.core.management.base import BaseCommand
from guess_game.models import Word  # Замените 'myapp' на имя вашего приложения


class Command(BaseCommand):
    help = 'Add words to the Word model'

    def handle(self, *args, **options):
        words_array = [
    {
        "original_word": "plane",
        "translated_word": "самолет",
        "auxiliary_words": {
            "Fly": "летіти",
            "Airport": "аеропорт",
            "Wings": "крила"
        },
        "word_level": "A1"
    },
    {
        "original_word": "car",
        "translated_word": "автомобіль",
        "auxiliary_words": {
            "Drive": "водити",
            "Road": "дорога",
            "Engine": "двигун"
        },
        "word_level": "A1"
    },
    {
        "original_word": "tram",
        "translated_word": "трамвай",
        "auxiliary_words": {
            "Tracks": "рейки",
            "City": "місто",
            "Stop": "зупинка"
        },
        "word_level": "A1"
    },
    {
        "original_word": "bus",
        "translated_word": "автобус",
        "auxiliary_words": {
            "Passengers": "пасажири",
            "Route": "маршрут",
            "Stop": "зупинка"
        },
        "word_level": "A1"
    },
    {
        "original_word": "train",
        "translated_word": "поїзд",
        "auxiliary_words": {
            "Rails": "рейки",
            "Station": "станція",
            "Journey": "подорож"
        },
        "word_level": "A1"
    },
    {
        "original_word": "ship",
        "translated_word": "корабель",
        "auxiliary_words": {
            "Sail": "плавати",
            "Ocean": "океан",
            "Cruise": "круїз"
        },
        "word_level": "A1"
    },
    {
        "original_word": "bicycle",
        "translated_word": "велосипед",
        "auxiliary_words": {
            "Pedal": "педаль",
            "Ride": "кататися",
            "Cyclist": "велосипедист"
        },
        "word_level": "A1"
    }
]






        for word_data in words_array:
            word_instance = Word(
                original_word=word_data["original_word"],
                translated_word=word_data["translated_word"],
                auxiliary_words=word_data["auxiliary_words"],
                word_level=word_data["word_level"],
            )
            word_instance.save()
        print(len(words_array))
        self.stdout.write(self.style.SUCCESS('Words added successfully!'))










