# English Vocabulary Memorisation Program

Welcome to the **English Vocabulary Memorisation Program**, a web application developed as a project assignment for the Software Construction course. This project is built using **Python-Django** technologies and aims to assist users in effectively learning and memorising English vocabulary.

## Features

- **User Authentication**: Users can register and log in to their accounts.
- **Randomised Quiz**: A quiz of 10 random words is presented to users upon login.
- **Progress Tracking**: Each correct answer increases the word's score by 1 point.
- **Learning Completion**: Words with 6 points are considered fully learned and will no longer appear in quizzes.
- **Adaptive Spaced Repetition**: The occurrence of a word is managed by an algorithm that follows specific intervals:
  - 1 day
  - 1 week
  - 1 month
  - 3 months
  - 6 months
  - 12 months
- **Dynamic Styling**: The project includes customised CSS for a visually appealing user interface.

---

## Project Structure

```
├── README.md
├── db.sqlite3
├── denem.py
├── eski.py
├── manage.py
├── models.py
├── projeinfo.txt
├── static/
│   └── css/
│       ├── login.css
│       ├── register.css
│       └── resetP.css
├── templates/
│   ├── home.html
│   └── partials/
│       ├── login.html
│       ├── main.html
│       ├── nav.html
│       ├── register.html
│       ├── reset_password.html
│       └── user.html
├── wordDemo/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── __pycache__/
│   └── migrations/
│       ├── 0001_initial.py
│       ├── 0002_correctanswers_correct_count_and_more.py
│       ├── __init__.py
│       └── __pycache__/
└── wordProgram/
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    ├── wsgi.py
    └── __pycache__/
```

---

## How It Works

1. **User Registration and Login**:
   - Users create an account and log in to access the application.

2. **Quiz**:
   - Upon login, a quiz with 10 random words appears.
   - Users select the correct meaning for each word.

3. **Scoring System**:
   - For every correct answer, the word's score increases by 1 point.
   - Words with 6 points are marked as fully learned and excluded from future quizzes.

4. **Spaced Repetition Algorithm**:
   - Words reappear based on the following intervals: 1 day, 1 week, 1 month, 3 months, 6 months, and 12 months.
   - Words do not appear more than once on the same day.

---

## Technologies Used

- **Backend**: Python-Django
- **Frontend**: HTML, CSS
- **Database**: SQLite

---

## Installation

To set up and run the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/dirshaye/english-word-memorization.git
   cd english-word-memorization
   ```

2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   Open your web browser and go to `http://127.0.0.1:8000`.

---

## Future Improvements

- Add more advanced quiz types and difficulty levels.
- Implement user statistics and progress dashboards.
- Integrate audio pronunciation for words.
- Provide multilingual support.

---

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

## Contributors

- [Dirshaye](https://github.com/dirashye)
- [Meric Dogan](https://github.com/miracdogann)
- [Mucahit çaliş](https://github.com/mchtx)

Feel free to contribute to this project by submitting issues or pull requests!

