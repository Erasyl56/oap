squares = []
positive_even = []

for value in numbers:
    squares.append(value ** 2)
    if value > 0 and value % 2 == 0:
        positive_even.append(value)

print("Квадраттар тізімі:", squares)
print("Оң жұп сандар тізімі:", positive_even)
