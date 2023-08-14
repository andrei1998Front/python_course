from utils import *
from config import *


def main():
    result = 0

    # Приветствие

    user_name = input("Введите ваше имя\n")

    # Достаем слова из файла и задаем вопросы
    words = read_words_from_file(WORDS_PATH)

    for word in words:
        shuffled_word = shuffle_word(word)

        print(f"Угадайте слово {shuffled_word}")
        answer = input()

        if word == answer:
            print("Верно! Вы получаете 10 очков.")
            result += 10
        else:
            print(f"Неверно! Верный ответ - {word}")

    # Записываем результат

    write_result(HISTORY_PATH, user_name, result)

    # Откроем историю и посчитаем статистику

    stats = calc_statistics(HISTORY_PATH)

    print(f"Всего игр сыграно: {stats.get('count_games')}")
    print(f"Максимальный рекорд: {stats.get('max_result')}")

main()
