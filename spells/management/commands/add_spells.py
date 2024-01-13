from django.core.management.base import BaseCommand
from spells.models import Spell


class Command(BaseCommand):
    help = 'Add words to the Fact model'

    def handle(self, *args, **options):
        data_arr = [
          {"Ексклюзивний": ["Exclusive", "Exclusiv", "Excluusive"]},
          {"Підсумок": ["Summation", "Sumation", "Summattion"]},
          {"Диверсифікація": ["Diversification", "Diversificacion", "Diversifcation"]},
          {"Ідентифікація": ["Identification", "Identificacion", "Identifcation"]},
          {"Кореляція": ["Correlation", "Correlacion", "Correlattion"]},
          {"Дефіцит": ["Deficit", "Deficitt", "Defecit"]},
          {"Ескалація": ["Escalation", "Escallation", "Esclation"]},
          {"Легалізація": ["Legalization", "Legalizacion", "Legalizattion"]},
          {"Рекомендація": ["Recommendation", "Recomendacion", "Recomendattion"]},
          {"Модифікація": ["Modification", "Modificacion", "Modifcation"]},
          {"Професіоналізм": ["Professionalism", "Profesionalism", "Proffessionalism"]},
          {"Асоціація": ["Association", "Assosiation", "Associattion"]},
          {"Консолідація": ["Consolidation", "Consolodation", "Consolidattion"]},
          {"Соціалізація": ["Socialization", "Socializacion", "Socializattion"]},
          {"Експлікація": ["Explication", "Explikacion", "Explikattion"]},
          {"Деконструкція": ["Deconstruction", "Deconstruccion", "Deconstruktcion"]},
          {"Легітимізація": ["Legitimization", "Legitimizacion", "Legitimizattion"]},
          {"Стандартизація": ["Standardization", "Standardizacion", "Standardizattion"]},
          {"Екстраполяція": ["Extrapolation", "Extrapollation", "Extrapolation"]},
          {"Інтенсифікація": ["Intensification", "Intensificacion", "Intensificattion"]}
        ]

        for data in data_arr:
            new_instance = Spell(
                word=data,
                level="C1"
            )
            new_instance.save()

        print(len(data_arr))
        self.stdout.write(self.style.SUCCESS('Facts added successfully!'))
