class Questions:
    def __init__(self, text, complexity, right_answer):
        """ Инициализатор класса """
        # Константа
        self.MAX_COMPLEXITY = 5

        self.text = text
        self.complexity = self.set_complexity(complexity)
        self.right_answer = right_answer

        # Значения по умолчанию
        self.answered = False
        self.user_answer = None
        self.points = self.get_points()

    def get_points(self):
        """ Возвращает int, количество баллов """
        return self.complexity * 10

    def is_correct(self):
        """Проверка правильности ответа"""
        return self.right_answer.lower() == self.user_answer.lower()

    def build_question(self):
        """Генерация вопроса"""
        return f"Вопрос: {self.text}\nСложность: {self.complexity}/5"

    def set_complexity(self, complexity_str):
        """ Регулировка значения сложности вопроса"""
        complexity = int(complexity_str)

        if complexity < 0:
            return 0
        elif complexity > self.MAX_COMPLEXITY:
            return self.MAX_COMPLEXITY
        else:
            return complexity

    def build_feedback(self):
        """Ответ программы на ответ пользователя"""
        if self.is_correct():
            return f"Ответ верный, получено {self.points} баллов"
        else:
            return f"Ответ неверный, верный ответ {self.right_answer}"


