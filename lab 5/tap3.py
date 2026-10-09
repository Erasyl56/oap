massiv = [5, -3, 8, -2, 10, 7]

on = 0
teris = 0
zhup = 0

for san in massiv:
    if san > 0:
        on += 1

    if san < 0:
        teris += 1

    if san % 2 == 0:
        zhup += 1

print("Оң сандар саны:", on)
print("Теріс сандар саны:", teris)
print("Жұп сандар саны:", zhup)