

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    item_price = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
    order = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    num_item_offer = {'A': 3, 'B': 2}
    multi_price = {'A': 130, 'B': 45}
    i = 0
    total = 0

    while i < len(skus):
        if skus[i] not in item_price:
            return -1
        order[skus[i]] += 1
        i += 1

    for item, unit in order.items():
        if item not in multi_price:
            total += (unit*item_price[item])
        else:
            discounted = (unit//num_item_offer[item])*multi_price[item]
            non_discounted = (unit % num_item_offer[item])*item_price[item]
            total += (discounted + non_discounted)

    return total


print(checkout(""))
print(checkout("A"))
print(checkout("B"))
print(checkout("AxA"))
print(checkout("AAA"))
print(checkout("AAAA"))



