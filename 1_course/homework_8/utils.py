import requests
from Questions import Questions


def get_questions_from_url(path='https://www.jsonkeeper.com/b/0L53'):
    """ Получим список вопросов из юрл"""

    response = requests.get(path)

    if response.status_code == 200:
        questions = response.json()
    else:
        questions = ["Error"]

    return questions


def create_questions_list(questions):
    """ Обработаем полученный список вопросов """
    if questions[0] == "Error":
        return questions[0]

    count_question = len(questions)

    for question in range(count_question):
        questions[question] = Questions(questions[question]["q"], questions[question]["d"], questions[question]["a"])

    return questions


def calc_stats(questions):
    count_questions = len(questions)
    count_right_answers = 0
    points = 0

    for question in questions:
        if question.is_correct():
            count_right_answers += 1
            points += question.points

    return count_right_answers, points, questions


def print_stats(questions):
    """ Вывод статистики """

    count_right_answers, points, count_questions = calc_stats(questions)

    print("Вот и всё!")
    print(f"Отвечено {count_right_answers} из {count_questions}")
    print(f"Набрано баллов {points}")
