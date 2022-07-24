

# noinspection PyUnusedLocal
# skus = unicode string
from sre_constants import CHCODES


def checkout(skus):
    price_table = {
        'A': {1: 50, 3: 130, 5: 200},
        'B': {1: 30, 2: 45},
        'C': {1: 20},
        'D': {1: 15},
        'E': {1: 40},
        'F': {1: 10},
        'G': {1: 20},
        'H': {1: 10, 5: 45, 10: 80},
        'I': {1: 35},
        'J': {1: 60},
        'K': {1: 80, 2: 150},
        'L': {1: 90},
        'M': {1: 15},
        'N': {1: 40},
        'O': {1: 10},
        'P': {1: 50, 5: 200},
        'Q': {1: 30, 3: 80},
        'R': {1: 50},
        'S': {1: 30},
        'T': {1: 20},
        'U': {1: 40},
        'V': {1: 50, 2: 90, 3: 130},
        'W': {1: 20},
        'X': {1: 90},
        'Y': {1: 10},
        'Z': {1: 50}
    }
    order = {k: 0 for k in price_table.keys()}
    multi_products = {
        'E': {2: 'B'},
        'F': {3: 'F'},
        'N': {3: 'M'},
        'R': {3: 'Q'},
        'U': {4: 'U'}}
    i = 0
    total = 0

    while i < len(skus):
        if skus[i] not in price_table:
            return -1
        order[skus[i]] += 1
        i += 1

    for item, offer in multi_products.items():
        for unit, second_item in offer.items():
            order[second_item] = max(0,
                                     order[second_item] - (order[item]//unit))

    for item, units in order.items():
        for unit, price in dict(sorted(
                price_table[item].items(), key=lambda kv: kv[1], reverse=True)).items():
            total += ((order[item]//unit) * price)
            order[item] = order[item] % unit
    return total



