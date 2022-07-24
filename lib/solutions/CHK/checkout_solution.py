

# noinspection PyUnusedLocal
# skus = unicode string
from sre_constants import CHCODES


def checkout(skus):
    item_price = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10}
    order = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0}
    num_item_offer = {'A': {5, 3}, 'B': 2}
    multi_products = {'E': {2: 'B'}, 'F': {3: 'F'}}
    multi_price = {'A': {5: 200, 3: 130}, 'B': 45}
    i = 0
    total = 0

    while i < len(skus):
        if skus[i] not in item_price:
            return -1
        order[skus[i]] += 1
        i += 1

    for item, offer in multi_products.items():
        for unit, second_item in offer.items():
            print(item)
            print(second_item)
            print(unit)
            order[second_item] = max(0,
                                     order[second_item] - (order[item]//unit))

    print(order)
    # order['B'] -= (order['E']//2)
    # if order['B'] < 0:
    #     order['B'] = 0

    # order['F'] -= (order['F']//3)

    for item, unit in order.items():
        if item not in multi_price:
            total += (unit*item_price[item])
        else:
            if item == 'E':
                total += unit*item_price[item]
            elif item == 'B':
                discounted = (unit//num_item_offer[item])*multi_price[item]
                non_discounted = (unit % num_item_offer[item])*item_price[item]
                total += (discounted + non_discounted)
            elif item == 'A':
                discounted = (unit//5)*200
                unit = unit % 5
                discounted += (unit//3)*130
                unit = unit % 3
                non_discounted = unit * item_price[item]
                total += (discounted + non_discounted)

    return total


print(checkout("AAAAA"))
print(checkout("AAAAAEEB"))
print(checkout("AAAAAEEBBB"))
print(checkout("AAAAAFFF"))


