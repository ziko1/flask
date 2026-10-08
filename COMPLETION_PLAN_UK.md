# Flask — план завершення

Scope: мінімальний серверний шаблон. Власну бізнес-функцію користувач ще не визначив.

1. Відтворюване clean install на Python 3.12, pinned dependencies.
2. GET / збережено, /health дає JSON, debug вимкнений, WSGI і PORT працюють.
3. CI відтворює unittest і WSGI configuration check.
4. Окремо визначити основний бізнес-сценарій і середовище розгортання.

Product status: NOT READY — бізнес-вимоги та live deployment не визначені. Локальний template scope перевіряється evidence/verification.json.
