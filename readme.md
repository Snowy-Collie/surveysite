# Survey System

This is an open-source survey system built using Python, allowing users to create accounts, design and publish surveys, and complete surveys. The project is currently in progress and is being continuously improved.

## Features

- User Registration and Login
- Password Reset
- User Profile (to be added soon)
- Survey Creation, Publishing, and Completion (coming soon)

## Technologies Used

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python (Flask)
- **Database:** SQLite (for user data)
- **Libraries/Packages:**
  - Flask
  - SQLAlchemy
  - Flask-Bcrypt
  - Flask-CORS

## Installation

1. Clone this repository to your local machine.

    ```bash
    git clone https://github.com/Snowy-Collie/Survey-System.git
    cd survey-system
    ```

2. Install the required dependencies using `pip`.

    ```bash
    pip install -r requirements.txt
    ```

3. Run the application.

    ```bash
    python ./app.py
    ```

4. The system and website will be running locally on `http://127.0.0.1:5000`.

## Usage

Once the system is running, you can use the following endpoints:

- **POST** `/register` - Register a new user
- **POST** `/login` - Login with existing credentials
- **POST** `/reset-password` - Reset your password if forgotten

## Contributing

Feel free to fork this repository, open issues, and submit pull requests if you want to contribute. This project is open-source, and contributions are always welcome!

## License

This project is licensed under the MIT License.

