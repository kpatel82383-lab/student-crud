\# Student CRUD API



This project is a simple Student CRUD application developed using FastAPI.



\## Features



\- Create a student

\- View all students

\- View a student by ID

\- Update a student

\- Delete a student



\## Technologies Used



\- Python

\- FastAPI

\- Pydantic

\- Uvicorn



\## Project Structure



student-crud/

\- main.py

\- models/

\- routes/

\- controllers/

\- requirements.txt

\- README.md



\## How to Run



Install the required packages:



pip install -r requirements.txt



Run the application:



uvicorn main:app --reload



Open the API documentation:



http://127.0.0.1:8001/docs



\## API Endpoints



POST /students - Create a student

GET /students - Get all students

GET /students/{id} - Get student by ID

PUT /students/{id} - Update a student

DELETE /students/{id} - Delete a student

