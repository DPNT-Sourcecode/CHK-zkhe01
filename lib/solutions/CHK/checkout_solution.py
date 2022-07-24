

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
    num_item_offer = {'A': 3, 'B': 2}
    multi_price = {'A': 130, 'B': 45}
    i = 0
    total = 0
    while i < len(skus):
        units = 0
        while skus[i].isdigit():
            units = (units*10) + int(skus[i])
            i += 1

        item = skus[i]
        if item not in multi_price:
            total += (units*prices[item])
        else:
            discounted = (units//num_item_offer[item])*multi_price[item]
            non_discounted = (units % num_item_offer[item])*prices[item]
            total += (discounted + non_discounted)

        i += 1

    return total


print(checkout("1A2B3C1D"))

