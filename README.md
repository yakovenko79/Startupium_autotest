<h1 align="center">Starupium_project проект автоматизации тестирования приложения <a href="https://test.startupium.ru">test.startupium.ru</a></h1><br>

---

Папка idea попала сюда случайно %)<br>
<h3>В пакете Startupium_project лежат:</h3>
- **conftest** - это хранилище фикстур, пока здесь лежат запуск драйвера и остановка. Также выбор браузера (Chrome или Firefox). По умолчанию хром.<br>
- папка **pages**: тут лежат файлы страниц (__Page Object__ рекомендует =))<br>
   *articles_page.py* - страница статей<br>
   *about_page.py* - страница "О сайте"<br>
   *search_user.py* - страница поиска пользователей<br>
   *base_page.py* - базовый класс<br>
   *login_page.py* - страница логина<br>
   *main_page.py* - главная страница<br>
   *search_project.py* - страница поиска проектов<br>
   *footer.py* - футер<br>
   *header.py* -  хедер<br>
   *locators.py* - селекторы<br>
   *profile_page.py* - страница профиля<br>
   *project_page.py* - страница создания проекта<br>
   *search_user.py* - страница поиска пользователей<br>
   *registration_page.py* - страница ввода регистрационых данных (не реализовано, т.к есть в рабочем проекте)<br>
- **test_login_page.py** - тестирование возможности логина с валидными данными<br>
- **test_create_new_project.py**:<br>
    - test_create_new_project_into_draft - тестирование возможности создания черновика проекта используя валидные данные<br>
    - test_create_and_publish_new_project - тестирование возможности создания и публикации проекта используя валидные данные<br>
- **test_main_page_unauthorized.py** - тестирование главной страницы из тест-сьюта регрессионного тестирования пользователь неавторизован<br>
- **test_main_page_authorized.py** - тестирование главной страницы из тест-сьюта регрессионного тестирования пользователь авторизован<br>
- **test_search_project.py** - тестирование возможности поиска проекта<br>
     - test_search_project_unauthorized_user - тестирование возможности поиска проекта неавторизованным пользователем<br>
- **requirements.txt** - зависимости<br>
- **pytest.ini** - маркировка тестов<br>
     - *regression* - регрессионные тесты, можно использовать для запуска всех тестов<br>
     - *authorized* - тесты для авторизованного пользователя<br>
     - *unauthorized* - тесты для неавторизованного пользователя<br>
---
Для запуска группы тестов исходя из маркировки рекомендуется использовать запуск из командной строки<br>

pytest {test} (например: *pytest test_main_page_authorized.py*)<br>
pytest -m {marker} (например: *pytest -m regression*)<br>

Также возможно выполнять run какого-либо одного теста, либо класса прямо из кода<br> 

---
В настоящий момент проект содержит 53 автотеста<br>


     

     
   
