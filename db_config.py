import mysql.connector

# Database Configuration
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "#Chowdary@536",
    "database": "student_db"
}

# Get a database connection
def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

# Create table if not exists
def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            class VARCHAR(20) NOT NULL,
            father_name VARCHAR(100),
            mother_name VARCHAR(100),
            phone VARCHAR(15) NOT NULL,
            email VARCHAR(100) NOT NULL
        )
    """)
    conn.commit()
    cursor.close()

# Insert student record
def insert_student(name, student_class, father_name, mother_name, phone, email):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, class, father_name, mother_name, phone, email) VALUES (%s, %s, %s, %s, %s, %s)", 
                       (name, student_class, father_name, mother_name, phone, email))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except mysql.connector.Error as e:
        print(f"Error inserting data: {e}")
        return False

# Fetch all students from the database
def get_all_students():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return students

