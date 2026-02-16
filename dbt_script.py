import sqlite3
import os

DATABASE_NAME = 'db.sqlite3'

def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row  # This allows accessing columns by name
    return conn

def create_student(name, email, reg_no, course, batch, department, status):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO sms_app_student (name, email, reg_no, course, batch, department, status) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (name, email, reg_no, course, batch, department, status)
        )
        conn.commit()
        print("Student created successfully.")
    except sqlite3.IntegrityError as e:
        print(f"Error creating student: {e}. Email or Registration Number might already exist.")
    finally:
        conn.close()

def read_students():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sms_app_student")
    students = cursor.fetchall()
    conn.close()
    if students:
        print("
--- Student Records ---")
        for student in students:
            print(f"ID: {student['id']}, Name: {student['name']}, Email: {student['email']}, Reg No: {student['reg_no']}, Course: {student['course']}, Batch: {student['batch']}, Department: {student['department']}, Status: {student['status']}")
        print("-----------------------")
    else:
        print("No student records found.")

def update_student(student_id, name, email, reg_no, course, batch, department, status):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE sms_app_student SET name=?, email=?, reg_no=?, course=?, batch=?, department=?, status=? WHERE id=?",
            (name, email, reg_no, course, batch, department, status, student_id)
        )
        conn.commit()
        if cursor.rowcount > 0:
            print(f"Student with ID {student_id} updated successfully.")
        else:
            print(f"No student found with ID {student_id}.")
    except sqlite3.IntegrityError as e:
        print(f"Error updating student: {e}. Email or Registration Number might already exist.")
    finally:
        conn.close()

def delete_student(student_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM sms_app_student WHERE id=?", (student_id,))
    conn.commit()
    if cursor.rowcount > 0:
        print(f"Student with ID {student_id} deleted successfully.")
    else:
        print(f"No student found with ID {student_id}.")
    conn.close()

def main_menu():
    while True:
        print("
--- Student Database Menu ---")
        print("1. Create Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            reg_no = input("Enter registration number: ")
            course = input("Enter course: ")
            batch = input("Enter batch: ")
            department = input("Enter department: ")
            status = input("Enter status (active, inactive, suspended): ")
            create_student(name, email, reg_no, course, batch, department, status)
        elif choice == '2':
            read_students()
        elif choice == '3':
            student_id = input("Enter student ID to update: ")
            name = input("Enter new name: ")
            email = input("Enter new email: ")
            reg_no = input("Enter new registration number: ")
            course = input("Enter new course: ")
            batch = input("Enter new batch: ")
            department = input("Enter new department: ")
            status = input("Enter new status (active, inactive, suspended): ")
            update_student(student_id, name, email, reg_no, course, batch, department, status)
        elif choice == '4':
            student_id = input("Enter student ID to delete: ")
            delete_student(student_id)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()