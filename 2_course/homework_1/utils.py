import requests
from classes.Candidate import Candidate
from config import CANDIDATES_URL


def get_array_from_url():
    """Получение списка кандидатов по ссылке"""
    return requests.get(CANDIDATES_URL).json()


def create_candidate_instance(candidate):
    """Создание экземпляра кандидата"""
    return Candidate(candidate)


def create_candidates_list(candidates):
    """Создание списка кандидатов"""
    candidates_list = []

    for candidate in candidates:
        candidates_list.append(create_candidate_instance(candidate))

    return candidates_list


def get_candidates_list():
    """Передадим готовый список экземпляров класса"""
    array = get_array_from_url()
    return create_candidates_list(array)


def generate_main_page(candidates_list):
    """Вьюшка списка кандидатов"""
    html = []

    for candidate in candidates_list:
        html.append(
            '<pre>\n'
            + f'{candidate.name} -\n'
            + f'{candidate.position}\n'
            + f'{candidate.get_skills_string()}\n'
            + '</pre>'
        )

    return '\n'.join(html)


def search_candidate(candidates, position):
    """Поиск кандидата по позиции"""
    for candidate in candidates:
        if candidate.position == position:
            return candidate


def generate_candidate_page(position, candidates):
    """Вьющка кандидата"""
    candidate = search_candidate(candidates, position)

    return f'<img src="{candidate.picture}"/>\n' \
        '<pre>\n' \
        f'{candidate.name} -\n' \
        f'{candidate.position}\n' \
        f'{candidate.get_skills_string()}\n' \
        '</рге>'


def search_candidates_on_skill(candidates, skill):
    """Поиск кандидата по навыку"""
    candidates_with_skill = []

    for candidate in candidates:
        if skill in candidate.skills:
            candidates_with_skill.append(candidate)

    return candidates_with_skill


def generate_search_result_page(skill, candidates):
    """вьюшка списка найденных по навыку кандидатов"""
    candidates = search_candidates_on_skill(candidates, skill)

    return generate_main_page(candidates)
