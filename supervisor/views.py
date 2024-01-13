from random import choice, choices
from django.forms.models import model_to_dict
from django.http import JsonResponse
from facts.models import Fact
from news.models import New
from quotes.models import Quote
from spells.models import Spell
from dialogs.models import Dialog

def random_data_view(request, amount):
    data_list = []

    for _ in range(amount):

        model = get_random_model()
        if model == "guess_game":
            print("guess_game")
            data_list.append({"type": "guess_game"})
        else:
            random_object = get_random_object(model)
            model_name = model.__name__.lower()

            # Добавляем новое поле "type" в данные
            random_object["type"] = model_name
            data_list.append(random_object)

    return JsonResponse(data_list, safe=False)


def get_random_model():
    # 54 3 60 127 11
    models = [Fact, New, Quote, Spell, Dialog, "guess_game"]
    weights = [0.24, 0.05, 0.25, 0.45, 0.1, 0.03]  # Пример весов, сумма должна быть равна 1.0
    selected_model = choices(models, weights)[0]
    return selected_model


def get_random_object(model):
    count = model.objects.count()
    if count > 0:
        random_object = model.objects.order_by('?').first()
        data = model_to_dict(random_object)

        return data

    return {}




