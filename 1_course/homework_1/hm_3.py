# Импорт библиотеки случайных чисел

import random

# Список слов для перевода

words = [
    "code",
    "bit bit",
    "list",
    "soul",
    "next"
]

# Список ответов

answers = []

# Азбука морзе

MORSE = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-",
    " ": "/"
}


def morse_encode(sentence):
    """Функция переводящя текст в азбуку морзе"""

    str_ = ""

    # количество букв в слове
    count_letters = len(sentence)
    last_letter_index = count_letters - 1

    for num_letter in range(count_letters):

        letter = sentence[num_letter]

        if num_letter != last_letter_index:
            str_ += MORSE.get(letter, '') + ' '
        else:
            str_ += MORSE.get(letter, '')

    return str_


def get_word():
    """Функция для получения случайного слова из списка"""

    # random.choice - возвращает случайный элемент последовательности
    word = random.choice(words)
    
    return word


def print_statistics(answers_):
    """Вывод статистики ответов"""
    
    count_answer = len(answers_)
    right_answers = sum(answers_)
    wrong_answers = count_answer - sum(answers_)
        
    print(f"Всего задачек: {count_answer}")
    print(f"Отвечено верно: {right_answers}")
    print(f"Отвечено неверно: {wrong_answers}")


def main():
    count_words = len(words)

    # Приветствие
    print("Сегодня мы будем расшифровывать морзянку.")
    input("Нажмите Enter и начнем")

    # запускаем цикл вопросов

    for word_idx in range(count_words):

        random_word = get_word()
        morse_word = morse_encode(random_word)

        answer = input(f"Слово {word_idx + 1} {morse_word} \n").lower()

        if answer == random_word:
            print(f"Верно, {random_word}!")
            answers.append(True)
        else:
            print(f"Нерно, {random_word}!")
            answers.append(False)

    print_statistics(answers)


main()
