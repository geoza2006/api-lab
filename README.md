# API lab

ITDS362 API testing exercise for QuickPizza using requests and pytest.

## Install and run

    python -m venv .venv
    .venv\Scripts\activate
    pip install -r requirements.txt
    pytest -v
    pytest -v --html=report.html --self-contained-html

## Input domain model: POST /api/ratings

| Characteristic | Blocks | Values in tests | Covering tests |
|---|---|---|---|
| C1 stars value | below 1; 1 to 5 base; above 5 | 0; 3; 6 | test_stars_out_of_range, test_base_choice_is_saved |
| C2 stars type | whole number base; decimal; text; missing | 3; 3.5; "3"; no field | test_base_choice_is_saved, test_decimal_stars_is_refused, test_text_stars_is_refused, test_missing_stars_is_refused |
| C3 pizza | exists base; does not exist | fixture pizza; 999999999 | test_base_choice_is_saved, test_nonexistent_pizza_is_refused |
| C4 token | own base; none; wrong length | auth; no header; token short | test_base_choice_is_saved, test_missing_token_is_refused, test_wrong_token_is_refused |

Base choice coverage needs 1 + 2 + 3 + 1 + 2 = 9 tests. All combinations need 3 x 4 x 2 x 3 = 72 tests.

Excluded tools characteristic "how many of the three tools are excluded" has blocks 0, 1, 2, and 3. The block with all three tools reveals the defect tracked as xfail in test_excluded_tools.py.
