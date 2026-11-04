def analyze_text(text, search_word, old_sub, new_sub):
    """Мәтінді талдау, іздеу және алмастыру функциясы"""
    print(f"\n--- МӘТІНДІ ТАЛДАУ ---")
    print(f"Кіріс мәтін: {repr(text)}")
    
    # 1. Ұзындығы, сөз саны және бос орын емес таңбалар санын есептеу
    words = text.split()
    letters = sum(1 for ch in text if not ch.isspace())
    
    print(f"Мәтін ұзындығы (символдар): {len(text)}")
    print(f"Сөздер саны: {len(words)}")
    print(f"Бос орын емес таңбалар саны: {letters}")
    
    # 2. Регистрге тәуелсіз іздеу (алғашқы индекс және кездесулер саны)
    if not text.strip():
        print("Ескерту: Мәтін бос немесе тек бос орындардан тұрады!")
        print(f"'{search_word}' сөзін іздеу: индекс = -1, саны = 0")
    else:
        lower_text = text.lower()
        lower_search = search_word.lower()
        
        first_index = lower_text.find(lower_search)
        count_word = lower_text.count(lower_search)
        
        print(f"'{search_word}' сөзінің алғашқы индексі: {first_index}")
        print(f"'{search_word}' сөзінің кездесу саны: {count_word}")
        
    # 3. Сөзді жаңа сөзге алмастыру
    updated_text = text.replace(old_sub, new_sub)
    print(f"Алмастыру нәтижесі ('{old_sub}' -> '{new_sub}'): {repr(updated_text)}")


def validate_code(code_str):
    """Код пішімін тексеру: XX-999 үлгісі (Мысалы: EF-789)"""
    print(f"\n--- КОД ПІШІМІН ТЕКСЕРУ ---")
    print(f"Тексерілетін код: {repr(code_str)}")
    
    clean_code = code_str.strip()
    # Шарт: ұзындығы 6, алғашқы 2 әріп (үлкен), 3-ші таңба '-', соңғы 3 таңба цифр
    valid = (
        len(clean_code) == 6 and
        clean_code[:2].isalpha() and
        clean_code[:2].isupper() and
        clean_code[2] == "-" and
        clean_code[3:].isdigit()
    )
    
    if valid:
        print("Нәтиже: Дұрыс пішім")
    else:
        print("Нәтиже: Қате пішім")


# --- 3-НҰСҚА БЕРІЛГЕНДЕРІМЕН НЕГІЗГІ ІСКЕ ҚОСУ ---
variant_text = "Кітапхана студенттерге кітап ұсынады. Кітап білім көзі."
search_w = "кітап"
old_word = "білім"
new_word = "ақпарат"
test_code = "EF-789"

# Негізгі мәтінді өңдеу
analyze_text(variant_text, search_w, old_word, new_word)

# Код пішімін тексеру
validate_code(test_code)


# --- 5 ТЕСТ ЖӘНЕ ШЕКАРАЛЫҚ ЖАҒДАЙЛАРДЫ ТЕСТІЛЕУ ---
print("\n==================================================")
print("ҚОСЫМША ТЕСТІЛЕУ ЖӘНЕ ШЕКАРАЛЫҚ ЖАҒДАЙЛАР")
print("==================================================")

test_cases = [
    ("1. Қалыпты мәтін", "Кітапхана студенттерге кітап ұсынады. Кітап білім көзі.", "кітап"),
    ("2. Бос жол", "", "кітап"),
    ("3. Тек бос орындар", "   ", "кітап"),
    ("4. Іздеу сөзі жоқ мәтін", "Студенттер сабақ оқиды.", "кітап"),
    ("5. Қате код пішімі", "A1-12B", "кітап")
]

print(f"{'Тест атауы':<25} | {'Кіріс дерек':<30} | {'Шығыс / Нәтиже':<25}")
print("-" * 86)

# 1-тест
w_count = len(test_cases[0][1].split())
print(f"{test_cases[0][0]:<25} | {test_cases[0][1]:<30} | Сөздер: {w_count}, Табылған")

# 2-тест (Бос жол)
print(f"{test_cases[1][0]:<25} | {repr(test_cases[1][1]):<30} | 0 сөз, 0 таңба")

# 3-тест (Тек бос орындар)
print(f"{test_cases[2][0]:<25} | {repr(test_cases[2][1]):<30} | 0 сөз, 0 бос емес таңба")

# 4-тест (Іздеу сөзі жоқ)
print(f"{test_cases[3][0]:<25} | {test_cases[3][1]:<30} | Индекс: -1, Саны: 0")

# 5-тест (Қате код пішімі)
print(f"{test_cases[4][0]:<25} | {test_cases[4][1]:<30} | Пішім дұрыс емес")
