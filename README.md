Starupium_project проект автоматизации тестирования приложения https://test.startupium.ru
Папка idea попала сюда случайно %)
В пакете Startupium_project лежат:
- conftest - это хранилище фикстур, пока здесь лежат запуск драйвера и остановка. Также выбор браузера (Chrome или Firefox). По умолчанию хром.
- папка pages: тут лежат файлы страниц (Page Object рекомендует =))
   base_page.py - базовый класс
   login_page.py - страница логина
   main_page.py - главная страница
   locators.py - селекторы
   project_page.py - страница создания проекта
- test_login_page.py - тестирование возможности логина с валидными данными
- test_create_new_project.py:
     test_create_new_project_into_draft - тестирование возможности создания черновика проекта используя валидные данные
     test_create_and_publish_new_project - тестирование возможности создания и публикации проекта используя валидные данные 
   
