import pytest

@pytest.mark.parametrize("excluded", [[], ["Knife"], ["Scissors"], ["Pizza cutter"], ["Knife", "Scissors"], ["Knife", "Pizza cutter"], ["Pizza cutter", "Scissors"]])
def test_excluded_tool_is_not_used(api, auth, excluded):
    res = api.post("/api/pizza", json={"excludedTools": excluded}, headers=auth)
    assert res.status_code == 200
    assert res.json()["pizza"]["tool"] not in excluded

@pytest.mark.xfail(reason="Defect 1: excluding all tools returns 500 with an empty body instead of 400 JSON", strict=True)
def test_excluding_all_tools_is_rejected_with_a_client_error(api, auth):
    res = api.post("/api/pizza", json={"excludedTools": ["Knife", "Pizza cutter", "Scissors"]}, headers=auth)
    assert res.status_code == 400
    assert res.json() == {"error": "no suitable tool"}
