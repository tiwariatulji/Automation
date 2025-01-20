import requests
import pytest

def test_get_all_posts():
    # Base URL
    base_url = "https://jsonplaceholder.typicode.com"

    # Step 1: Fetch all posts using a GET endpoint
    response = requests.get(f"{base_url}/posts")

    # Step 2: Assert that the response status code is 200
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    # Step 3: Validate that the response returns a non-empty list of posts
    posts = response.json()
    assert isinstance(posts, list), "Response is not a list"
    assert len(posts) > 0, "The posts list is empty"

    # Step 4: Verify that for a specific id (e.g., id=1), the post title and body are not null
    specific_post_response = requests.get(f"{base_url}/posts/1")
    assert specific_post_response.status_code == 200, f"Expected status code 200 for post with id=1, but got {specific_post_response.status_code}"

    specific_post = specific_post_response.json()
    assert specific_post.get("id") == 1, "The id of the specific post is not 1"
    assert specific_post.get("title") is not None, "Title for post with id=1 is null"
    assert specific_post.get("body") is not None, "Body for post with id=1 is null"

if __name__ == "__main__":
    pytest.main()
