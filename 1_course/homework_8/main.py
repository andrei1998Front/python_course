import random
from utils import *
from config import *


def main():
    object_list = get_questions_from_url(QUESTIONS_PATH)
    questions = create_questions_list(object_list)

    if questions[0] == "Error":
        print("Ошибка получения данных! Обратитесь к программисту!")
        return

    count_questions = len(questions) - 1
    answered_questions = 0

    print("Игра начинается!")
    print()

    while answered_questions <= count_questions:
        question = questions[random.randint(0, count_questions)]

        if question.answered:
            continue

        print(question.build_question())

        question.user_answer = input()

        print(question.build_feedback())

        question.answered = not question.answered

        answered_questions += 1

    print_stats(questions)


main()
