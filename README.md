# Описание 

    Бэкэнд приложения "Онлайн-тренер". Реализована возможность регистрации пользователей,
создания тренировок для тренеров и написания отчетов выполненных тренировок учениками.
Создавать, редактировать и удалять тренировки могут только поьзователи, которые имеют статус 
"тренер". Просматривать тренировки могут ученики, для которых написана данная тренировка.
Просматривать отчеты могут все зарегистрированные пользователи. Редактировать и удалять отчеты
могут только авторы отчетов. 

#Примеры запросов к API 

*Регистрация нового пользователя 

/auth/users/  
[](https://github.com/fatrunner-39/online_coach/blob/master/screenshots/create_user.jpg) 

*Получение JWT токена 

/auth/jwt/create/ 
[](https://github.com/fatrunner-39/online_coach/blob/master/screenshots/create_jwt.jpg) 

*Обновление профиля пользователя 

/api/v1/profile/{pk}/ 
[](https://github.com/fatrunner-39/online_coach/blob/master/screenshots/update_profile.jpg) 

*Создание тренировки 

/api/v1/workouts/ 
[](https://github.com/fatrunner-39/online_coach/blob/master/screenshots/create_workout_part1.jpg) 
[](https://github.com/fatrunner-39/online_coach/blob/master/screenshots/create_workout_part_2.jpg) 

*Получение списка тренировок 

/api/v1/workouts/ 
[]() 

*Удаление тренировки 

/api/v1/workouts/{pk}/ 
[](https://github.com/fatrunner-39/online_coach/blob/master/screenshots/delete_workout.jpg) 

*Создание отчета 

/api/v1/reports/ 
[](https://github.com/fatrunner-39/online_coach/blob/master/screenshots/create_report.jpg) 

*Получение списка отчетов 

/api/v1/reports/ 
[](https://github.com/fatrunner-39/online_coach/blob/master/screenshots/get_reports.jpg) 

*Обновление отчета 

/api/v1/reports/{pk}/ 
[](https://github.com/fatrunner-39/online_coach/blob/master/screenshots/update_report.jpg) 

#Установка 

1. git clone https://github.com/fatrunner-39/online_coach.git 
2. cd online_coach 
3. source env/bin/activate (for windows env\Scripts\activate) 
4. pip install -r requirements.txt 
5. create .env file in setttings package 
6. createdb -U username database_name 
7. python manage.py migrate 
8. python manage.py runserver 
   