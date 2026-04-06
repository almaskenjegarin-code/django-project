import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from rewards.models import Reward

rewards = [
    {
        'title': 'Эко-шоппер "Чистый Город"', 
        'description': 'Стильная сумка из переработанных материалов. Заменит тысячи пластиковых пакетов!', 
        'cost': 300
    },
    {
        'title': 'Скидка 15% в кофейне "Зерно"', 
        'description': 'Получите промокод на скидку при покупке кофе в свою кружку.', 
        'cost': 150
    },
    {
        'title': 'Многоразовая термокружка', 
        'description': 'Держит тепло до 6 часов. Идеальна для зимних прогулок.', 
        'cost': 500
    }
]

for r_data in rewards:
    Reward.objects.get_or_create(title=r_data['title'], defaults={'description': r_data['description'], 'cost': r_data['cost']})

print("Rewards seeded successfully!")
