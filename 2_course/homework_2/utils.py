import json


def load_candidates_from_json(path):
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_candidate(candidates, candidate_id):
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            return candidate


def normalisation_name(name):
    """Убираем нижнее подчеркивание и приводим к нижнему регистру строку для поиска"""
    if '_' in name:
        return ' '.join(name.split('_')).lower()

    return name.lower()


def get_candidates_by_name(candidates, candidate_name):
    normal_name = normalisation_name(candidate_name)
    candidates_with_name = []

    for candidate in candidates:
        if normal_name in candidate["name"].lower():
            candidates_with_name.append(candidate)

    return candidates_with_name


def get_candidates_by_skill(candidates, skill_name):
    normal_name = normalisation_name(skill_name)
    candidates_with_skill = []

    for candidate in candidates:
        if normal_name in candidate["skills"].lower():
            candidates_with_skill.append(candidate)

    return candidates_with_skill, normal_name
