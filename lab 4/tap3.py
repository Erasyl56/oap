# n санын енгізу
n = int(input("n санын енгізіңіз (>= 1): "))

total_sum = 0

# range(1, n + 1) арқылы 1-ден n-ге дейін қосу
for i in range(1, n + 1):
    total_sum += i

print(f"1-ден {n}-ге дейінгі сандардың қосындысы: {total_sum}")
