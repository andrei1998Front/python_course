from validators import *


def main():
    # Проверка check_pin
    assert check_pin("1239") is True, "error"
    assert check_pin("3333") is False, "error"
    assert check_pin("1234") is False, "error"
    assert check_pin("00011") is False, "error"
    assert check_pin("8765") is True, "error"

    # Проверка check_pass
    assert check_pass("secretd00r") is True, "error"
    assert check_pass("huskyeye5") is True, "error"
    assert check_pass("secret") is False, "error"
    assert check_pass("fh43j_!") is False, "error"
    assert check_pass("m3wm3wm3w") is True, "error"

    # Проверка check_mail
    assert check_mail("local@skypro") is False, "error"
    assert check_mail("you(at)sky.pro") is False, "error"
    assert check_mail("me@sky.pro") is True, "error"
    assert check_mail("@lizaveta") is False, "error"
    assert check_mail("alarm@gmail.com") is True, "error"

    # Проверка check_name
    assert check_name("Данил") is True, "error"
    assert check_name("Р_и_т_а") is False, "error"
    assert check_name("К0нстантин") is False, "error"
    assert check_name("А Ф") is True, "error"
    assert check_name("Елена") is True, "error"


main()
