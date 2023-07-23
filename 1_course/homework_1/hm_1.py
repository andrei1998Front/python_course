# 1. Приветствие
print("Привет! Предлагаю проверить свои знания английского!")

# 2. Считаем имя пользователя
user_name =  input("Расскажи как тебя зовут!")

# 3. Выведем имя пользователя

print(f"Привет, {user_name}, начинаем тренировку!")

# 4. Иницилизация вспомогательных переменных
balls = 0
right_a = 'is'

# 5. Задаем вопросы
quest = input("My name ___ Vova")

if quest == right_a:
    print("Ответ верный!")
    print("Вы получаете 10 баллов!")
    balls += 10
else:
    print("Неправильно.")
    print(f"Правильный ответ: {right_a}")

right_a = 'am'
quest = input("I  ___ a coder")

if quest == right_a:
    print("Ответ верный!")
    print("Вы получаете 10 баллов!")
    balls += 10
else:
    print("Неправильно.")
    print(f"Правильный ответ: {right_a}")
    
right_a = 'in'
quest = input("I live ___ Moscow")

if quest == right_a:
    print("Ответ верный!")
    print("Вы получаете 10 баллов!")
    balls += 10
else:
    print("Неправильно.")
    print(f"Правильный ответ: {right_a}")
    
# вывод результатов
print(f"Вот и всё, {user_name}!")
print(f"Вы ответили на { int(balls / 10) } вопросов из 3 верно.")
print(f"Вы заработали {balls} баллов.")
print(f"Это { (balls / 30) * 100 } процентов.")
