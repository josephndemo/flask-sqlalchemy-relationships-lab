EventWise Flask-SQLAlchemy Relationships Lab
Overview

This project demonstrates how to build and manage relationships using Flask-SQLAlchemy in a Flask API application.

The application models an event management platform called EventWise, where:

Events contain Sessions
Speakers present Sessions
Speakers have Bios

The project includes:

One-to-Many relationships
One-to-One relationships
Many-to-Many relationships
Cascading deletes
RESTful API endpoints
Database migrations
Seed data
Automated tests
Technologies Used
Python 3
Flask
Flask-SQLAlchemy
Flask-Migrate
SQLAlchemy
SQLite
Pytest
Project Structure
.
├── server
│   ├── app.py
│   ├── models.py
│   ├── seed.py
│   ├── migrations/
│   ├── testing/
│   └── instance/
├── Pipfile
├── Pipfile.lock
└── README.md
Entity Relationship Diagram (ERD)
Relationships
One-to-Many
One Event has many Sessions
One Session belongs to one Event
One-to-One
One Speaker has one Bio
One Bio belongs to one Speaker
Many-to-Many
One Session has many Speakers
One Speaker can present many Sessions

This relationship is managed through the session_speakers association table.

Model Attributes
Event
Field	Type
id	Integer
name	String
location	String
Session
Field	Type
id	Integer
title	String
start_time	DateTime
event_id	Foreign Key
Speaker
Field	Type
id	Integer
name	String
Bio
Field	Type
id	Integer
bio_text	String
speaker_id	Foreign Key
Setup Instructions
1. Clone the Repository
git clone <repository-url>
2. Navigate Into the Project
cd flask-sqlalchemy-relationships-lab/server
3. Install Dependencies

Using pipenv:

pipenv install
pipenv shell

Or using pip:

pip install -r requirements.txt
Database Setup
Initialize Migrations
flask db init
Generate Migration
flask db migrate -m "Initial migration"
Apply Migration
flask db upgrade
Seed the Database

Run:

python seed.py

This inserts sample:

Events
Sessions
Speakers
Bios
Running the Application

Start the Flask server:

python app.py

The application runs on:

http://127.0.0.1:5555
API Endpoints
Events
GET /events

Returns all events.

Response Example
[
  {
    "id": 1,
    "name": "Tech Conference",
    "location": "New York"
  }
]
GET /events/<id>/sessions

Returns sessions for a specific event.

Success Response
[
  {
    "id": 1,
    "title": "Flask APIs",
    "start_time": "2026-05-20T10:00:00"
  }
]
Error Response
{
  "error": "Event not found"
}
Speakers
GET /speakers

Returns all speakers.

Response Example
[
  {
    "id": 1,
    "name": "Alice Johnson"
  }
]
GET /speakers/<id>

Returns a speaker and their bio.

Success Response
{
  "id": 1,
  "name": "Alice Johnson",
  "bio_text": "Backend engineer and Flask expert."
}
Speaker Without Bio
{
  "id": 2,
  "name": "Bob Smith",
  "bio_text": "No bio available"
}
Error Response
{
  "error": "Speaker not found"
}
Sessions
GET /sessions/<id>/speakers

Returns all speakers for a session.

Success Response
[
  {
    "id": 1,
    "name": "Alice Johnson",
    "bio_text": "Backend engineer and Flask expert."
  }
]
Error Response
{
  "error": "Session not found"
}

Author

Joseph Mokaya