from flask import Flask
from utils import *


def main():
    app = Flask(__name__)

    candidates = get_candidates_list()

    @app.route('/')
    def main_page():
        return generate_main_page(candidates)

    @app.route('/candidates/<int:position>')
    def candidate_page(position):
        return generate_candidate_page(position, candidates)

    @app.route('/skills/<skill>')
    def skill_search_result_page(skill):
        return generate_search_result_page(skill, candidates)

    app.run(debug=True)


if __name__ == '__main__':
    main()
