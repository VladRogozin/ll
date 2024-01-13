from django.core.management.base import BaseCommand
from facts.models import Fact


class Command(BaseCommand):
    help = 'Add words to the Fact model'

    def handle(self, *args, **options):
        facts_data = [
            {
                "fact": {
                    "english": "The first aeroplane flew on December 17, 1903.",
                    "ukrainian": "Перший літак полетів 17 грудня 1903 року."
                },
                "words": {
                    "ukrainian": ["Перший", "Літак", "Полетів", "Грудень",],
                    "english": ["First", "Aeroplane", "Flew", "December",]
                }
            },

            {
                "fact": {
                    "english": "Venus is the only planet to spin clockwise.",
                    "ukrainian": "Венера - єдина планета, яка обертається за годинниковою стрілкою."
                },
                "words": {
                    "ukrainian": ["Венера", "Єдина", "Планета", "Обертатися","Годинниковa Стрілка"],
                    "english": ["Venus", "Is Only", "Planet", "Spin", "Clockwise"]
                }
            },

            {
                "fact": {
                    "english": "Nutmeg is a hallucinogen.",
                    "ukrainian": "Горіх мускатний - галюциноген."
                },
                "words": {
                    "ukrainian": ["Горіх Мускатний", "Галюциноген"],
                    "english": ["Nutmeg", "Hallucinogen"]
                }
            },

            {
                "fact": {
                    "english": "Competitive art used to be an Olympic sport.",
                    "ukrainian": "Конкурсне мистецтво колись було олімпійським видом спорту."
                },
                "words": {
                    "ukrainian": ["Конкурсний", "Мистецтво", "Олімпійський", "Спорт"],
                    "english": ["Competitive", "Art", "Olympic", "Sport"]
                }
            },

            {
                "fact": {
                    "english": "A chef's hat has 100 pleats.",
                    "ukrainian": "Кулінарна шапка має 100 складок."
                },
                "words": {
                    "ukrainian": ["Кухар", "Шапка", "Складка"],
                    "english": ["Chef's", "Hat", "Pleats"]
                }
            },

            {
                "fact": {
                    "english": "In 2014, there was a Tinder match in Antarctica.",
                    "ukrainian": "У 2014 році в Антарктиці була пара на Tinder."
                },
                "words": {
                    "ukrainian": ["Бути", "Tinder", "З 'єднана","Антарктика"],
                    "english": ["Was", "Tinder", "Match", "Antarctica"]
                }
            },

            {
                "fact": {
                    "english": "The Spanish national anthem has no words.",
                    "ukrainian": "У іспанському національному гімні немає слів."
                },
                "words": {
                    "ukrainian": ["Іспанський", "Національний", "Гімн", "Слово"],
                    "english": ["Spanish", "National", "Anthem", "Words"]
                }
            },
        ]

        for fact_data in facts_data:
            fact_instance = Fact(
                fact_english=fact_data["fact"]["english"],
                fact_ukrainian=fact_data["fact"]["ukrainian"],
                words=fact_data["words"],
                word_level="A2"  # Установите уровень слова по вашему усмотрению
            )
            fact_instance.save()

        print(len(facts_data))
        self.stdout.write(self.style.SUCCESS('Facts added successfully!'))








