# Django Hello World with Material Dashboard

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/nherriot/hello_world_project/tree/master.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/nherriot/hello_world_project/tree/master)

This is a simple Django application integrated with Creative Tim's Material Dashboard, featuring a styled "Hello World" page with a sidebar, navbar, button, and table. The project includes pytest for testing, WhiteNoise for static file serving, and CircleCI for continuous integration.

## Prerequisites

- **Python 3.12** or higher
- **Git**
- A Unix-like system (e.g., Ubuntu, macOS) or Windows with WSL
- (Optional) A virtual environment tool like `venv`

## Setup Instructions

### 1. Clone the Repository
Clone the project to your local machine:

```bash
git clone git@github.com:<username>/<repo>.git
cd hello_world_project
```

Replace `<username>/<repo>` with your GitHub username and repository name.

### 2. Set Up a Python Virtual Environment
Create and activate a virtual environment to isolate dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Linux/macOS
# or
.\venv\Scripts\activate  # On Windows
```

### 3. Install Python Packages
Install the required packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

This installs Django, Uvicorn, WhiteNoise, pytest, pytest-django, and other dependencies.

### 4. Run the Development Server
Start the Django development server to test the application:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser. You should see the "Hello World" page with a Material Dashboard sidebar, navbar, button, and table.

## Running Tests

The project includes pytest tests to verify the "Hello World" view and UI components.

1. Ensure the virtual environment is activated:
   ```bash
   source venv/bin/activate  # On Linux/macOS
   # or
   .\venv\Scripts\activate  # On Windows
   ```

2. Run the tests:
   ```bash
   pytest
   ```

You should see output indicating that tests (e.g., `test_hello_world_view`, `test_click_me_button`) have passed.

## Running with Uvicorn and Collecting Static Files

For a production-like setup or to test with `DEBUG = False`, use Uvicorn (an ASGI server) and collect static files for WhiteNoise.

1. **Collect Static Files**:
   Ensure static files (e.g., Material Dashboard CSS, JS, favicon) are copied to `staticfiles/`:
   ```bash
   python manage.py collectstatic
   ```
   Type `yes` when prompted.

2. **Run Uvicorn**:
   Start the application with Uvicorn:
   ```bash
   uvicorn hello_world_project.asgi:application --host 0.0.0.0 --port 8000
   ```

3. **Test the Application**:
   Visit `http://127.0.0.1:8000/`. The app should load with all styling and functionality (sidebar, navbar, button, table, favicon).

4. **Test with `DEBUG = False`** (Optional):
   - Edit `hello_world_project/settings.py` and set `DEBUG = False`.
   - Re-run `collectstatic` and Uvicorn.
   - Verify the app loads correctly, with WhiteNoise serving static files.

## Project Structure

- `hello_app/`: Contains the Django app with views, templates, and tests.
- `hello_world_project/`: Django project settings, ASGI/WSGI config.
- `static/`: Source static files (e.g., Material Dashboard assets).
- `staticfiles/`: Collected static files for production.
- `.circleci/config.yml`: CircleCI configuration for CI/CD.
- `requirements.txt`: Python dependencies.
- `pytest.ini`: Pytest configuration.

## Contributing

Feel free to fork the repository, create a feature branch, and submit a pull request. Ensure tests pass and add new tests for new features.

## License

This project is licensed under the MIT License.


