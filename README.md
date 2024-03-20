Starupium_project проект автоматизации тестирования приложения https://test.startupium.ru
Папка idea попала сюда случайно %)
В пакете Startupium_project лежат:
- conftest - это хранилище фикстур, пока здесь лежат запуск драйвера и остановка. Также выбор браузера (Chrome или Firefox). По умолчанию хром.
- папка pages: тут лежат файлы страниц (Page Object рекомендует =))
   base_page.py - базовый класс
   login_page.py - страница логина
   main_page.py - главная страница
   locators.py - селекторы
- test_login_page.py - тестирование возможности логина с валидными данными
   
