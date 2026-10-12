# Массивтің бос емес екенін ескерсек (1-тапсырмадағы numbers тізімін қолданамыз)
if len(numbers) > 0:
    total_sum = 0
    max_val = numbers[0]
    min_val = numbers[0]

    for item in numbers:
        total_sum += item
        if item > max_val:
            max_val = item
        if item < min_val:
            min_val = item

    average = total_sum / len(numbers)

    print(f"Элементтер қосындысы: {total_sum}")
    print(f"Максималды элемент: {max_val}")
    print(f"Минималды элемент: {min_val}")
    print(f"Арифметикалық ортасы: {average:.2f}")
else:
    print("Массив бос.")
