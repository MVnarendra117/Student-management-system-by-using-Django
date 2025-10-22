🎓 Student Management System

A Full-Stack Django Web Application for Managing Students and Teachers Efficiently

Overview

The Student Management System is a full-stack web application built using Python Django that enables administrators to seamlessly manage students and teachers within a school environment.
It provides a secure login system, intuitive UI, and complete CRUD (Create, Read, Update, Delete) operations for both student and teacher data.
The project demonstrates strong backend logic, clean frontend design, and real-world database integration.




🚀 Key Features

👥 Student & Teacher Management – Add, edit, view, and delete records dynamically.

🔐 User Authentication – Secure login and signup system powered by Django’s built-in authentication module.

🧱 CRUD Operations – Fully functional database operations for managing user data.

🧩 Modular Architecture – Separate apps for accounts and student for cleaner project structure.

🎨 Responsive Frontend – Built using HTML, CSS, and Bootstrap for a clean and mobile-friendly interface.

⚙️ Admin Dashboard – Leverages Django Admin for quick management and data overview.

🗄️ Database Integration – Uses Django ORM with SQLite3 for seamless data storage and querying.


🗂️ Project Structure

school/
│
├── accounts/                # Handles user authentication (login, registration)
├── student/                 # Student & teacher CRUD logic, forms, templates
├── static/                  # CSS stylesheets and images
│   ├── css/
│   └── images/
├── templates/               # HTML templates
│   ├── registration/        # Login & Signup pages
│   ├── student/             # Student templates
│   ├── teacher/             # Teacher templates
│   └── welcome.html         # Home page
├── school/                  # Project configuration (settings, URLs, WSGI)
│   ├── settings.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3               # Local database
├── manage.py                # Django CLI entry point
└── requirements.txt         # (Dependencies list)



🧰 Tech Stack
Layer	Technology
Frontend	HTML5, CSS3, Bootstrap
Backend	Python, Django
Database	SQLite3
Tools	Git, VS Code / PyCharm
Version Control	Git & GitHub


⚙️ Installation and Setup

Follow these steps to run the project locally 👇

1. Clone the Repository
   git clone https://github.com/MVnarendra117/student-management-system.git
   cd student-management-system

2. Create a Virtual Environment
   python -m venv venv
   venv\Scripts\activate

3. Install Dependencies
   pip install -r requirements.txt

4. Run Migrations
   python manage.py makemigrations
   python manage.py migrate

5. Create a Superuser (Admin Access)
   python manage.py createsuperuser

6. Start the Development Server
   python manage.py runserver


🧠 Learning Outcomes

Gained hands-on experience in Django MVC architecture and database modeling.

Learned to design modular, reusable Django apps for scalable project development.

Improved front-end design and UI/UX consistency using Bootstrap and CSS.

Strengthened knowledge of CRUD operations, ORM handling, and authentication systems.
