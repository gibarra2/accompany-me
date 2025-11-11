# Acompáñame

Acompáñame (accompany me) is a web app where users can collaborate with others to plan group vacations.

Users can create accounts, create trips including other users, and add places to visit for their trips. On their trip pages, users can view a map with markers for every location they plan to visit. This can help users group activities which are geographically close together. Furthermore, users can build out their itineraries, which are then visualized as a timeline on their trip page.

Acompáñame was created as a capstone project for Ada Developers Academy.

This repository holds the backend code. The front end repository is [accompany-me-frontend](https://github.com/gibarra2/accompany-me-frontend).

## Demo

[![Thumbnail image of demo video for Acompáñame](https://img.youtube.com/vi/Ich7joHgOiA/0.jpg)](https://youtu.be/Ich7joHgOiA?si=4-8UhKqskR_JSS-D&t=42)

## Tech Stack

### Backend

- Django
- Django REST Framework
- MySQL

### Frontend

- React
- Material UI

## Setup

1. Clone this repository.
2. Create a virtual environment with the venv module or your tool of choice.

```bash
$ python3 -m venv venv
```

3. Activate the virtual environment and install the dependencies from the requirements.txt file.

```bash
$ source venv/bin/activate
$ pip install -r requirements.txt
```

4. Create a local database and update the DATABASES field in `backend/settings/dev.py`.
5. Apply migrations to the database.

```bash
$ python manage.py migrate
```

6. Use the following command to run your local server.

```bash
$ python manage.py runserver
```

7. This app makes use of geocoding from the [LocationIQ API](https://locationiq.com/geocoding). If you would like to use this feature you must request an API Key from their website.
