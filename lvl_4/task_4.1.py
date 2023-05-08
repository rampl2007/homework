# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:


import sqlite3

#создание таблицы Students
def create_table():
    connection = sqlite3.connect('teatchers.db')
    cursor = connection.cursor()
    sqlquery = """CREATE TABLE Students (
    Student_Id INTEGER NOT NULL,
    Student_Name TEXT NOT NULL,
    School_Id INTEGER NOT NULL PRIMARY KEY
    );"""
    cursor.execute(sqlquery)
    connection.commit()
    connection.close()

#заполнение данными таблицы Students
def insert_data():
    connection = sqlite3.connect('teatchers.db')
    cursor = connection.cursor()
    sqlquery = """insert into Students (Student_Id, Student_Name, School_Id)
    VALUES
    (201, 'Иван', 1),
    (202, 'Петр', 2),
    (203, 'Анастасия', 3),
    (204, 'Игорь', 4);"""
    cursor.execute(sqlquery)
    connection.commit()
    connection.close()

def get_student_data(Student_Id):
    try:
        connection = sqlite3.connect('teatchers.db')
        cursor = connection.cursor()
        select_query = """SELECT Students.Student_Id, Students.Student_Name, School.School_Id, School.School_Name
        FROM Students
        full JOIN School ON School.school_id = Students.school_id"""
        cursor.execute(select_query)
        records = cursor.fetchall()
        connection.close()
        for row in records:
            if row[0] == Student_Id:
                print("ID Студента:", row[0])
                print("Имя студента:", row[1])
                print("ID школы:", row[2])
                print("Название школы:", row[3])
    except(Exception, sqlite3.Error) as error:
        print("Ошибка в получении данных: ", error)


# create_table()
# insert_data()
x = int(input("Введите ID студента: "))
get_student_data(x)