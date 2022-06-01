from run import app


def test_get_posts_all(mock_post_manager_load_data, post_fields):
    response = app.test_client().get("/api/posts", follow_redirects=True)

    assert type(response.json) == list
    assert set(response.json[0].keys()) == post_fields


def test_get_posts(mock_post_manager_load_data, post_fields):
    response = app.test_client().get("/api/posts/1", follow_redirects=True)

    assert type(response.json) == dict
    assert set(response.json.keys()) == post_fields
