# Үш нақты санды енгізу
num1 = float(input("Бірінші санды енгізіңіз: "))
num2 = float(input("Екінші санды енгізіңіз: "))
num3 = float(input("Үшінші санды енгізіңіз: "))

# Есептеулер
total_sum = num1 + num2 + num3
average = total_sum / 3
product = num1 * num2 * num3
square_first = num1 ** 2

# Нәтижелерді шығару
print(f"Қосындысы: {total_sum:.2f}")
print(f"Арифметикалық ортасы: {average:.2f}")
print(f"Көбейтіндісі: {product:.2f}")
print(f"Бірінші санның квадраты: {square_first:.2f}")
