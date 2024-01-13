from django.core.management.base import BaseCommand
from news.models import New


class Command(BaseCommand):
    help = 'Add words to the Fact model'

    def handle(self, *args, **options):
        data_arr = []

        for data in data_arr:
            new_instance = New(
                title=data["title"],
                english_news=data["news"]["english"],
                ukrainian_news=data["news"]["ukrainian"],
                keywords=data["keywords"],
                questions=data["questions"]
            )
            new_instance.save()

        print(len(data_arr))
        self.stdout.write(self.style.SUCCESS('Facts added successfully!'))








