"""В prices.py сделай функции add_tax(price, tax) и discount(price, percent). 
В utils.py сделай format_price(price), которая возвращает, например, "19.99 €".
Внутри prices.py импортируй format_price через relative import.

В __init__.py создай version = "1.0". 
В main.py импортируй package так, чтобы вывести shop.version и воспользоваться функциями. Где-нибудь обязательно используй as.
"""

import mini_shop.shop as shop

import mini_shop.shop.prices as sp

print(shop.version)

price = 100

print(sp.format_price(price))
print(sp.add_tax(price, 0.19))
print(sp.discount(price, percent=0.2))






