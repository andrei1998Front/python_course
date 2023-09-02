from config import WORDS_URL
from utils import *


def main():
    player = create_player()
    greet_the_player(player.name)

    word = load_random_word(WORDS_URL)
    conduct_a_survey(word, player)

    print_finall_message(player.calc_count_used_words())


main()
