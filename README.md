Starupium_project проект автоматизации тестирования приложения https://test.startupium.ru<br>
Папка idea попала сюда случайно %)<br>
В пакете Startupium_project лежат:
- conftest - это хранилище фикстур, пока здесь лежат запуск драйвера и остановка. Также выбор браузера (Chrome или Firefox). По умолчанию хром.<br>
- папка pages: тут лежат файлы страниц (Page Object рекомендует =))<br>
   base_page.py - базовый класс<br>
   login_page.py - страница логина<br>
   main_page.py - главная страница<br>
   search_page.py - страница поиска проектов<br>
   footer.py - футер<br>
   header.py -  хедер<br>
   locators.py - селекторы<br>
   project_page.py - страница создания проекта<br>
- test_login_page.py - тестирование возможности логина с валидными данными
- test_create_new_project.py:<br>
     - test_create_new_project_into_draft - тестирование возможности создания черновика проекта используя валидные данные
     - test_create_and_publish_new_project - тестирование возможности создания и публикации проекта используя валидные данные 
- test_main_page.py - тестирование главной страницы из тест-сьюта регрессионного тестирования (будет пополняться)<br>
- test_search_project.py - тестирование возможности поиска проекта<br>
     - test_search_project_unauthorized_user - тестирование возможности поиска проекта неавторизованным пользователем
     
   
