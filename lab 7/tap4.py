positive = 0
negative = 0
zeros = 0
even = 0
odd = 0

for value in numbers:
    if value > 0:
        positive += 1
    elif value < 0:
        negative += 1
    else:
        zeros += 1
    
    if value % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"Оң сандар саны: {positive}")
print(f"Теріс сандар саны: {negative}")
print(f"Нөлдер саны: {zeros}")
print(f"Жұп элементтер саны: {even}")
print(f"Тақ элементтер саны: {odd}")
