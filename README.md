Late Show API

A Flask REST API for managing episodes, guests, and appearances from a late-night show. The API supports retrieving episodes and guests, viewing episode appearances, creating new appearances, and deleting episodes.

Technologies Used

Python

Flask

Flask SQLAlchemy

Flask Migrate

SQLite

SQLAlchemy Serializer

Flask CORS

Setup Instructions
Clone the Repository
git clone
cd lateshow-firstname-lastname

Install Dependencies
pip install -r requirements.txt

Database Setup
Run Migrations
Setup Database
Seed the Database
python seed.py

Running the Server
python app.py


The server will run on:

http://localhost:5555
