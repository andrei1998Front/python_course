import random


def read_words_from_file(path):
    """ Читаем слова из файла """

    with open(path) as words:

        words_list = []

        for word in words:
            words_list.append(word.strip())

        return words_list


def shuffle_word(word):
    """ Перемешиваем слово """

    letters_list = list(word)

    random.shuffle(letters_list)

    return "".join(letters_list)


def write_result(path, user_name, result):
    """ Записываем результат в файл """

    with open(path, 'a') as history:
        history.write(f"{user_name} {result}\n")


def calc_statistics(path):
    """ Посчитаем статистику по всем играм """
    count_games = 0
    max_result = 0
    current_line_idx = 0

    with open(path) as history:
        for line in history:
            line_result = line.strip().split(" ")[1]

            if line_result.isdigit() is False:
                print(f"На строке {current_line_idx} содержится ошибка")
                current_line_idx += 1

                continue

            current_result = int(line_result)

            if max_result < current_result:
                max_result = current_result

            count_games += 1

        return {"count_games": count_games, "max_result": max_result}
