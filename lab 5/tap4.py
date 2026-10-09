massiv = [5, 8, 2, 10, 4]

izdelgen = int(input("Ізделетін санды енгізіңіз: "))
tabyldy = False

for i in range(len(massiv)):
    if massiv[i] == izdelgen:
        print("Санның индексі:", i)
        tabyldy = True
        break

if not tabyldy:
    print("Мұндай сан массивте жоқ")