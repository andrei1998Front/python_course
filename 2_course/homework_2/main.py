from utils import *
from flask import Flask, render_template
from config import CANDIDATES_PATH

app = Flask(__name__)

candidates = load_candidates_from_json(CANDIDATES_PATH)


@app.route('/')
def main_page():
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:id>')
def candidate_page(id):
    candidate = get_candidate(id)

    return render_template('single.html', candidate=candidate)


@app.route('/search/<name>')
def candidates_page_by_name(name):
    candidates_by_name = get_candidates_by_name(name)
    return render_template('search.html', candidates=candidates_by_name)


@app.route('/skill/<skill>')
def candidates_page_by_skill(skill):
    candidates_by_skill, normal_skill = get_candidates_by_skill(skill)
    return render_template('skill.html', candidates=candidates_by_skill, skill=normal_skill)


if __name__ == '__main__':
    app.run(debug=True)
