import random
import sys

import requests

from BasicWord import BasicWord
from Player import Player


def load_list_from_url(path):
    """Получаем список слов по ссылке"""

    return requests.get(path).json()


def get_random_word(words):
    """Получаем случайное слово из списка"""

    return random.choice(words)


def create_basic_word(word):
    """Создаем экземпляр загаданного слова"""

    return BasicWord(word['word'], word['subword'])


def load_random_word(path='https://www.jsonkeeper.com/b/1SQR'):
    """Создаем экземпляр случайно загаданного слова"""

    words = load_list_from_url(path)
    word = get_random_word(words)
    return create_basic_word(word)


def create_player():
    """Создаем экземпляр игрока"""

    player_name = input("Введите имя игрока:\n")
    return Player(player_name)


def greet_the_player(player_name):
    """Приветствие"""
    print(f"Привет, {player_name}")


def print_start_message(word):
    """Вывод начального сообщения"""
    print(f"Составьте {word.calc_count_words()} слов  из слова {word.original_word}")
    print("Слова должны быть не короче 3 букв")
    print("Чтобы закончить игру, угадайте все слова или напишите \"stop\"")
    print("Поехали, ваше первое слово?")


def check_user_input(user_input, word, player):
    """ Проверка пользовательского ввода """
    if len(user_input) < 3:
        print("Слишком короткое слово")
        return False
    elif user_input == 'stop':
        print_finall_message(player.calc_count_used_words())
        sys.exit()
    elif player.check_double_wording(user_input):
        print("Уже использовано")
        return False
    elif word.check_user_input(user_input):
        print("Верно")
        return True
    print("Неверно")
    return False


def start_survey(word, player):
    """Цикл угадывания слов"""
    count_words = word.calc_count_words()

    while player.calc_count_used_words() < count_words:
        user_input = input().lower()
        if check_user_input(user_input, word, player):
            player.insert_word(user_input)


def print_finall_message(count_used_words):
    """Вывод финального сообщения"""
    print(f"Игра завершена! Вы угадали {count_used_words} слов")

def conduct_a_survey(word: BasicWord, player: Player):
    """Проведения опроса"""
    print_start_message(word)

    start_survey(word, player)
