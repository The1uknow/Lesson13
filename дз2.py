import sqlite3

c = sqlite3.connect("mydatabase.db")
cursor = c.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    grade TEXT
)
""")
c.commit()

cursor.execute("SELECT COUNT(*) FROM students")
if cursor.fetchone()[0] == 0:
    students_data = [
        ("лола", 20, 5),
        ("самир", 22, 4),
        ("крис", 21, 4)
    ]
    cursor.executemany("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", students_data)
    c.commit()

def get_student_by_name(name):
    cursor.execute("SELECT name, age, grade FROM students WHERE name = ?", (name,))
    student = cursor.fetchone()
    if student:
        print(f"имя: {student[0]}, возраст: {student[1]}, оценка: {student[2]}")
    else:
        print("студент не найден")

def update_student_grade(name, new_grade):
    cursor.execute("UPDATE students SET grade = ? WHERE name = ?", (new_grade, name))
    if cursor.rowcount == 0:
        print("студент не найден")
    else:
        c.commit()
        print(f"оценка студента {name} обновлена на {new_grade}")

def delete_student(name):
    cursor.execute("DELETE FROM students WHERE name = ?", (name,))
    if cursor.rowcount == 0:
        print("студент не найден")
    else:
        c.commit()
        print(f"студент {name} удален")


while True:
    print("\nменю:")
    print("1. показать всех студентов")
    print("2. найти студента по имени")
    print("3. изменить оценку студента")
    print("4. удалить студента")
    print("5. выход")
    choice = input("выберите действие: ")

    if choice == "1":
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        if students:
            for student in students:
                print(f"ID: {student[0]}, имя: {student[1]}, возраст: {student[2]}, оценка: {student[3]}")
        else:
            print("нет студентов в базе данных")
    elif choice == "2":
        name = input("введите имя студента: ")
        get_student_by_name(name)
    elif choice == "3":
        name = input("введите имя студента: ")
        new_grade = input("введите новую оценку: ")
        update_student_grade(name, new_grade)
    elif choice == "4":
        name = input("введите имя студента: ")
        delete_student(name)
    elif choice == "5":
        print("вы вышли")
        break
    else:
        print("попробуйте снова")

c.close()