total_seconds = int(input("6432: "))

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"{total_seconds} секунд — бұл {hours} сағат {minutes} минут {seconds} секунд.")