# coding: utf-8

from fastapi.testclient import TestClient


from playlist.models.playlist import Playlist  # noqa: F401


def test_playlist_delete(client: TestClient):
    """Test case for playlist_delete

    Delete the artist data
    """
    params = [("category_id", 56),     ("id", 56),     ("name", 'name_example')]
    headers = {
    }
    response = client.request(
        "DELETE",
        "/playlist",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_playlist_get(client: TestClient):
    """Test case for playlist_get

    Getting all the playlist data (default limit is 20)
    """
    params = [("category_id", 56),     ("id", 56),     ("since_id", 56),     ("limit", 56),     ("created_at_min", 'created_at_min_example'),     ("created_at_max", 'created_at_max_example')]
    headers = {
    }
    response = client.request(
        "GET",
        "/playlist",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_playlist_post(client: TestClient):
    """Test case for playlist_post

    Creating the playlist data
    """
    params = [("category_id", 56),     ("name", 'name_example'),     ("url", 'url_example')]
    headers = {
    }
    response = client.request(
        "POST",
        "/playlist",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_playlist_put(client: TestClient):
    """Test case for playlist_put

    Update the artist data
    """
    params = [("category_id", 56),     ("name", 'name_example'),     ("url", 'url_example')]
    headers = {
    }
    response = client.request(
        "PUT",
        "/playlist",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

