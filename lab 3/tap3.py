ball = int(input("70: "))

if ball < 0 or ball > 100:
    print("Қате! Балл 0 мен 100 аралығында болуы керек.")
elif ball >= 90:
    print("Баға: A")
elif ball >= 75:
    print("Баға: B")
elif ball >= 60:
    print("Баға: C")
else:
    print("Баға: D")