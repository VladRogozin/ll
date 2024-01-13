from django.urls import path
from .views import *


urlpatterns = [
    path('dialog/<int:amount>/', DialogListView.as_view(), name='dialog-list'),
    path('dialog/create/', DialogCreateView.as_view(), name='dialog-create'),
]

# Зустріч із старим другом:
#
# Планування побачення та обговорення подій.
# На ринку:
#
# Покупка продуктів на ринку.
# Торгівля та узгодження цін.
# Кіно чи театр:
#
# Покупка квитків та обговорення фільму чи вистави.
# Заняття фітнесом:
#
# Реєстрація в тренажерному залі або на групових заняттях.
# На банківській консультації:
#
# Відкриття рахунку чи отримання іншої банківської послуги.
# В агенції нерухомості:
#
# Огляд житла та узгодження деталей оренди чи купівлі.
# На весіллі:
#
# Поради щодо організації весілля та обговорення деталей.
# На природі:
#
# Замовлення кемпінгу чи готелю для відпочинку.
# У театральній студії:
#
# Реєстрація на акторські курси та обговорення п'єси.
# Замовлення їжі доставкою:
#
# Вибір страв та узгодження адреси доставки.
# В автосервісі:
#
# Запис на технічне обслуговування або ремонт автомобіля.
# На виставці мистецтв:
#
# Придбання квитків та обговорення творів мистецтва.
# Зустріч із керівником проекту:
#
# Планування зустрічі та обговорення питань проекту.
# В аеропорту:
#
# Реєстрація на рейс та організація перельоту.
# У ресторані зі спеціальністю:
#
# Обговорення меню та замовлення страв за особливим рецептом.
