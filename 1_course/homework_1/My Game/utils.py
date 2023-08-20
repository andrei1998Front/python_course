import json


def load_question(path):
    """ Получение списка вопросов из файла """
    with open(path, encoding="utf-8") as questions_file:
        questions = json.load(questions_file)

        return questions


def get_count_question(questions):
    count_questions = 0

    for category in questions:
        count_questions += len(questions[category])

    return count_questions


def show_field(questions):
    field = []
    """ Вывод игрового поля """
    for category, category_item in questions.items():
        field_line = []

        field_line.append(category)

        for price, question in category_item.items():
            if question["asked"]:
                field_line.append("   ")
            else:
                field_line.append(price)

        field.append(" ".join(field_line))

    return "\n".join(field)


def parse_input(input):
    """ Делит ввод пользователя на категорию и число """
    input_arr = []
    error_cartage = ("Error", "Error")

    if " " in input:
        for item in input.split():
            input_arr.append(item)
    else:
        return error_cartage

    if len(input_arr) != 2:
        return error_cartage
    else:
        return input_arr[0], input_arr[1]


def show_question(question):
    """ Вывод вопроса """
    print(f"Слово {question['question']} в переводе означает...")


def show_stats(points, correct, incorrect):
    """ Вывод статистики """

    print("У нас закончились вопросы!\n")
    print(f"Ваш счет: {points}")
    print(f"Верных ответов: {correct}")
    print(f"Неверных ответов: {incorrect}")


def get_max_gamer_id(stats_dict):
    """ Создание айди игрока """

    gamer_nums = []

    for key in stats_dict.keys():
        gamer_nums.append(int(key[-1]))

    return max(gamer_nums) + 1


def save_result_to_file(path, stats_dict):
    """ Запись статистики в файл """

    stats_json = json.dumps(stats_dict)

    with open(path, 'w') as stats_file:
        stats_file.write(stats_json)
