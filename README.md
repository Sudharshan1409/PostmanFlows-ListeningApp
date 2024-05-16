# Flask Application

This is a Flask web application that includes basic functionalities such as managing blog posts and handling Dropbox webhooks. The application uses SQLite for its database and Flask-Migrate for handling database migrations.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Adding a New API](#adding-a-new-api)
- [Adding a New Database Model](#adding-a-new-database-model)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.7+
- Virtualenv (optional but recommended)

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/yourrepository.git
    cd yourrepository
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Migrate Database:
    ```bash
    flask db migrate -m "Initial migration"
    ```

5. Set up the database:
    ```bash
    flask db upgrade
    ```

6. Run the application:
    ```bash
    python app.py
    ```

## Usage

- Open your browser and navigate to `http://localhost:8000` to view the home page.

## Adding a New API

Please refer to [API.md](API.md) for instructions on adding a new API.

## Adding a New Database Model

Please refer to [DatabaseModels.md](DatabaseModels.md) for instructions on adding a new database model.

## Contributing

Feel free to open issues or submit pull requests if you have any improvements or bug fixes.
