import random

result = 0

# Приветствие

user_name = input("Введите ваше имя\n")

# Достаем слова из файла и задаем вопросы

with open("words.txt") as words:
    for word in words:
        word_without_sym = word.strip()
        word_list = list(word_without_sym)

        random.shuffle(word_list)
        shuffle_word = ''.join(word_list)

        print(f"Угадайте слово {shuffle_word}")
        answer = input()

        if word_without_sym == answer:
            print("Верно! Вы получаете 10 очков.")
            result += 10
        else:
            print(f"Неверно! Верный ответ - {word_without_sym}")

# Записываем результат

with open("history.txt", 'a') as history:
    history.write(f"{user_name} {result}\n")

# Откроем историю и посчитаем статистику
count_games = 0
max_result = 0
current_line_idx = 0

with open('history.txt') as history:
    for line in history:
        line_result = line.strip().split(" ")[1]

        if line_result.isdigit() is False:
            print(f"На строке {current_line_idx} содержится ошибка")
            current_line_idx += 1

            continue

        current_result = int(line_result)

        if(max_result < current_result):
            max_result = current_result

        count_games += 1

print(f"Всего игр сыграно: {count_games}")
print(f"Максимальный рекорд: {max_result}")