# Приклади повідомлень комітів (Conventional Commits)

Відповідно до специфікації **Conventional Commits**, повідомлення коміту має чітку структуру:
`тип(область): короткий опис змін`

## Основні типи комітів (Types)
* `feat` — додавання нової функціональності (feature).
* `fix` — виправлення помилки або дефекту (bug fix).
* `docs` — оновлення документації (звіти, README, коментарі).
* `style` — зміни форматування коду, відступів чи пробілів (без зміни логіки).
* `refactor` — рефакторинг коду без виправлення помилок чи додавання нових функцій.
* `test` — додавання або оновлення модульних/інтеграційних тестів.
* `chore` — оновлення конфігурацій проєкту, залежностей, інструментів збірки чи хуків.

---

## ✅ Коректні приклади (успішно проходять валідацію `commitizen`)
* `feat(lab6): configure pre-commit hooks and commitizen validation`
* `fix(parser): resolve null pointer exception in inventory module`
* `docs(lab6): add README report and commit examples`
* `style(core): format python scripts using black`
* `refactor(api): optimize database query execution`
* `test(processor): add unit tests with 100% branch coverage`
* `chore: update pre-commit hook revisions in config`

---

## ❌ Некоректні приклади (блокуються хуком `commitizen`)
* `зробив лабораторну роботу` — *відсутній тип коміту та двокрапка.*
* `update files` — *використано довільний текст замість стандартизованого типу.*
* `feat add new validation` — *порушено синтаксис: пропущено двокрапку (`:`) після типу.*
* `FEAT(lab6): add config` — *тип коміту має бути написаний виключно малими літерами.*
* `feat(lab6): ` — *відсутній опис змін після двокрапки.*
