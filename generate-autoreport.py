import pandas as pd
import random
import string
import os
import configparser

dirname = os.path.dirname(__file__)

config = configparser.ConfigParser()
config.read(os.path.join(dirname, 'config.ini'))

SHOPS = eval(config['Shops-info']['shops'])
CASH = eval(config['Shops-info']['cash'])

d = {
    'посуда': ['тарелка', 'чайник', 'кастрюля', 'чашка'],
    'бытовая химия': ['стиральный порошок', 'зубная паста', 'гель для душа', 'шампунь'],
    'текстиль': ['штора', 'подушка', 'одеяло'],
    'освещение': ['светильник', 'лампочка']
}

category = []
item = []
for k, v in d.items():
  for value in v:
    category.append(k)
    item.append(value)

for i in SHOPS:
  for j in CASH:
    tab = {
        'shop_number': i,
        'cash_number': j,
        'doc_id': [''.join(random.choices(string.ascii_letters + string.digits,k=10)) for _ in range(len(category))],
        'item': item,
        'category': category,
        'amount': [random.randint(0, 50) for _ in range(len(category))],
        'price': [round(random.uniform(100, 3000), 1) for _ in range(len(category))],
        'discount': [random.choice([0, 3, 5]) for _ in range(len(category))]
    }
    report = pd.DataFrame(tab)
    report.to_csv(os.path.join(dirname, f'{i}_{j}.csv'), index=False)