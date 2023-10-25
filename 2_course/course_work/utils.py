import json
import re
import os

def check_bookmark(post_id, bookmarks):
    for bookmark in bookmarks:
        if bookmark["post_id"] == post_id:
            return True

    return False


def check_len(checked_list):
    if len(checked_list) > 0:
        return checked_list
    else:
        raise ValueError


def search_tags(text):
    return re.findall(r'#\w+', text)


def extract_text(tag):
    return re.search(r'\w+', tag)[0].lower()

def install_links(tags):
    links = []
    for tag in tags:

        link_text = f'<a href="/tag/{extract_text(tag)}" class="item__tag">{tag}</a>'
        link_pattern = f'{tag}(?![а-яА-Яa-zA-Z0-9])'
        links.append({"text": link_text, "pattern": link_pattern})

    return links


def replace_tags(text):
    tags = search_tags(text)
    links = install_links(tags)

    for link in links:
        text = re.sub(link["pattern"], link["text"], text)

    return text


def get_posts_all(posts_path, bookmarks_path):
    with open(posts_path, 'r', encoding='utf-8') as data_file:
        posts = json.load(data_file)
        bookmarks = get_bookmarks_all(bookmarks_path)
        for post in posts:
            content = post["content"]
            post["content"] = replace_tags(content)
            post["have_bookmark"] = check_bookmark(post["pk"], bookmarks)

    return check_len(posts)


def get_bookmarks_all(path):
    with open(path, 'r') as data_file:
        bookmarks = json.load(data_file)

    return bookmarks


def get_all_comments(path):

    with open(path, 'r', encoding='utf-8') as data_file:
        comments = json.load(data_file)

    return check_len(comments)


def check_post(post_id, posts):
    for post in posts:
        if post['pk'] == post_id:
            return True

    return False


def get_comments_by_post_id(post_id, comments_path, posts):

    if check_post(post_id, posts) is False:
        raise ValueError

    comments = get_all_comments(comments_path)

    comments_post = []

    for comment in comments:
        if comment["post_id"] == post_id:
            comments_post.append(comment)

    return check_len(comments_post)


def get_posts_by_user(user_name, posts):
    user_posts = []

    for post in posts:
        if user_name.lower() == post['poster_name'].lower():
            user_posts.append(post)

    return check_len(user_posts)


def search_for_posts(query, posts):
    posts_by_query = []

    for post in posts:
        if query.lower() in post['content'].lower():
            posts_by_query.append(post)

    return posts_by_query


def get_post_by_pk(pk, posts):
    for post in posts:
        if post['pk'] == pk:
            return post

    raise ValueError


def get_posts_by_tag(tag, posts):
    posts_by_tag = []
    search_pattern = f'#{tag}(?![а-яА-Яa-zA-Z0-9])'

    for post in posts:
        result = re.search(search_pattern, post['content'])
        if result:
            posts_by_tag.append(post)
        else:
            continue

    return posts_by_tag


def write_json(list_for_json, path):
    if os.path.exists(path) is False:
        raise FileNotFoundError

    list_json = json.dumps(list_for_json, ensure_ascii=False)

    with open(path, 'w', encoding='utf-8') as data_file:
        data_file.write(list_json)


def add_bookmark(path, post_id, bookmarks, posts):
    if check_post(post_id, posts) is False:
        raise ValueError

    bookmarks.append({"post_id": post_id})

    new_bookmarks = []
    [new_bookmarks.append(x) for x in bookmarks if x not in new_bookmarks]
    bookmarks = new_bookmarks

    write_json(bookmarks, path)


def delete_bookmark(path, post_id, bookmarks):
    bookmarks_count = len(bookmarks)

    for i in range(bookmarks_count):
        if bookmarks[i]['post_id'] == post_id:
            del bookmarks[i]
            write_json(bookmarks, path)
            return


def get_posts_by_bookmarks(posts, bookmarks):
    post_by_bookmarks = []

    for post in posts:
        for bookmark in bookmarks:
            if post['pk'] == bookmark['post_id']:
                post_by_bookmarks.append(post)

    return post_by_bookmarks
