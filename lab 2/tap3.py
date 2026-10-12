# Секунд санын енгізу
total_seconds = int(input("Тәулік басынан өткен секунд санын енгізіңіз: "))

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"Нәтижесі: {hours} сағат {minutes} минут {seconds} секунд")
