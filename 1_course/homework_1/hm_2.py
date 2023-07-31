# Слова, которые нужно угадаывать

easy = {
    "peacock":  "павлин",
    "habit": "привычка",
    "pimple": "прыщ",
    "better":  "лучше",
    "rhythm": "ритм"
}

medium = {
    "clearly":  "павлин",
    "aurora": "Аврора",
    "pontificate": "понтификат",
    "libra":  "весы",
    "observation": "наблюдение"
}

hard = {
    "calamity":  "бедствие",
    "so": "так",
    "bronchitis": "бронхит",
    "malediction":  "проклятие",
    "laundry": "прачечная"
}

# Уровни

levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично"
}

# Словарь ответов

answers = {}

# Выбор уровня сложности

print("Выберите уровень сложности")
selected_level = input("Легкий, средний, сложный")
word = {}

if selected_level.lower() == "легкий":
    word = dict(easy)
elif selected_level.lower() == "средний":
    word = dict(medium)
elif selected_level.lower() == "сложный":
    word = dict(hard)

print("Выбран уровень сложности, мы предложим 5 слов, подберите перевод")
input("Нажмите Enter")
# Задаем вопросы

for term, translation in word.items():
    translation_len = len(translation)
    first_letter = translation[0]
    translation_low = translation.lower()

    answer = input(f"{term}, {translation_len} букв, начинается на {first_letter}...").lower()

    if translation_low == answer:
        print(f"Верно. {term} это {answer}")
        answers[term] = True
    else:
        print(f"Неверно, {term} это {translation}")
        answers[term] = False

# Вывод результатов

count_right_answers = 0

print("Правильно отвечены слова:")
for answer, value in answers.items():
    if value is True:
        print(answer)
        count_right_answers += 1

print("Неправильно отвечены слова:")
for answer, value in answers.items():
    if value is False:
        print(answer)

rang = levels[count_right_answers]

print(f"Ваш ранг:\n{rang}")
