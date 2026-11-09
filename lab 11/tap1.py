# lab11_var4.py - 4-нұсқа: Спорт клубы

print("--- А тапсырмасы: Бірегей мәндер және қайталанулар ---")
sports = [
    "Футбол", "Бокс", "Шахмат", "Футбол", 
    "Баскетбол", "Бокс", "Жүзу", "Шахмат", 
    "Футбол", "Волейбол"
]

unique_sports = set(sports)
total_count = len(sports)
unique_count = len(unique_sports)
duplicate_count = total_count - unique_count

print(f"Бастапқы тізім: {sports}")
print(f"Бірегей спорт түрлері жиыны: {unique_sports}")
print(f"Жалпы элементтер саны: {total_count}")
print(f"Бірегей элементтер саны: {unique_count}")
print(f"Қайталанатын элементтер саны: {duplicate_count}\n")


print("--- Ә тапсырмасы: Жиіліктік талдау ---")
frequency = {}
for sport in sports:
    frequency[sport] = frequency.get(sport, 0) + 1

print("Спорт түрлерінің кездесу жиілігі:", frequency)

# Ең жиі кездесетін спорт түрін табу
max_freq = max(frequency.values())
most_common = [s for s, count in frequency.items() if count == max_freq]
print(f"Ең жиі кездесетін спорт түрі(ндері): {most_common} ({max_freq} рет)\n")


print("--- Б тапсырмасы: Сөздіктер тізімін өңдеу ---")
members_records = [
    {"аты": "Бекжан", "спорт түрі": "Футбол", "жасы": 19},
    {"аты": "Айдын", "спорт түрі": "Шахмат", "жасы": 16},
    {"аты": "Ержан", "спорт түрі": "Бокс", "жасы": 21},
    {"аты": "Мадина", "спорт түрі": "Жүзу", "жасы": 17}
]

# 1. Шарт бойынша іріктеу («18 жастан асқан қатысушылар»)
print("18 жастан асқан қатысушылар:")
adult_members = [m for m in members_records if m["жасы"] > 18]
for m in adult_members:
    print(f"- {m['аты']}: {m['спорт түрі']} ({m['жасы']} жаста)")

# 2. Бір жазбаның бір өрісін өзгерту (мысалы, Айдынның жасын жаңарту)
print("\nМәліметтерді жаңартуға дейін (Айдын):")
print(members_records[1])

members_records[1]["жасы"] = 17  # Жасын өзгерту

print("Мәліметтерді жаңартудан кейін:")
print(members_records[1])


print("\n--- В тапсырмасы: Арнайы жағдайларды тексеру ---")
def analyze_data(data_list):
    if not data_list:
        return "Тізім бос", {}, 0
    unique_set = set(data_list)
    freq = {}
    for item in data_list:
        freq[item] = freq.get(item, 0) + 1
    return unique_set, freq, len(data_list) - len(unique_set)

# 1. Бос тізім
print("Бос тізім нәтижесі:", analyze_data([]))

# 2. Қайталанусыз тізім
print("Қайталанусыз тізім нәтижесі:", analyze_data(["Футбол", "Бокс", "Шахмат"]))

# 3. Барлық мәндері бірдей тізім
print("Барлық мәні бірдей тізім нәтижесі:", analyze_data(["Футбол", "Футбол", "Футбол"]))
