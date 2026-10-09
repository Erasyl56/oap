massiv = [5, 8, 2, 10, 4]

kosyndy = 0
en_ulken = massiv[0]
en_kishi = massiv[0]

for san in massiv:
    kosyndy += san

    if san > en_ulken:
        en_ulken = san

    if san < en_kishi:
        en_kishi = san

orta = kosyndy / len(massiv)

print("Қосынды:", kosyndy)
print("Ең үлкен элемент:", en_ulken)
print("Ең кіші элемент:", en_kishi)
print("Орташа арифметикалық:", orta)