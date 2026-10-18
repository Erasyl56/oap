
password = input("Құпиясөзді енгізіңіз: ")

score = 0

if len(password) >= 8:
    score += 1

if any(c.isupper() for c in password):
    score += 1

if any(c.islower() for c in password):
    score += 1

if any(c.isdigit() for c in password):
    score += 1

if any(not c.isalnum() for c in password):
    score += 1

if score <= 2:
    level = "Әлсіз"
elif score <= 4:
    level = "Орташа"
else:
    level = "Күшті"

print("Қауіпсіздік деңгейі:", level)
print("Ұпай:", score, "/ 5")
