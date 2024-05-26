<h1 align="center">Starupium_project проект автоматизации тестирования приложения <a href="https://test.startupium.ru">test.startupium.ru</a></h1><br>

---

Папка idea попала сюда случайно %)<br>
<h3>В пакете Startupium_project лежат:</h3>
- <b>conftest</b> - это хранилище фикстур, пока здесь лежат запуск драйвера и остановка. Также выбор браузера (Chrome или Firefox). По умолчанию хром.<br>
- папка <b>pages</b> тут лежат файлы страниц (<b>Page Object</b> рекомендует =))<br>
   <i>articles_page.py</i> - страница статей<br>
   <i>about_page.py</i> - страница "О сайте"<br>
   <i>search_user.py</i> - страница поиска пользователей<br>
   <i>base_page.py</i> - базовый класс<br>
   <i>login_page.py</i> - страница логина<br>
   <i>main_page.py</i> - главная страница<br>
   <i>search_project.py</i> - страница поиска проектов<br>
   <i>footer.py</i> - футер<br>
   <i>header.py</i> -  хедер<br>
   <i>locators.py</i> - селекторы<br>
   <i>profile_page.py</i> - страница профиля<br>
   <i>project_page.py</i> - страница создания проекта<br>
   <i>search_user.py</i> - страница поиска пользователей<br>
   <i>registration_page.py</i> - страница ввода регистрационых данных (не реализовано, т.к есть в рабочем проекте)<br>
- <b>test_login_page.py</b> - тестирование возможности логина с валидными данными<br>
- <b>test_create_new_project.py**:</b>
    - test_create_new_project_into_draft - тестирование возможности создания черновика проекта используя валидные данные<br>
    - test_create_and_publish_new_project - тестирование возможности создания и публикации проекта используя валидные данные<br>
- <b>test_main_page_unauthorized.py</b> - тестирование главной страницы из тест-сьюта регрессионного тестирования пользователь неавторизован<br>
- <b>test_main_page_authorized.py</b>- тестирование главной страницы из тест-сьюта регрессионного тестирования пользователь авторизован<br>
- <b>test_search_project.py</b> - тестирование возможности поиска проекта<br>
     - test_search_project_unauthorized_user - тестирование возможности поиска проекта неавторизованным пользователем<br>
- <b>requirements.txt</b> - зависимости<br>
- <b>pytest.ini</b> - маркировка тестов<br>
     - <i>regression</i> - регрессионные тесты, можно использовать для запуска всех тестов<br>
     - <i>authorized</i> - тесты для авторизованного пользователя<br>
     - <i>unauthorized</i> - тесты для неавторизованного пользователя<br>
  
---

Для запуска группы тестов исходя из маркировки рекомендуется использовать запуск из командной строки<br>

pytest {test} (например: <i>pytest test_main_page_authorized.py</i>)<br>
pytest -m {marker} (например: <i>pytest -m regression</i>)<br>

Также возможно выполнять run какого-либо одного теста, либо класса прямо из кода<br> 

---

В настоящий момент проект содержит 53 автотеста<br>

---


     

     
   
