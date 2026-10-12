positive_count = 0
negative_count = 0
even_count = 0

for item in numbers:
    if item > 0:
        positive_count += 1
    elif item < 0:
        negative_count += 1
    
    if item % 2 == 0:
        even_count += 1

print(f"Оң сандар саны: {positive_count}")
print(f"Теріс сандар саны: {negative_count}")
print(f"Жұп элементтер саны: {even_count}")
