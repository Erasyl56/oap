if len(numbers) < 2:
    print("Қате: Массив ұзындығы 2-ден кем, екінші үлкен элементті анықтау мүмкін емес.")
else:
    # Ең үлкен және екінші үлкенді табу
    first_max = numbers[0]
    second_max = None

    for item in numbers:
        if item > first_max:
            second_max = first_max
            first_max = item
        elif item != first_max and (second_max is None or item > second_max):
            second_max = item

    if second_max is None:
        print("Барлық элементтер бірдей, екінші үлкен элемент жоқ.")
    else:
        print(f"Екінші по величине (үлкен) элемент: {second_max}")
