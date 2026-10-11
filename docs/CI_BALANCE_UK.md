# Розподіл перевірок CI

## Поточний стан — 2026-10-11

Для `ziko1/flask` основний сервіс перевірок — **GitHub Actions, стандартний Linux runner**. Це серверний Flask-шаблон. Окремого native iOS/macOS завдання немає; Codemagic для цього репозиторію не налаштовано.

Конфігурація перевірена на exact Git SHA `68fb12b4895fa3cbd4a98cab1a150dd4e1f72ca6`, [PR #2](https://github.com/ziko1/flask/pull/2), поверх `fix/runtime-readiness-20261008` / `4ff580b7a06131ec9102109f06c9ac9e33e1adb0`. Зміни стосуються лише workflow. Вихідний код, залежності й наявні тести збережені.

## Коли запускати

| Подія | Поведінка |
| --- | --- |
| Push до робочої гілки | Окремий дубль тестів не запускається; робота перевіряється через PR. |
| Створення або оновлення PR | Наявний suite запускається для PR до будь-якої гілки, включно зі stacked PR. |
| Push до main або Git tag | Наявні перевірки запускаються. |
| Ручний запуск | `workflow_dispatch` налаштовано; GitHub надає його після появи workflow у default branch. |
| Нові зміни того самого PR | Застарілий незавершений verification run скасовується. |

Suite: `python -m unittest -v` та `gunicorn --check-config main:app` на Python 3.12. Job обмежений 10 хвилинами. Існуючий pip cache збережено. 

## Фактична перевірка

YAML, маршрутизація подій, збереження команд/jobs і read-only permissions перевірені. GitHub зареєстрував один PR workflow для цього candidate без дублюючого branch-push workflow. [Запуск 38160743104](https://github.com/ziko1/flask/actions/runs/38160743104) зупинився до виділення runner: `runner_id=0`, `steps=[]`. **Нові application/build checks мають стан BLOCKED_ENVIRONMENT, а не PASS.** Причина — обмеження виконання на стороні облікового запису провайдера.

[Машинний доказ](../evidence/ci-balance-20261011.json) зберігає full SHA, GitHub run/job IDs, порівняння джерел та окремі історичні результати. Подальший documentation-only commit не змінює tested workflow і не підміняє його SHA. Він позначений `[skip ci]`, щоб не повторювати завідомо заблокований запуск.

Після відновлення GitHub виконати наявні перевірки для погодженого exact source. Поточний PR не злитий; готовність усього продукту визначається окремо у [плані завершення](../COMPLETION_PLAN_UK.md).

Офіційні правила: [події та фільтри workflow](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax), [concurrency](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency).
