# coding: utf-8

from fastapi.testclient import TestClient


from artist.models.artist import Artist  # noqa: F401


def test_artist_delete(client: TestClient):
    """Test case for artist_delete

    Delete the artist data
    """
    params = [("source_id", 56),     ("id", 56),     ("name", 'name_example')]
    headers = {
    }
    response = client.request(
        "DELETE",
        "/artist",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artist_get(client: TestClient):
    """Test case for artist_get

    Getting all the artist data (default limit is 20)
    """
    params = [("id", 56),     ("source_id", 56),     ("since_id", 56),     ("limit", 56),     ("created_at_min", 'created_at_min_example'),     ("created_at_max", 'created_at_max_example'),     ("nationality", 'nationality_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/artist",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artist_post(client: TestClient):
    """Test case for artist_post

    Creating the artist data
    """
    params = [("source_id", 56),     ("name", 'name_example'),     ("birthday", 'birthday_example'),     ("gender", 'gender_example'),     ("life", 'life_example'),     ("url", 'url_example')]
    headers = {
    }
    response = client.request(
        "POST",
        "/artist",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artist_put(client: TestClient):
    """Test case for artist_put

    Update the artist data
    """
    params = [("source_id", 56),     ("name", 'name_example'),     ("birthday", 'birthday_example'),     ("gender", 'gender_example'),     ("life", 'life_example'),     ("url", 'url_example')]
    headers = {
    }
    response = client.request(
        "PUT",
        "/artist",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

