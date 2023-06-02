def get_cost_of_coffee(number_of_coffee, price_per_coffee):
    total_price = 0
    cups_until_free = 8
    while number_of_coffee != 0:
        if cups_until_free == 0:
            cups_until_free = 8
            number_of_coffee -= 1
        else:
            total_price += price_per_coffee
            number_of_coffee -= 1
            cups_until_free -= 1
    return total_price


