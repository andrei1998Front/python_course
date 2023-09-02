class Player:

    def __init__(self, name):
        self.name = name
        self.used_words = []

    def __repr__(self):
        return f'Игрок: {self.name}.\nИспользованные слова: {self.concatenate_used_words()}.'

    def concatenate_used_words(self):
        """Список использованных слов в виде строки"""
        return ', '.join(self.used_words)

    def calc_count_used_words(self):
        """ Возврат количества использованных слов """
        return len(self.used_words)

    def insert_word(self, word):
        """Добавление слова в использованные слова"""
        self.used_words.append(word.lower())

    def check_double_wording(self, word):
        if word in self.used_words:
            return True
        else:
            return False
