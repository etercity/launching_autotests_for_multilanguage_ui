# launching_autotests_for_multilanguage_ui
(stepik) Учебный проект автотестов, в которых реализовано решение, позволяющее запускать автотесты для разных языков пользователей, передавая нужный язык в командной строке.

Команда для запуска теста:
pytest --language=es test_items.py

!Внимание! драйвер расположен в папке drivers проекта, соответственно в файле conftest.py прописан путь к драйверу.
 