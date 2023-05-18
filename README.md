# EasyLedger

EasyLedger: Built to keep simple financial record such cash flow statement, income statement and balance sheet for Vivirgros. EasyLedger is a web application built using Flask, Jinja templating, Flask-SQLAlchemy, PostgreSQL, and Flask-Migrate.

## Features

- Keep track of financial records including cash flow statements, balance sheets, and income statements.
- User-friendly interface for managing financial data.
- Seamless integration with PostgreSQL database for data storage.
- Flask-Migrate allows for smooth database migrations.

## Installation

1. Clone the repository:

    ```Copy code
    git clone https://github.com/your-username/easyledger.git
    ```

2. Create a virtual environment (optional but recommended):

    ***For Windows***

    ```Copy code
    python3 -m venv env
    source env/scripts/activate
    ```

    ***For Mac***

    ```Copy code
    python3 -m venv env
    source env/bin/activate
    ```

3. Install the required dependencies:

    ***Install `pipenv`***

    ```Copy code
    pip install pipenv
    ```

    ***and the install dependencies***

    ```Copy code
    pipenv install
    ```

4. Set up the database:

    - Make sure you have PostgreSQL installed and running.
    - Create a new database for EasyLedger.

5. Configuration:

    - Rename the `.env.example` file to `.env`.
    - Update the `.env` file with your database credentials and other settings.

6. Run database migrations:

    ```Copy code
    flask db upgrade
    ```

7. Start the application:

    ***For Windows***

    ```Copy code
    export FLASK_APP=src/server.py
    ```

    ```Copy code
    export FLASK_DEBUG=True
    ```

    ***For Mac***

    ```Copy code
    set FLASK_APP=src/server.py
    ```

    ```Copy code
    set FLASK_DEBUG=True
    ```

    `To run app`

    ```Copy code
    python src/server.py
    ```

8. Open your web browser and visit `http://localhost:5000` to access EasyLedger.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please create a new issue or submit a pull request.

## License

This project is licensed under the [Apache License](LICENSE).
