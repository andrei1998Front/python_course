from utils import *
from config import *


def main():
    questions_dict = load_question(QUESTIONS_PATH)

    count_questions = get_count_question(questions_dict) - 1

    count_answers = 0
    points = 0
    correct = 0
    incorrect = 0

    while count_answers <= count_questions:
        print(show_field(questions_dict))

        user_choice = input("Выберите вопрос:\n")

        category, price = parse_input(user_choice)

        if (
            category not in questions_dict
            or price not in questions_dict[category]
        ):
            print("Такого вопроса нет! Попробуйте ещё раз")
            continue
        elif questions_dict[category][price]["asked"] is True:
            print("Данный вопрос уже был задан! Попробуйте ещё раз")
            continue

        question = questions_dict[category][price]
        right_answer = question["answer"]

        show_question(question)

        user_answer = input().lower()

        if user_answer == right_answer:
            points += int(price)
            correct += 1

            print(f"Верно +{price}. Ваш счет = {points}")
        else:
            points -= int(price)
            incorrect += 1

            print(f"Неверно, на самом деле - {right_answer}. -{price}. Ваш счет = {points}")

        question['asked'] = not question['asked']

        if count_answers == count_questions:
            show_stats(points, correct, incorrect)

        count_answers += 1

    stats_dict = load_question(STATISTICS_PATH)
    gamer_id = get_max_gamer_id(stats_dict)

    stats_dict[f"gamer_{gamer_id}"] = {"points": points, "correct": correct, "incorrect": incorrect}

    save_result_to_file(STATISTICS_PATH, stats_dict)


main()
