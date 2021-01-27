# Library Management System

This project is a library management system implemented with Python and MySQL. It includes command-line functionality for managing users, books, and transactions. The system supports operations such as user registration, login, borrowing books, and more.

## Project Structure
The project is organized into the following directories:

```
.
├── code
│   ├── Pipfile
│   ├── Pipfile.lock
│   ├── main.py                 # Command-line interface for library system operations
│   └── test_library_system.py  # Testing script for stored procedures (future work includes automating the tests)
└── sql
    ├── functions.sql           # SQL file defining functions used in the database
    ├── tables.sql              # SQL file defining database tables
    └── tests.sql               # SQL file with test queries and data
```

## Requirements
To set up and run this project, you will need the following:
- Python 3.8+
- Pipenv (for managing Python dependencies)
- MySQL

### Setting up the Python Environment
To install the required dependencies, run the following commands in the `code` directory:

```
cd code
pipenv install
```

This will create a virtual environment and install the dependencies specified in the `Pipfile`.

### Database Setup
To set up the MySQL database schema, execute the SQL scripts in the following order:

1. **Create tables**: Run the `tables.sql` script to set up the initial database schema.

```
mysql -u <username> -p <database> < sql/tables.sql
```

2. **Define functions**: After setting up the tables, execute the `functions.sql` script to create necessary functions.

```
mysql -u <username> -p <database> < sql/functions.sql
```

3. **Run tests**: Finally, you can execute the `tests.sql` script to run any test queries and validate the setup.

```
mysql -u <username> -p <database> < sql/tests.sql
```

### Running the Command-Line Interface
You can interact with the library system through the command-line interface (`main.py`). To start the system, run the following command:

```
pipenv run python main.py
```

You can then use commands like `register`, `login`, `add_book`, `borrow_book`, etc.

### Testing the System
The `test_library_system.py` file contains test cases for the system. To run the existing tests manually, you can execute specific functions by modifying the `main()` function in `test_library_system.py`. Automated tests will be introduced in the future to streamline the testing process.
