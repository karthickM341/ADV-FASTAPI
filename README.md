# Advanced FastAPI Application (Doctors, Patients & Appointments)

# Project Overview

This project is a fully functional backend system built using **FastAPI**.
It manages **Doctors, Patients, and Appointments** with authentication, database integration, and modular architecture.

# Features
# Doctor Module

* Create, Update, Delete Doctors
* Filter doctors by specialization
* Activate / Deactivate doctor

# Patient Module

* Create, Update, Delete Patients
* Search patients by name or phone

# Appointment Module

* Create appointment (Doctor ↔ Patient)
* View all appointments
* Get appointments by doctor or patient
* Cancel appointment

# Authentication

* JWT-based login system
* Secure APIs (except login)

# Additional Features

* Pagination support
* Structured project architecture
* SQLite database with SQLAlchemy ORM
* Logging support
* Environment variable configuration

# Tech Stack

* Python 3.9+
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Uvicorn
* JWT (python-jose)
* Passlib (bcrypt)

#API Documentation

Once server is running, open:
Swagger UI
http://127.0.0.1:8000/docs


---
