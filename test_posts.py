from conftest import BASE_URL
from src.enums.global_enums import GlobalErrorMessages


def test_get_all_posts(api):
    response = api.get(f'{BASE_URL}/posts')
    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert len(response.json()) == 100, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value


def test_get_post_by_id(api):
    response = api.get(f'{BASE_URL}/posts/1')
    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert response.json()['id'] == 1


def test_patching_resource(api):
    data = {
        "title": "foo",
        "body": "..."
    }
    response = api.patch(f'{BASE_URL}/posts/1', json=data)
    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert response.json()['id'] == 1
    assert response.json()['title'] == 'foo'
    assert response.json()['body'] == '...'
    assert response.json()['userId'] == 1


def test_get_posts_by_user_id(api):
    response = api.get(f'{BASE_URL}/posts', params={'userId': 1})
    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert len(response.json()) > 0, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value


def test_create_post(api):
    data = {
        "title": "foo",
        "body": "bar",
        "userId": 1,
    }
    response = api.post(f'{BASE_URL}/posts', json=data)
    assert response.status_code == 201, GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert response.json()['id'] == 101
    assert response.json()['userId'] == 1


def test_update_post(api):
    data = {
        "id": 1,
        "title": "foo",
        "body": "bar",
        "userId": 1,
    }
    response = api.put(f'{BASE_URL}/posts/1', json=data)
    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert response.json()['id'] == 1
    assert response.json()['title'] == "foo"
    assert response.json()['body'] == "bar"
    assert response.json()['userId'] == 1


def test_delete_post(api):
    response = api.delete(f'{BASE_URL}/posts/1')
    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert response.content == b'{}'
