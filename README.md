# Time Tracker

A Django-based time tracking application that allows users to track time spent on tasks with a simple interface.

## Features

- Start/pause/stop timer functionality
- Manual time entry option
- Time logs overview with search and pagination
- Docker support for easy setup

## Installation

### Using Docker

1. Clone the repository:
```bash
git clone <repository-url>
cd time_tracker
```

2. Build and run the Docker containers:
```bash
docker-compose up --build
```

3. In a new terminal, run migrations:
```bash
docker-compose exec web python manage.py migrate
```

4. Create a superuser:
```bash
docker-compose exec web python manage.py createsuperuser
```

### Manual Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd timetracker
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver 8080
```

## Usage

1. Access the application at http://localhost:8080
2. Log in with your superuser credentials
3. Use the timer to track time or add manual time entries
4. View and search your time logs in the logs section

## Development Notes

Sure! Here’s a concise version in English:

- **Time spent**: 2 weeks
  - I dedicated two weeks to designing, developing, and testing the time tracking application, allowing me to focus on each feature while ensuring code quality.

- **Liked aspects**: 
  - I enjoyed working with Django for its clear structure and powerful tools for rapid web application development. Implementing the timer and time log management was a rewarding challenge.

- **Areas for improvement**: 
  - While the application is functional, the user interface could be enhanced with a more modern and responsive design. Additionally, adding unit and integration tests would strengthen the application's robustness.

- **Future enhancements**: 
  - With more time, I would like to integrate features such as visualizations of time spent on tasks, notifications to remind users to start or stop tracking, and a more advanced authentication system for user management.
