def get_errors(*errors_arr):
    """ Задача на обработку ошибок """
    errors = {
        "out": "Вы вышли из системы",
        "noaccess": "У вас нет доступа в этот раздел",
        "unknown": "Неизвестная ошибка",
        "timeout": "Система долго отвечает",
        "robot": "Ваши действия похожи на робота"
    }

    arr_for_return = []

    for error in errors_arr:

        if error in errors:
            err_item = errors[error]

            arr_for_return.append(err_item)

    return arr_for_return


def draw_carpet_line(w, w_border, h, border, body, cell):
    """ Задача на ковер (псевдографика) """
    left_border = w_border * border + w_border * body
    right_border = w_border * body + w_border * border

    for header_height in range(h):
        print(left_border + cell * w + right_border)


def get_letter(list_, letter):
    """" Буква по индексу (для кодирования)  """

    max_idx = len(list_) - 1
    letter_index = list_.index(letter)

    if letter_index < max_idx:
        return list_[letter_index + 1]
    else:
        return list_[0]


def shift_encode(string):
    """ Кодировка сдвигом """

    ALPHABET_RU = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    ALPHABET_RU_UPPER = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    ALPHABET_EN = 'abcdefghijklmnopqrstuvwxyz'
    ALPHABET_EN_UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ALPHABET_ALL = ALPHABET_RU + ALPHABET_RU_UPPER + ALPHABET_EN + ALPHABET_EN_UPPER

    encoded_list = []

    for letter in string:
        if letter not in ALPHABET_ALL:
            encoded_list.append(letter)
        elif letter in ALPHABET_RU:
            encoded_list.append(get_letter(ALPHABET_RU, letter))
        elif letter in ALPHABET_RU_UPPER:
            encoded_list.append(get_letter(ALPHABET_RU_UPPER, letter))
        elif letter in ALPHABET_EN:
            encoded_list.append(get_letter(ALPHABET_EN, letter))
        elif letter in ALPHABET_EN_UPPER:
            encoded_list.append(get_letter(ALPHABET_EN_UPPER, letter))

    return "".join(encoded_list)


def get_letter_decoded(list_, letter):
    max_idx = len(list_) - 1
    letter_index = list_.index(letter)

    if letter_index == 0:
        return list_[max_idx]
    elif letter_index == max_idx:
        return list_[0]
    else:
        return list_[letter_index - 1]


def shift_decode(string):
    """ Расшифрока строки """

    ALPHABET_RU = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    ALPHABET_RU_UPPER = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    ALPHABET_EN = 'abcdefghijklmnopqrstuvwxyz'
    ALPHABET_EN_UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ALPHABET_ALL = ALPHABET_RU + ALPHABET_RU_UPPER + ALPHABET_EN + ALPHABET_EN_UPPER

    decoded_list = []

    for letter in string:
        if letter not in ALPHABET_ALL:
            decoded_list.append(letter)
        elif letter in ALPHABET_RU:
            decoded_list.append(get_letter_decoded(ALPHABET_RU, letter))
        elif letter in ALPHABET_RU_UPPER:
            decoded_list.append(get_letter_decoded(ALPHABET_RU_UPPER, letter))
        elif letter in ALPHABET_EN:
            decoded_list.append(get_letter_decoded(ALPHABET_EN, letter))
        elif letter in ALPHABET_EN_UPPER:
            decoded_list.append(get_letter_decoded(ALPHABET_EN_UPPER, letter))

    return "".join(decoded_list)


def draw_carpet(w, h):
    border = "&"
    body = "+"
    carpet_cell = "#"
    border_val = 10
    # header
    draw_carpet_line(w, border_val, border_val, border, body, body)

    draw_carpet_line(w, border_val, h, border, body, carpet_cell)

    # footer
    draw_carpet_line(w, border_val, border_val, border, body, body)


def main():
    print("Задача 1")
    print(get_errors("out", "robot", "1"))

    print("\n")

    print("Задача 2")
    draw_carpet(10, 10)

    print("\n")

    print("Задача 3")

    encoded_str = shift_encode("Я изучаю English")
    decoded_str = shift_decode(encoded_str)

    print(encoded_str)
    print(decoded_str)


main()
