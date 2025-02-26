from flask import Flask, render_template, request, flash, redirect, jsonify
import re
import os
import pandas as pd
from db_config import get_db_connection, create_table, insert_student, get_all_students

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Ensure database table is created
with get_db_connection() as conn:
    create_table(conn)

# Regex pattern to allow only alphabetic characters (spaces allowed)
NAME_PATTERN = re.compile(r"^[A-Za-z\s]+$")

@app.route("/", methods=["GET", "POST"])
def index():
    students = get_all_students()
    form_data = request.form.to_dict()

    if request.method == "POST":
        name = form_data.get("name", "").strip()
        student_class = form_data.get("student_class", "").strip()
        father_name = form_data.get("father_name", "").strip()
        mother_name = form_data.get("mother_name", "").strip()
        phone = form_data.get("phone", "").strip()
        email = form_data.get("email", "").strip()

        errors = []

        if not name or not student_class or not phone or not email:
            errors.append("All required fields must be filled.")

        if not NAME_PATTERN.match(name):
            errors.append("Student Name should contain only alphabets.")

        if father_name and not NAME_PATTERN.match(father_name):
            errors.append("Father's Name should contain only alphabets.")

        if mother_name and not NAME_PATTERN.match(mother_name):
            errors.append("Mother's Name should contain only alphabets.")

        if not phone.isdigit() or len(phone) < 10:
            errors.append("Phone number should contain only digits and be at least 10 characters long.")

        if "@" not in email or "." not in email:
            errors.append("Invalid email format.")

        if errors:
            for error in errors:
                flash(error, "danger")
            return render_template("index.html", students=students, form_data=form_data)

        success = insert_student(name, student_class, father_name, mother_name, phone, email)
        if success:
            flash("Student record added successfully!", "success")
        else:
            flash("Failed to add record!", "danger")

        return redirect("/")

    return render_template("index.html", students=students, form_data={})

@app.route("/update-excel", methods=["POST"])
def update_excel():
    students = get_all_students()
    file_path = "students.xlsx"

    if not students:
        return jsonify({"message": "No student data available!", "status": "danger"})

    # Load existing data if the file exists
    if os.path.exists(file_path):
        existing_df = pd.read_excel(file_path)
        existing_ids = set(existing_df["ID"]) if "ID" in existing_df else set()
    else:
        existing_df = pd.DataFrame()
        existing_ids = set()

    # Convert new data into a DataFrame
    df = pd.DataFrame(students, columns=["ID", "Name", "Class", "Father Name", "Mother Name", "Phone", "Email"])
    
    # Filter out already existing records
    new_data = df[~df["ID"].isin(existing_ids)]

    if new_data.empty:
        return jsonify({"message": "No new student records to update in Excel!", "status": "warning"})

    # Append new data and save
    final_df = pd.concat([existing_df, new_data], ignore_index=True)
    final_df.to_excel(file_path, index=False)

    return jsonify({"message": "Excel file updated successfully!", "status": "success"})

if __name__ == "__main__":
    app.run(debug=True)
