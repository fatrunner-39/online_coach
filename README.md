# Описание
###     Бэкэнд приложения "Онлайн-тренер". Реализована возможность регистрации пользователей,
###создания тренировок для тренеров и написания отчетов выполненных тренировок учениками.
###Создавать, редактировать и удалять тренировки могут только поьзователи, которые имеют статус 
###"тренер". Просматривать тренировки могут ученики, для которых написана данная тренировка.
###Просматривать отчеты могут все зарегистрированные пользователи. Редактировать и удалять отчеты
###могут только авторы отчетов.

#Примеры запросов к API
*Регистрация нового пользователя
/auth/users/


*Получение JWT токена
/auth/jwt/create/

*Обновление профиля пользователя
/api/v1/profile/{pk}/


*Создание тренировки
/api/v1/workouts/


*Получение списка тренировок
/api/v1/workouts/


*Удаление тренировки
/api/v1/workouts/{pk}/


*Создание отчета
/api/v1/reports/


*Получение списка отчетов
/api/v1/reports/


*Обновление отчета
/api/v1/reports/{pk}/


#Установка
1. git clone https://github.com/fatrunner-39/online_coach.git
2. cd online_coach
3. source env/bin/activate (for windows env\Scripts\activate)
4. pip install -r requirements.txt
5. create .env file in setttings package
6. createdb -U username database_name
7. python manage.py migrate
8. python manage.py runserver
   