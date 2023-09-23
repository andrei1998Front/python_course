import json

__data = []


def load_candidates_from_json(path):
    with open(path, 'r', encoding='utf-8') as file:
        global __data
        __data = json.load(file)

    return __data


def get_candidate(candidate_id):
    for candidate in __data:
        if candidate["id"] == candidate_id:
            return candidate


def normalisation_name(name):
    """Убираем нижнее подчеркивание и приводим к нижнему регистру строку для поиска"""
    if '_' in name:
        return ' '.join(name.split('_')).lower()

    return name.lower()


def get_candidates_by_name(candidate_name):
    normal_name = normalisation_name(candidate_name)

    return [candidate for candidate in __data if normal_name in candidate["name"].lower()]


def get_candidates_by_skill(skill_name):
    normal_name = normalisation_name(skill_name)

    return [candidate for candidate in __data if normal_name in candidate["skills"].lower()], normal_name
