# Library Service

## Project Description

**Library Service** is a web application that enables users to manage library borrowings, process payments, and receive notifications via Telegram. Administrators have the ability to manage books, users, and monitor all borrowings.

## Technologies Used

- Python 3.x
- Django
- Celery
- Redis
- Docker

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/halyna-baklanova/library-service
   cd your-repositor

2. **Create a virtual environment:**
   It is recommended to create a virtual environment for isolation:

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # for Linux/MacOS
    .venv\Scripts\activate  # for Windows 

3. **Install dependencies**: Install all required libraries listed in requirements.txt:

    ```bash
    pip install -r requirements.txt
   
4. Setup environment variables: create a .env file in the project root directory with the following variables(example .env.sample)

5. **Run database migrations:**
    ```bash
    python manage.py migrate

6. **Start the server:**
    ```bash
    python manage.py runserver

7. **Create an admin user:**
    ```bash
    python manage.py createsuperuser

8. **Visit the site: Open your browser and go to:**
    ```bash
    http://localhost:8000

9. **Set up Docker:** run the following:

    ```bash
    docker-compose up --build


## Endpoints

- Admin Panel: `/admin/`
- Books Service API: `/api/book-service/`
- Customer API: `/api/user/`
- Borrowing Service API: `/api/borrowing/`


## Notifications Service (Telegram)

- Sending notifications about new borrowing created, borrowings overdue & successful payment
- Scheduled tasks for notifications about overdue borrowings using Сelery
- Telegram API integration

