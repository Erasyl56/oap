search_value = int(input("Ізделетін санды енгізіңіз: "))
found_index = -1

for i in range(len(numbers)):
    if numbers[i] == search_value:
        found_index = i
        break  # Табылғаннан кейін циклді тоқтату

if found_index != -1:
    print(f"Сан массивте табылды. Индексі: {found_index}")
else:
    print("Бұл сан массивте жоқ.")
