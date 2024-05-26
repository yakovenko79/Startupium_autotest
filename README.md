<h1 align="center">Starupium_project проект автоматизации тестирования приложения <a href="https://test.startupium.ru">test.startupium.ru</a></h1><br>

---

Папка idea попала сюда случайно %)<br>
<h3>В пакете Startupium_project лежат:</h3>
- <b>conftest</b> - это хранилище фикстур, пока здесь лежат запуск драйвера и остановка. Также выбор браузера (Chrome или Firefox). По умолчанию хром.<br>
- папка <b>pages</b> тут лежат файлы страниц (<b>Page Object</b> рекомендует =))<br>
<ul>
<li> <i>articles_page.py</i> - страница статей<br></li>
<li> <i>about_page.py</i> - страница "О сайте"<br></li>
<li> <i>search_user.py</i> - страница поиска пользователей<br></li>
<li> <i>base_page.py</i> - базовый класс<br></li>
<li> <i>login_page.py</i> - страница логина<br></li>
<li> <i>main_page.py</i> - главная страница<br></li>
<li> <i>search_project.py</i> - страница поиска проектов<br></li>
<li> <i>footer.py</i> - футер<br></li>
<li> <i>header.py</i> -  хедер<br></li>
<li> <i>locators.py</i> - селекторы<br></li>
<li> <i>profile_page.py</i> - страница профиля<br></li>
<li> <i>project_page.py</i> - страница создания проекта<br></li>
<li> <i>search_user.py</i> - страница поиска пользователей<br></li>
<li> <i>registration_page.py</i> - страница ввода регистрационых данных (не реализовано, т.к есть в рабочем проекте)<br></li>
</ul>
- <b>test_login_page.py</b> - тестирование возможности логина с валидными данными<br>
<br>
- <b>test_create_new_project.py</b> - тестирование возможности создания нового проекта:<br>
<ul>
<li> test_create_new_project_into_draft - тестирование возможности создания черновика проекта используя валидные данные<br></li>
<li> test_create_and_publish_new_project - тестирование возможности создания и публикации проекта используя валидные данные<br></li>
</ul>
- <b>test_main_page_unauthorized.py</b> - тестирование главной страницы из тест-сьюта регрессионного тестирования пользователь неавторизован<br>
- <b>test_main_page_authorized.py</b>- тестирование главной страницы из тест-сьюта регрессионного тестирования пользователь авторизован<br>
- <b>test_search_project.py</b> - тестирование возможности поиска проекта<br>
    <li> test_search_project_unauthorized_user - тестирование возможности поиска проекта неавторизованным пользователем<br></li>
- <b>requirements.txt</b> - зависимости<br>
- <b>pytest.ini</b> - маркировка тестов<br>
<ul>
    <li> <i>regression</i> - регрессионные тесты, можно использовать для запуска всех тестов<br></li>
    <li> <i>authorized</i> - тесты для авторизованного пользователя<br></li>
    <li> <i>unauthorized</i> - тесты для неавторизованного пользователя<br></li>
</ul>
---

Для запуска группы тестов исходя из маркировки рекомендуется использовать запуск из командной строки<br>

pytest {test} (например: <i>pytest test_main_page_authorized.py</i>)<br>
pytest -m {marker} (например: <i>pytest -m regression</i>)<br>

Также возможно выполнять run какого-либо одного теста, либо класса прямо из кода<br> 

---

В настоящий момент проект содержит 53 автотеста<br>

---


     

     
   
