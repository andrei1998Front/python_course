from utils import *

import pytest

post_keys_should_be = {
    "poster_name",
    "poster_avatar",
    "pic",
    "content",
    "views_count",
    "likes_count",
    "pk",
    "have_bookmark"
}

comment_keys_should_be = {
    "post_id",
    "commenter_name",
    "comment",
    "pk"
}

bookmarks_keys_should_be = {
    "post_id"
}

class TestUtils:
    def test_check_bookmark(self, test_config):
        bookmarks = get_bookmarks_all(test_config['bookmarks_path'])

        assert type(bookmarks) == list, 'Возвращаемый тип должен быть списком'
        assert check_bookmark('fff', bookmarks) is False, 'Идентификаторы поста быть только целочисленными значениями'

    def test_search_tags(self):
        tag = 'Привет, это мой новый #tag'
        without_tag = 'А это текст без тега'

        assert search_tags(tag)[0] == '#tag', 'Не обнаружен тэг'
        assert len(search_tags(without_tag)) == 0, 'Обнаружены тэги, там где их нет'

    def test_extract_text(self):
        tag = '#tag'
        without_tag = 'А это текст без тега'

        assert extract_text(tag) == 'tag', 'Не верно извлекается текст тэга'
        assert extract_text(without_tag) == 'а', 'Не верно извлекается текст'

    def test_install_links(self):
        tags = ['#tag', 'A это текст без тега']

        assert type(install_links(tags)) == list, 'Не верно возвращаемый тип данных'
        assert type(install_links(tags)[0]) == dict, 'Не верный тип элемента списка'
        assert install_links(tags)[0]['text'] == '<a href="/tag/tag" class="item__tag">#tag</a>', 'Не верно устанавливается ссылка'
        assert install_links(tags)[0]['pattern'] == '#tag(?![а-яА-Яa-zA-Z0-9])', 'Не верно устанавливается паттерн'
        assert install_links(tags)[1]['text'] == '<a href="/tag/a" class="item__tag">A это текст без тега</a>', 'Не верно устанавливается безтэговая ссылка'
        assert install_links(tags)[1]['pattern'] == 'A это текст без тега(?![а-яА-Яa-zA-Z0-9])', 'Не верно устанавливается безтеговый паттерн'

    def test_replace_tags(self):
        text = '#tag ппп #ggg'

        assert replace_tags(text) == '<a href="/tag/tag" class="item__tag">#tag</a> ппп <a href="/tag/ggg" class="item__tag">#ggg</a>', 'Ссылка не установлена'

    def test_get_posts_all(self, test_config):

        posts = get_posts_all(test_config['posts_path'], test_config['bookmarks_path'])

        assert type(posts) == list, "Неверный тип возвращаемых данных"
        assert set(posts[0].keys()) == post_keys_should_be, "неверный список ключей"

        with pytest.raises(ValueError):
            get_posts_all(test_config["empty_list"], test_config['bookmarks_path'])

    def test_get_all_comments(self, test_config):
        comments = get_all_comments(test_config['comments_path'])

        assert type(comments) == list, "Неверный тип возвращаемых данных"
        assert set(comments[0].keys()) == comment_keys_should_be, "неверный список ключей"

        with pytest.raises(ValueError):
            get_all_comments(test_config["empty_list"])

    def test_get_bookmarks_all(self, test_config):
        bookmarks = get_bookmarks_all(test_config['bookmarks_path'])
        assert type(bookmarks) == list

        if len(bookmarks) > 0:
            assert set(bookmarks[0].keys()) == bookmarks_keys_should_be

    def test_check_post(self, test_config):
        posts = get_posts_all(test_config['posts_path'], test_config['bookmarks_path'])

        assert check_post("1", posts) is False, "Найдет пост с несуществующем ключом"
        assert check_post(1, posts) is True, "Сушествующий пост не найден"

    def test_check_len(self):
        assert check_len([1]) == [1], "Неверно подсчитывается количество элементов"

        with pytest.raises(ValueError):
            check_len([])

    def test_get_comments_by_post_id(self, test_config):
        posts = get_posts_all(test_config['posts_path'], test_config['bookmarks_path'])

        with pytest.raises(ValueError):
            get_comments_by_post_id("1", test_config['comments_path'], posts)

        with pytest.raises(ValueError):
            get_comments_by_post_id(1, test_config['empty_list'], posts)

    def test_get_posts_by_user(self, test_config):
        posts = get_posts_all(test_config['posts_path'], test_config['bookmarks_path'])

        with pytest.raises(ValueError):
            get_posts_by_user("", posts)

    def test_search_for_posts(self, test_config):
        posts = get_posts_all(test_config['posts_path'], test_config['bookmarks_path'])

        assert type(search_for_posts('а', posts)) == list
        assert len(search_for_posts('хуй', posts)) == 0, "Предполагалось, что мата не будет :)"

    def test_get_post_by_pk(self, test_config):
        posts = get_posts_all(test_config['posts_path'], test_config['bookmarks_path'])

        with pytest.raises(ValueError):
            get_post_by_pk("", posts)


    def test_get_posts_by_tag(self, test_config):
        posts = get_posts_all(test_config['posts_path'], test_config['bookmarks_path'])
        tag = 'кот'
        tag_no_result = 'кит'

        assert type(get_posts_by_tag(tag, posts)) == list
        assert len(get_posts_by_tag(tag, posts)) > 0
        assert len(get_posts_by_tag(tag_no_result, posts)) == 0

    def test_write_json(self):
        with pytest.raises(FileNotFoundError):
            write_json([], 'dfgfdg.json')

    def test_add_bookmark(self, test_config):
        posts = get_posts_all(test_config['posts_path'], test_config['bookmarks_path'])
        bookmarks = get_bookmarks_all(test_config['bookmarks_path'])

        with pytest.raises(FileNotFoundError):
            add_bookmark('fff', 1, bookmarks, posts)

        with pytest.raises(ValueError):
            add_bookmark(test_config['bookmarks_path'], 'fff', bookmarks, posts)

    def test_delete_bookmark(self, test_config):
        bookmarks = get_bookmarks_all(test_config['bookmarks_path'])

        if len(bookmarks) > 0:
            with pytest.raises(FileNotFoundError):
                delete_bookmark('fdsf', 1, bookmarks)

    def test_get_posts_by_bookmarks(self, test_config):
        posts = get_posts_all(test_config['posts_path'], test_config['bookmarks_path'])
        bookmarks = get_bookmarks_all(test_config['bookmarks_path'])

        posts_by_bookmarks = get_posts_by_bookmarks(posts, bookmarks)
        assert type(posts_by_bookmarks) == list

        if len(posts_by_bookmarks) > 0:
            assert set(posts_by_bookmarks[0].keys()) == post_keys_should_be
