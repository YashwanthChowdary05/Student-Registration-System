CREATE DATABASE student_db;
USE student_db;

CREATE USER 'root'@'localhost' IDENTIFIED BY '#Chowdary@536';
GRANT ALL PRIVILEGES ON student_db.* TO 'root'@'localhost';
FLUSH PRIVILEGES;

select * from students;


-- <style>
--         body {
--             font-family: 'Times New Roman', Times, serif;
--             background-color: #83aded;
--             color: solid black;
--         }

--         .container {
--             max-width: 950px;
--             margin: 0 auto;
--             padding: 40px;
--             background-color: #ffffff;
--             border-color: black;
--             border-radius: 12px;
--             box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
--         }

--         h2 {
--             font-size: 30px;
--             color: #1e2a3d;
--             font-weight: bold;
--             text-align: center;
--             margin-bottom: 30px;
--         }

--         h3 {
--             font-size: 24px;
--             color: #1e2a3d;
--             margin-top: 40px;
--             margin-bottom: 20px;
--         }

--         .form-label {
--             font-weight: bold;
--             color: #000000;
--         }

--         .form-control {
--             border-radius: 10px;
--             box-shadow: none;
--             border: 1px solid #ccc;
--             font-size: 16px;
--             padding: 12px;
--         }

--         .form-control:focus {
--             border-color: blue;
--             box-shadow: 0 0 5px rgba(67, 128, 194, 0.573);
--         }

--         .btn-primary {
--             background-color: rgb(62, 62, 255);
--             border: none;
--             padding: 12px 20px;
--             font-size: 18px;
--             border-radius: 10px;
--             cursor: pointer;
--         }

--         .btn-primary:hover {
--             background-color: rgb(41, 87, 255);
--         }

--         .alert {
--             font-size: 16px;
--             border-radius: 8px;
--             margin-bottom: 20px;
--         }

--         .alert.alert-success {
--             background-color: #d4edda;
--             color: #155724;
--         }

--         .alert.alert-danger {
--             background-color: #f8d7da;
--             color: #721c24;
--         }

--         table {
--             width: 100%;
--             margin-top: 30px;
--             border-collapse: collapse;
--         }

--         th, td {
--             padding: 14px;
--             text-align: left;
--             border-bottom: 1px solid #ddd;
--             font-size: 16px;
--         }

--         th {
--             background-color: #7ad47d;
--             color: white;
--             font-weight: bold;
--         }

--         tbody tr:nth-child(odd) {
--             background-color: #f9f9f9;
--         }

--         tbody tr:nth-child(even) {
--             background-color: #f1f1f1;
--         }

--         tbody tr:hover {
--             background-color: #f1f9f4;
--         }

--         .table-bordered {
--             border: 1px solid #ddd;
--         }

--         .table-bordered th, .table-bordered td {
--             border: 1px solid #ddd;
--         }
--     </style>