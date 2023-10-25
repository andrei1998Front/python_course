import pytest
import run


@pytest.fixture()
def test_client():
    app = run.app
    return app.test_client()


@pytest.fixture()
def test_config():
    return {
        "posts_path": run.app.config.get('POSTS_PATH'),
        "comments_path": run.app.config.get('COMMENTS_PATH'),
        "bookmarks_path": run.app.config.get('BOOKMARKS_PATH'),
        "empty_list": run.app.config.get('EMPTY_LIST_PATH')
    }
