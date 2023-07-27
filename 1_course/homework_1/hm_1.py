# 1. Приветствие

start = input("Привет! Предлагаю проверить свои знания английского! Наберите ready, чтобы начать!")

if start == "ready":
    user_name =  input("Расскажи как тебя зовут!")

    # 3. Выведем имя пользователя

    print(f"Привет, { user_name }, начинаем тренировку!")

    # 4. Иницилизация вспомогательных переменных
    balls = 0

    questions = ["My name ___ Vova", "I  ___ a coder", "I live ___ Moscow"]
    answers=["is", "am", "in"]
    count_questions = len(questions)

    # 5. Задаем вопросы
    for q in range(count_questions):
        attempt = 1
        while True:
            quest = input(questions[q])

            if quest == answers[q]:
                print("Ответ верный!")

                if attempt == 1:
                    balls += 3

                elif attempt == 2:
                    balls += 2
                
                elif attempt == 3:
                    balls += 1
                break
            else:
                if attempt < 3:
                    attempt += 1 
                    print(f"Осталось попыток: { 4 - attempt }, попробуйте ещё раз!")

                else:
                    print(f"Увы, но нет! Верный ответ: { answers[q] }")
                    break
        

    result_percents = round( ( balls / ( count_questions * 10 ) ) * 100, 2 )
        
    # вывод результатов
    print(
        f"Вот и всё, { user_name }! " + 
        f"Вы ответили на { int(balls / count_questions) } вопросов из { count_questions } верно, " +
        f"это { result_percents } процентов."
    )
else:
    print("Кажется, вы не хотите играть. Очень жаль.")


