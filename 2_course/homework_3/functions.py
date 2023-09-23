import json
from config import *

__posts_data = []


def get_posts_from_json():
    try:
        with open(POSTS_PATH, "r", encoding="utf-8") as posts:
            global __posts_data
            posts_arr = json.load(posts)

            for post in posts_arr:
                __posts_data.append(post)
    finally:
        return __posts_data


def search_posts(string_for_search):
    string_for_search = string_for_search.lower()
    found_posts = []

    for post in __posts_data:
        if string_for_search in post["content"].lower():
            found_posts.append(post)

    return found_posts


def upload_post(post):
    global __posts_data
    __posts_data.append(post)

    with open(POSTS_PATH, 'w') as posts:
        json.dump(__posts_data, posts, ensure_ascii=False)


def check_extension(filename):
    extension = filename.split('.')[-1]
    print(extension)
    if extension in ALLOW_EXTENSIONS:
        return True

    else:
        return False


def save_form_result(pic, text):
    if pic and check_extension(pic.filename):
        path_to_save = f".{UPLOAD_FOLDER}/{pic.filename}"
        post = {"pic": path_to_save, "content": text}

        pic.save(path_to_save)
        upload_post(post)

        return post
    else:
        raise FileExistsError("Файла не существует или загружен файл неверного расширения")
