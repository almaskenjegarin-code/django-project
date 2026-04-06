# -*- coding: utf-8 -*-
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from sorting.models import Category, SortingRule

c1, _ = Category.objects.get_or_create(name='Пластик', icon_class='bi-cup-straw', order=1)
c2, _ = Category.objects.get_or_create(name='Макулатура', icon_class='bi-newspaper', order=2)
c3, _ = Category.objects.get_or_create(name='Стекло', icon_class='bi-cup-hot', order=3)
c4, _ = Category.objects.get_or_create(name='Электроника', icon_class='bi-plug', order=4)

SortingRule.objects.get_or_create(category=c1, title='Пластиковые бутылки (PET)', description='Смять, снять крышку (сдается отдельно).', is_recyclable=True)
SortingRule.objects.get_or_create(category=c1, title='Одноразовая посуда (PS, PVC)', description='Не принимается в большинстве пунктов.', is_recyclable=False)
SortingRule.objects.get_or_create(category=c2, title='Офисная бумага, картон', description='Очистить от скотча и скрепок.', is_recyclable=True)
SortingRule.objects.get_or_create(category=c3, title='Бутылки и банки', description='Сполоснуть, снять крышки.', is_recyclable=True)

print("Данные успешно добавлены!")
