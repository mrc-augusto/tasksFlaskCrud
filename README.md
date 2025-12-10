## Tasks Flask CRUD API

This project is a simple RESTful API for managing tasks, built with Flask. It supports full CRUD operations and includes automated tests using pytest.

### Features
- Create, read, update, and delete tasks
- Each task has an id, title, description, and completed status
- JSON responses with appropriate HTTP status codes
- Automated tests for all endpoints

### Requirements
- Python 3.7+
- Flask
- Flask-SQLAlchemy
- Flask-Cors
- Werkzeug
- pytest

Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the API
Activate your virtual environment and run:
```bash
python app.py
```
The API will be available at `http://127.0.0.1:5000`.

### License
This project is for educational purposes and is open source.