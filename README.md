#  Task Manager Web Application (Django)

##  Overview
This is a full-stack **Task Management Web Application** built using **Django** and deployed on **Railway**.

The system supports user authentication, role-based access (Admin & Member), project creation, and task management.

- Admins can create projects and manage tasks  
- Members can view and update assigned tasks  



##  Live Demo
 **Deployed URL:**  
https://web-production-731c3.up.railway.app/



##  Features

###  Authentication
- User Signup & Login
- Secure password handling
- Session-based authentication



###  Role Management
- Two roles: **Admin & Member**
- Role selection during signup
- Role-based access control



###  Project Management
- Admin can create projects
- View all projects


###  Task Management
- Create tasks under projects
- Update task status
- Assign tasks to users (Admin only)



###  Dashboard
- Role-based dashboard view
- Task and project overview



##  Tech Stack

- **Backend:** Django (Python)
- **Database:** PostgreSQL (Railway)
- **Frontend:** HTML, Bootstrap
- **Deployment:** Railway



##  Project Structure
    taskmanager/
    │── core/ # Main app
    │ ├── models.py # Database models (User, Profile, Task, Project)
    │ ├── views.py # Business logic
    │ ├── urls.py # App routes
    │ ├── templates/ # HTML templates
    │
    │── taskmanager/ # Project settings
    │ ├── settings.py
    │ ├── urls.py
    │
    │── manage.py




##  Installation & Setup (Local)

### 1️ Clone the repository

    git clone https://github.com/saba6309/team-task-manager
    cd taskmanager

###  2️ Create virtual environment

    python -m venv venv
    venv\Scripts\activate   # Windows

###  3️ Install dependencies

    pip install -r requirements.txt

###  4️ Run migrations

    python manage.py makemigrations
    python manage.py migrate

###  5️ Create superuser

    python manage.py createsuperuser

###  6️ Run server

    python manage.py runserver



##  Deployment (Railway)


### Connect GitHub repository to Railway

Add environment variables:

DATABASE_URL=your_postgres_url
SECRET_KEY=your_secret_key
Deploy automatically on push


## Roles Logic
Admin: Create projects, assign tasks, manage workflow

Member: View assigned tasks and update status



## Key Learnings
Django authentication system
Role-based access control
PostgreSQL integration
Deployment using Railway
Handling production errors



## Future Improvements
Task notifications
File attachments
REST API (Django REST Framework)
Better UI/UX
Charts & analytics dashboard


## Author

Shafia Saba
AI & ML Student



## License

This project is for educational purposes.
