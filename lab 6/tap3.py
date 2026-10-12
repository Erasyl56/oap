def is_passed(score):
    if score < 0 or score > 100:
        return "Қате: 0 мен 100 аралығындағы балл енгізіңіз!"
    return score >= 50

print(is_passed(49))   # False
print(is_passed(50))   # True
print(is_passed(100))  # True
print(is_passed(105))  # Қате хабарламасы
