# Online-Store

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Installation

***1. Create a virtual environment & activate it:***

```sh
python -m venv venv
venv\Scripts\activate
```
   
***2. Install project dependencies from requirements.txt:***
```sh
pip install -r requirements.txt
```

***3. Make necessary migrations:***
```sh
python manage.py makemigrations
python manage.py migrate
```

***4. Run the local server:***
```sh
python manage.py runserver
