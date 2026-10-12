text = input("Сандарды бос орынмен енгізіңіз: ")
numbers = [int(x) for x in text.split()]

print("Тізім:", numbers)
print("Элементтер саны:", len(numbers))

if numbers:
    print("Бірінші элемент:", numbers[0])
    print("Соңғы элемент:", numbers[-1])
else:
    print("Тізім бос.")
