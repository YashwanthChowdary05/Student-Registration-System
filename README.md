﻿# **Student-Registration-System Documentation**
## Overview
The Student Management System is a web-based application built using Flask, MySQL, and HTML/CSS. It allows users to register students, store their details in a MySQL database, and export student records to Excel and PDF formats.

## Project Structure
`
|-- app.py
|-- db_config.py
|-- templates/
|   |-- index.html
|-- static/
|-- students.xlsx (if exported)
|-- pdfs/
`

## Dependencies
- Flask
- WeasyPrint
- Pandas
- MySQL Connector
- Bootstrap (CDN)

## Installation & Setup
1. Install Python and MySQL.
2. Install dependencies using pip:
   `sh
   pip install flask weasyprint pandas mysql-connector-python
   `
3. Configure MySQL database with the credentials in `db_config.py`.
4. Run the Flask application:
   `sh
   python app.py
   `

## Database Configuration (db_config.py)
The application uses MySQL as the database. `db_config.py` contains:
- Database connection setup (`get_db_connection()`)
- Table creation (`create_table()`)
- Insert function (`insert_student()`)
- Fetch all records (`get_all_students()`)

### Database Schema
`
students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    class VARCHAR(20) NOT NULL,
    father_name VARCHAR(100),
    mother_name VARCHAR(100),
    phone VARCHAR(15) NOT NULL,
    email VARCHAR(100) NOT NULL
)
`

## Application Features
### 1. Student Registration (app.py)
- Accepts student details via an HTML form.
- Validates input fields:
  - Name, Father’s, and Mother’s names must be alphabetic.
  - Phone number must be numeric and at least 10 digits.
  - Email must be valid.
- Inserts valid data into the database.

### 2. Displaying Student Records (index.html)
- Fetches student details from the database.
- Displays records in an HTML table.
- Uses Bootstrap for styling.

### 3. Exporting Data
#### a. Export to Excel (update_excel function)
- Fetches all student records.
- Appends new records to `students.xlsx`.
- Prevents duplication.
- Returns a JSON response.

#### b. Export to PDF (export_pdf function)
- Captures the student records table as HTML.
- Converts HTML content into a PDF using WeasyPrint.
- Saves the file in the `pdfs/` directory.
- Provides a download option.

## API Endpoints
| Method | Route          | Description |
|--------|--------------|-------------|
| GET/POST | `/` | Displays form & processes student registration |
| POST | `/update-excel` | Exports student data to Excel |
| POST | `/export_pdf` | Exports student data to PDF |

## Usage Guide
1. Open `http://127.0.0.1:5000/` in a browser.
2. Fill out the student registration form.
3. Click `Submit` to save records.
4. Use `Export to Excel` or `Export to PDF` for data export.

## Future Enhancements
- Implement student record deletion and editing.
- Add user authentication.
- Enhance UI with additional Bootstrap elements.
- Implement pagination for large datasets.

## License
This project is open-source under the MIT License.

