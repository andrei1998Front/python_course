class BasicWord:

    def __init__(self, original_word, valid_words):
        self.original_word = original_word
        self.valid_words = valid_words

    def __repr__(self):
        return f'Исходное слово: {self.original_word}.\nДопустимые слова:{self.concatenate_valid_words()}'

    def concatenate_valid_words(self):
        """ Список допустимых слов в виде строки """
        return ', '.join(self.valid_words)

    def check_user_input(self, user_input):
        """ Проверка введенного слова на допустимость """

        if user_input in self.valid_words:
            return True
        else:
            return False

    def calc_count_words(self):
        """Возврат количества возможных слов"""
        return len(self.valid_words)
