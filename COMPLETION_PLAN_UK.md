# Flask — план завершення

Scope: мінімальний серверний шаблон. Власну бізнес-функцію користувач ще не визначив.

1. Відтворюване clean install на Python 3.12, pinned dependencies.
2. GET / збережено, /health дає JSON, debug вимкнений, WSGI і PORT працюють.
3. CI відтворює unittest і WSGI configuration check.
4. Окремо визначити основний бізнес-сценарій і середовище розгортання.

Product status: NOT READY — бізнес-вимоги та live deployment не визначені. Локальний template scope перевіряється evidence/verification.json.

## CI balance — 2026-10-11

Configuration source `68fb12b4895fa3cbd4a98cab1a150dd4e1f72ca6` у [PR #2](https://github.com/ziko1/flask/pull/2) зберігає наявний suite на GitHub Linux і усуває дубль feature-push/PR. Додано bounded job/cancellation; pip cache збережено. Source/configuration validation **PASS**; actual run 38160743104 **BLOCKED_ENVIRONMENT** до runner, tests/build **NOT_RUN**. Це не змінює product readiness вище. [CI інструкція](docs/CI_BALANCE_UK.md), [evidence](evidence/ci-balance-20261011.json), [пам'ять](PROJECT_MEMORY.md). Наступний крок — actual hosted verification після відновлення виконання, потім окреме рішення про merge.
