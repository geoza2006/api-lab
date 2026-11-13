# API lab results

## Part 0

- Step 0.1, the number of pizza names: see GET /api/names output; record the count from your run.
- Step 0.3, status code of the request without a token: 401
- Step 0.4, the name of your pizza: random per run; record the pizza name returned by POST /api/pizza.
- Step 0.12, results of the three runs without a session (optional): expected flaky; record each observed pass or fail.
- Step 0.16, blocks of "how many of the three tools are excluded": 0, 1, 2, and 3

## Defect report

- Title: Excluding every pizza tool returns an empty 500 response
- Request: POST /api/pizza with {"excludedTools":["Knife","Pizza cutter","Scissors"]} and a valid logged-in token
- Expected result: 400 Bad Request with a JSON error message explaining that no suitable tool is available
- Actual result: 500 Internal Server Error with an empty body
- Severity: Medium; the client cannot distinguish an unsatisfiable request from a server outage and receives no actionable message

## Part A

- Step A4, status codes when the other user reads, changes and deletes: record the exact three codes from your run; each must be a 4xx response

## Part B

1. API tests can find incorrect HTTP status codes and integration failures involving routing, authentication, serialization, persistence, or a real load balancer; a unit test with stubs cannot observe those real-system failures. Unit tests are still useful because they are fast, deterministic, and pinpoint the faulty function.
2. Each test creates a unique user so tests cannot change shared data or depend on another student's state. In Project 2, create uniquely named shop or hotel data, use only the group's own credentials, and clean up data created by a test.
3. One session preserves the load-balancer cookies, so user creation and login reach the same backend server. Without it, login can randomly reach a server that has not seen the new user, making the test flaky; record the three observed outcomes when running the optional test.
4. The three-excluded-tools block revealed the defect. A 500 with an empty body looks like an infrastructure failure and gives an API client no useful explanation, while a 400 JSON response identifies a bad request. The test remains as xfail so the defect stays visible and alerts us when it is fixed.
5. Base choice needs 1 + 2 + 3 + 1 + 2 = 9 tests. All combinations need 3 x 4 x 2 x 3 = 72 tests.
6. Record the exact read, update, and delete status codes from the owner tests. Any 4xx response is acceptable; the important property is that the other user cannot access the owner's data. A difference among 401, 403, and 404 is not automatically a defect unless the API contract specifies one exact code.
7. The made-up token is read-only in this exercise. Record the response from GET /api/ratings. If it grants access, that is a security defect because a stranger could read rating data; never use it to create, update, or delete anything.
8. API tests check exact methods, URLs, headers, status codes, JSON fields, and persistence efficiently. Only browser-level tests can verify visual layout, browser interactions, and what a real user sees on the page.
