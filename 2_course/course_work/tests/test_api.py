import json

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


class TestAPI:
    def test_get_posts(self, test_client):
        response = test_client.get('/api/posts', follow_redirects=True)
        posts = json.loads(response.data)

        assert type(posts) == list
        assert set(posts[0].keys()) == post_keys_should_be

    def test_get_post_by_pk(self, test_client):
        response = test_client.get('/api/posts/1', follow_redirects=True)
        post = json.loads(response.data)

        assert type(json.loads(response.data)) == dict
        assert set(post.keys()) == post_keys_should_be
