import sqlite3
import os

def create_database():
    if os.path.exists("students.db"):
        os.remove("students.db")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    return conn, cursor

def create_tables(cursor):

    cursor.execute('''
    CREATE TABLE Students (
        id INTEGER PRIMARY KEY,
        name VARCHAR NOT NULL,
        age INTEGER,
        email VARCHAR UNIQUE,
        city VARCHAR)
    ''')

    cursor.execute('''
        CREATE TABLE Courses (
            id INTEGER PRIMARY KEY,
            course_name VARCHAR NOT NULL,
            instructor TEXT,
            credits INTEGER)
        ''')


def insert_sample_data(cursor):

    students = [
        (1, 'Alice Johnson', 20, 'alice@gmail.com', 'New York'),
        (2, 'Bob Smith', 19, 'bob@gmail.com', 'Chicago'),
        (3, 'Carol White', 21, 'carol@gmail.com', 'Boston'),
        (4, 'David Brown', 20, 'david@gmail.com', 'New York'),
        (5, 'Emma Davis', 22, 'emma@gmail.com', 'Seattle')
    ]

    cursor.executemany("INSERT INTO Students VALUES (?,?,?,?,?)", students)

    courses = [
        (1, 'Python Programming', 'Dr. Anderson', 3),
        (2, 'Web Development', 'Prof. Wilson', 4),
        (3, 'Data Science', 'Dr. Taylor', 3),
        (4, 'Mobile Apps', 'Prof. Garcia', 2)
    ]

    cursor.executemany("INSERT INTO Courses VALUES (?,?,?,?)", courses)

    print("Sample data inserted successfully")

"""
def basic_sql_operations(cursor):

    #1) SELECT ALL
    print("----------Select All----------")
    cursor.execute("SELECT * FROM Students")
    records = cursor.fetchall()
    for row in records:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Email: {row[3]}, City: {row[4]}")

    # 2) SELECT Columns
    print("----------Select Columns----------")
    cursor.execute("SELECT name, age FROM Students")
    records = cursor.fetchall()
    print(records)

    # 3) WHERE clause (filitreleme)
    print("----------Where Age = 20 ----------")
    cursor.execute("SELECT * FROM Students WHERE age = 20")
    records = cursor.fetchall()
    for row in records:
        print(row)

    # 4) WHERE with string
    print("----------Where city = New York ----------")
    cursor.execute("SELECT * FROM Students WHERE city = 'New York'")
    records = cursor.fetchall()
    for row in records:
        print(row)

    # 5) ORDER BY
    print("----------Order by age ----------")  #yaşa göre diz
    cursor.execute("SELECT * FROM Students ORDER BY age")
    records = cursor.fetchall()
    for row in records:
        print(row)

    # 6) LIMIT
    print("----------Limit by 3 ----------")
    cursor.execute("SELECT * FROM Students LIMIT 3")
    records = cursor.fetchall()
    for row in records:
        print(row)

def sql_update_delete_insert_operations(conn, cursor):
    #1) Insert
    cursor.execute("INSERT INTO Students VALUES (6, 'Frank Miller', 23, 'frank@gmail.com','Miami')")
    conn.commit()

    # 2) UPDATE
    cursor.execute("UPDATE Students SET age = 24 WHERE id = 6")
    conn.commit()

    #3) DELETE
    cursor.execute("DELETE FROM Students WHERE id = 6")
    conn.commit()

def aggregate_functions(cursor):
    #1) Count
    print("----------Aggregate Functions Count----------")
    cursor.execute("SELECT COUNT(*) FROM Students")
    result = cursor.fetchone()
    print(result[0])

    # 2) Average
    print("----------Aggregate Functions Average----------")
    cursor.execute("SELECT AVG(age) FROM Students")
    result = cursor.fetchone()
    print(result[0])

    # 3) MAX - MIN
    print("----------Aggregate Functions Max-Min----------")
    cursor.execute("SELECT MAX(age), MIN(age) FROM Students")
    result = cursor.fetchone()
    max_age, min_age = result
    print(max_age)
    print(min_age)

    # 4) GROUP BY
    print("----------Aggregate Functions Group by----------")
    cursor.execute("SELECT city, COUNT(*) FROM Students GROUP BY city")
    result = cursor.fetchall()
    print(result)
"""

def questions(cursor):

    #Basit

    print( "----1) Bütün kursların bilgilerini getirin?" )
    cursor.execute("SELECT * FROM Courses")
    records = cursor.fetchall()
    for row in records:
        print(f"id: {row[0]}, course_name: {row[1]}, instructor: {row[2]}, credits: {row[3]}")

    print( "----2) Sadece eğitmenlerin ismini ve ders ismi bilgilerini getirin? ")
    cursor.execute("SELECT course_name,instructor  FROM Courses")
    records = cursor.fetchall()
    print(records)

    print( "----3) Sadece 21 yaşındaki öğrencileri getirin? ")
    cursor.execute("SELECT * FROM Students WHERE age = 21")
    records = cursor.fetchall()
    for row in records:
        print(row)

    print ( "----4) Sadece Chicago'da yaşayan öğrencileri getirin?" )
    cursor.execute("SELECT * FROM Students WHERE city = 'Chicago' ")
    records = cursor.fetchall()
    for row in records:
        print(row)

    print(" 5) Sadece 'Dr. Anderson' tarafından verilen dersleri getirin?" )
    cursor.execute("SELECT course_name FROM Courses WHERE instructor = 'Dr. Anderson' ")
    records = cursor.fetchall()
    for row in records:
        print(row)

    print( "----6) Sadece ismi 'A' ile başlayan öğrencileri getirin" )
    cursor.execute( "SELECT * FROM Students WHERE name LIKE 'A%' ")
    records = cursor.fetchall()
    for row in records:
        print(row)

    print( "----7) Sadece 3 ve üzeri kredi olan dersleri getirin? " )
    cursor.execute("SELECT * FROM Courses WHERE credits >= 3 ")
    records = cursor.fetchall()
    for row in records:
        print(row)

    #Detaylı
    print("----1) Öğrencileri alphabetic şekilde dizerek getirin")
    cursor.execute("SELECT * FROM Students ORDER BY name ")
    records = cursor.fetchall()
    for row in records:
        print(row)

    print("----2) 20 yaşından büyük öğrencileri, ismine göre sıralayarak getirin")
    cursor.execute("SELECT name,age FROM Students WHERE age>=20 ORDER BY name ")
    records = cursor.fetchall()
    for row in records:
        print(row)

    print("----3) Sadece 'New York' veya 'Chicago' da yaşayan öğrencileri getirin")
    cursor.execute("SELECT name,city FROM Students WHERE city IN ('Chicago', 'New York') ")
    records = cursor.fetchall()
    for row in records:
        print(row)

    print("----4)Sadece 'New York' ta yaşamayan öğrencileri getirin")
    cursor.execute("SELECT name,city FROM Students WHERE city != 'New York' ")
    records = cursor.fetchall()
    for row in records:
        print(row)

def main():
    conn, cursor = create_database()

    try:
        create_tables(cursor)
        insert_sample_data(cursor)
        #basic_sql_operations(cursor)
        #sql_update_delete_insert_operations(conn, cursor)
        #aggregate_functions(cursor)
        questions(cursor)
        conn.commit()

    except sqlite3.Error as e:
        print(e)

    finally:
        conn.close()


if __name__ == "__main__":
    main()