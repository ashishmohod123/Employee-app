Employee Management System

A simple Employee Management System built using Python, Flask, SQLite, HTML, and CSS. This application demonstrates basic CRUD (Create, Read, Update, Delete) operations with a clean and user-friendly interface.

Features

- Add New Employee
- View Employee List
- Edit Employee Details
- Delete Employee Records
- SQLite Database Integration
- Responsive and Simple UI

Technologies Used

- Python
- Flask
- SQLite3
- HTML5
- CSS3

Project Structure

Employee-Management-System/
│
├── app.py
├── employees.db
├── requirements.txt
├── README.md
│
├── static/
│   └── style.css
│
└── templates/
    ├── index.html
    ├── add.html
    └── edit.html

Installation

1. Clone the repository

git clone https://github.com/your-username/Employee-Management-System.git

2. Navigate to the project directory

cd Employee-Management-System

3. Install the required package

pip install -r requirements.txt

4. Run the application

python app.py

5. Open your browser and visit:

http://127.0.0.1:5000/

Database

The application automatically creates an SQLite database named employees.db with the following table:

Column| Type
id| INTEGER (Primary Key)
name| TEXT
dept| TEXT
salary| INTEGER

Future Enhancements

- Employee Search
- User Authentication
- Pagination
- Sorting & Filtering
- Bootstrap UI
- Form Validation
- Flash Messages
- REST API

Author

Ashish Mohod

Python Backend Developer

License

This project is developed for learning and educational purposes.