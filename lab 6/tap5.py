def subtotal(price, quantity):
    return price * quantity

def discount_amount(amount, rate):
    return amount * rate

def final_price(price, quantity, rate=0):
    amount = subtotal(price, quantity)
    return amount - discount_amount(amount, rate)

# Тестілеу
print(final_price(2500, 3, 0.10))  # 6750.0
print(final_price(1000, 1, 0.0))   # 1000.0 (0% жеңілдік, quantity=1)
print(final_price(500, 4, 1.0))    # 0.0 (100% жеңілдік)
