# Co-ToDo: A Django To-Do Application

A simple yet powerful To-Do list application built with the Django web framework. It allows users to register, log in, and manage their personal tasks in a clean and intuitive interface. This project demonstrates core Django concepts including user authentication, class-based views, and CRUD (Create, Read, Update, Delete) operations.

## Features

*   **Secure User Authentication**: Full registration, login, and logout functionality.
*   **Private Task Lists**: Each user can only see and manage their own tasks.
*   **Full CRUD Functionality**:
    *   **Create**: Add new tasks.
    *   **Read**: View a list of all tasks.
    *   **Update**: Mark tasks as complete or incomplete.
    *   **Delete**: Remove tasks from the list.
*   **Clean UI**: A user-friendly interface for easy task management.

## Tech Stack

*   **Backend**: Python, Django
*   **Frontend**: HTML, CSS
*   **Database**: SQLite (Django's default)

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   [Python 3.8+](https://www.python.org/downloads/)
*   [Pip](https://pip.pypa.io/en/stable/installation/) (usually comes with Python)
*   [Git](https://git-scm.com/)

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/djangoToDoApp.git
    cd djangoToDoApp
    ```

2.  **Create and activate a virtual environment:**
    *   On Windows:
        ```sh
        python -m venv venv
        .\venv\Scripts\activate
        ```
    *   On macOS/Linux:
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    This will create the `db.sqlite3` file and set up the necessary database tables.
    ```sh
    python manage.py migrate
    ```

5.  **Run the development server:**
    ```sh
    python manage.py runserver
    ```

6.  **Open the application:**
    Navigate to `http://127.0.0.1:8000/` in your web browser. You should see the login page.

## Usage

1.  Register for a new account using the "Register" link.
2.  Log in with your new credentials.
3.  You will be redirected to your personal to-do list.
4.  Use the input field to add new tasks.
5.  Click the `✓` button to toggle a task's completion status.
6.  Click the `×` button to delete a task.
7.  Click "Logout" when you are finished.

