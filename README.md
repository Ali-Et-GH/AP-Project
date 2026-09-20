# Skincare Recommendation Platform

A personalized skincare recommendation platform built with **Django** and **PostgreSQL**. The application helps users discover skincare products and generate personalized skincare routines based on their skin type, concerns, preferences, budget, and other personal factors.

## Features

- User registration, login, and logout
- Personalized skincare questionnaire
- Skin type and skin concern assessment
- Personalized skincare routine generation
- Product browsing and recommendations
- Product search and filtering
- Product ratings
- Like and view tracking
- Shopping cart and purchase management
- Browsing and purchase history
- Contextual user data tracking
- Image analysis data management
- Django admin panel

## Recommendation System

The platform uses information collected from the user's questionnaire and interactions to generate personalized skincare routines.

Recommendations can take into account:

- Skin type
- Skin concerns
- Eye concerns
- Age
- Product preferences
- Budget
- Dryness level
- Product interactions and history

## Technologies

- Python
- Django
- PostgreSQL
- Django ORM
- HTML
- CSS
- JavaScript

## Project Structure

The application is organized into several Django apps:

- `Home` – Main application page
- `Users` – Authentication, profiles, and shopping cart
- `Products` – Product management and recommendations
- `Quizzes` – Skincare questionnaire
- `Routines` – Personalized routine generation
- `History` – Browsing and purchase history
- `Contexts` – Contextual user information
- `Image_Analysis` – Skincare image analysis data
- `Choices` – Shared model choices and constants

## Getting Started

### 1. Clone the repository

    git clone <repository-url>
    cd Skincare_Recommendation_Platform

### 2. Install dependencies

    pip install -r requirements.txt

### 3. Configure PostgreSQL

Create a PostgreSQL database and update the database configuration in:

    Skincare_Recommendation_Platform/settings.py

### 4. Run migrations

    python manage.py migrate

### 5. Start the development server

    python manage.py runserver

Open `http://127.0.0.1:8000/` in your browser.
