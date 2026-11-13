import pytest
STARS_ERROR = "number of stars must be between 1 and 5 (inclusive)"

def test_base_choice_is_saved(api, auth, pizza_id):
    res = api.post("/api/ratings", json={"pizza_id": pizza_id, "stars": 3}, headers=auth)
    assert res.status_code == 201
    assert res.json()["stars"] == 3
    assert res.json()["pizza_id"] == pizza_id

@pytest.mark.parametrize("stars", [0, 6])
def test_stars_out_of_range(api, auth, pizza_id, stars):
    res = api.post("/api/ratings", json={"pizza_id": pizza_id, "stars": stars}, headers=auth)
    assert res.status_code == 400
    assert res.json() == {"error": STARS_ERROR}

def test_decimal_stars_is_refused(api, auth, pizza_id):
    res = api.post("/api/ratings", json={"pizza_id": pizza_id, "stars": 3.5}, headers=auth)
    assert res.status_code == 400
    assert res.json() == {"error": STARS_ERROR}

def test_text_stars_is_refused(api, auth, pizza_id):
    res = api.post("/api/ratings", json={"pizza_id": pizza_id, "stars": "3"}, headers=auth)
    assert res.status_code == 400
    assert res.json() == {"error": STARS_ERROR}

def test_missing_stars_is_refused(api, auth, pizza_id):
    res = api.post("/api/ratings", json={"pizza_id": pizza_id}, headers=auth)
    assert res.status_code == 400
    assert res.json() == {"error": STARS_ERROR}

def test_nonexistent_pizza_is_refused(api, auth):
    res = api.post("/api/ratings", json={"pizza_id": 999999999, "stars": 3}, headers=auth)
    assert 400 <= res.status_code < 500

def test_missing_token_is_refused(api, pizza_id):
    res = api.post("/api/ratings", json={"pizza_id": pizza_id, "stars": 3})
    assert 400 <= res.status_code < 500

def test_wrong_token_is_refused(api, pizza_id):
    res = api.post("/api/ratings", json={"pizza_id": pizza_id, "stars": 3}, headers={"Authorization": "token short"})
    assert 400 <= res.status_code < 500
