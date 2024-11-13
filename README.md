    Описание задачи:

        Необходимо разработать платформу для самообучения студентов.
        Платформа должна обеспечивать возможность авторизации и аутентификации пользователей,
        предоставлять функционал для создания и управления разделами и материалами, а также тестирования знаний.
        Основные сущности должны управляться как через административную панель Django, так и через REST API.
        Необходимо реализовать работу с правами пользователей и ролями. 
        Функционал платформы должен быть реализован с использованием Django Rest Framework (DRF).


    Требования:
        Авторизация и аутентификация:
            . Реализовать регистрацию и вход пользователей.
            . Обеспечить защиту API от неавторизованных пользователей с использованием JWT токенов.
        Управление контентом:
            . Реализовать CRUD (создание, чтение, обновление, удаление) для разделов и материалов через Django admin и REST API.
            . Владелец курса должен иметь возможность добавлять и управлять тестами для каждого материала.
        Тестирование знаний:
            . Реализовать функционал тестов для материалов.
            . Проверка ответов на тесты должна осуществляться через отдельный запрос на сервер.
        Права пользователей:
            Реализовать систему ролей и прав доступа:
                . Администраторы: полный доступ ко всем функциям платформы.
                . Владельцы курсов (Преподаватели): доступ к управлению своими курсами, материалами и тестами.
                . Студенты: доступ только к просмотру материалов и прохождению тестов.

    Технические требования:
        Фреймворк:
            . Для реализации проекта использовать фреймворк Django с Django Rest Framework (DRF).
        База данных:
            . Использовать PostgreSQL для хранения данных.
        ORM:
            . Использовать встроенную ORM Django для взаимодействия с базой данных.
        Документация:
            . В корне проекта должен быть файл README.md с описанием структуры проекта и инструкциями по установке и запуску.
            . Реализовать автогенерируемую документацию API с использованием Swagger.
        Качество кода:
            . Соблюдать стандарты PEP8.
            . Весь код должен храниться в удаленном Git репозитории.
        Тестирование:
            . Написать тесты для всех основных функций платформы.
        Безопасность:
            . Настроить CORS для работы с доверенными доменными именами или IP адресами.
            . Реализовать авторизацию с использованием JWT токенов
    
    Инструкция по запуску проекта:
        Перед тем как запускать проект, заполните все поля которые представлены в файле .env.sample
        После чего выполните и примените миграции, используя команды:
            . python manage.py makemigrations
            . python manage.py migrate
        Создайте Суперпользователя для управления админ-панелью, командой:
            . python manage.py csu
        Выполните команду, для запуска проекта:
            . python manage.py runserver

    Примечание:
        * Если хотите запустить тесты, то вам придется разграничить прова доступа к эндпоинтам поставив AllowAny
            тесты можно запустить командой python manage.py test