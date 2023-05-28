# Quiz Application

This is a quiz application that allows users to create and participate in timed quizzes. It provides a RESTful API for creating and retrieving quizzes.

## Tech Stack
```
- Python
- Django
```
## Installation

1. Clone the repository:
```
git clone https://github.com/Abhishek676062/quiz
```


2. Change into the project directory:

```
cd quiz-app
```

3. Create a virtual environment and activate it:

```
python -m venv venv
source venv/bin/activate
```


4. Install the dependencies:

```
pip install -r requirements.txt
```


5. Run database migrations:

```
python manage.py migrate
```


## Usage

1. Start the development server:


2. Access the application in your browser at `http://localhost:8000`.

3. Use the provided API endpoints to interact with the application:

- Create a quiz: `POST /quizzes`
- Get the active quiz: `GET /quizzes/active`
- Get the result of a quiz: `GET /quizzes/<quiz_id>/result`
- Get all quizzes: `GET /quizzes/all`

## Folder Structure

The project has the following folder structure:
```

├── quiz_app
│ ├── migrations
│ ├── static
│ ├── templates
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── urls.py
│ └── views.py
├── quiz_project
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── venv
├── manage.py
└── requirements.txt

```
