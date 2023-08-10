def check_pin(pin):
    """ Проверка пин-кода """

    pin_len = len(pin)

    if (
        pin_len != 4
        or pin == '1234'
    ):
        return False

    for num in pin:
        if pin.isdigit() is False:
            return False
        if pin.count(num) == 4:
            return False

    return True


def check_pass(pas):
    """ Проверка пароля """

    ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz"
    pas_lower = pas.lower()
    pass_len = len(pas_lower)
    check_symbol = False
    check_num = False

    for sym in pas_lower:
        if sym.isdigit():
            check_num = not check_num
            break
    for sym in pas_lower:
        if sym in ALPHABET:
            check_symbol = not check_symbol
            break

    if (
        pass_len >= 8
        and check_symbol
        and check_num
    ):
        return True
    else:
        return False


def check_mail(mail):
    """ Проверка почты """
    if "@" in mail and "." in mail:
        return True
    else:
        return False


def check_name(name):
    """ Проверка имени """
    name_lower = name.lower()
    ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя "

    for sym in name_lower:
        if sym not in ALPHABET:
            return False

    return True
