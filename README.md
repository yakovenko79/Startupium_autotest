Starupium_project проект автоматизации тестирования приложения https://test.startupium.ru<br>
Папка idea попала сюда случайно %)<br>
В пакете Startupium_project лежат:
- conftest - это хранилище фикстур, пока здесь лежат запуск драйвера и остановка. Также выбор браузера (Chrome или Firefox). По умолчанию хром.<br>
- папка pages: тут лежат файлы страниц (Page Object рекомендует =))<br>
   articles_page.py - страница статей<br>
   about_page.py - страница "О сайте"<br>
   search_user.py - страница поиска пользователей<br>
   base_page.py - базовый класс<br>
   login_page.py - страница логина<br>
   main_page.py - главная страница<br>
   search_project.py - страница поиска проектов<br>
   footer.py - футер<br>
   header.py -  хедер<br>
   locators.py - селекторы<br>
   profile_page.py - страница профиля<br>
   project_page.py - страница создания проекта<br>
   search_user.py - страница поиска пользователей<br>
   registration_page.py - страница ввода регистрационых данных<br>
- test_login_page.py - тестирование возможности логина с валидными данными
- test_create_new_project.py:<br>
     - test_create_new_project_into_draft - тестирование возможности создания черновика проекта используя валидные данные
     - test_create_and_publish_new_project - тестирование возможности создания и публикации проекта используя валидные данные 
- test_main_page.py - тестирование главной страницы из тест-сьюта регрессионного тестирования (будет пополняться)<br>
- test_main_page_authorized.py - тестирование главной страницы из тест-сьюта регрессионного тестирования<br>
- test_search_project.py - тестирование возможности поиска проекта<br>
     - test_search_project_unauthorized_user - тестирование возможности поиска проекта неавторизованным пользователем<br>
- requirements.txt - зависимости
     
   
