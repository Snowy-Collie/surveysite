# PolarForm

This is an open-source survey system built using Python, allowing users to create accounts, design and publish surveys, and complete surveys. The project is currently in progress and is being continuously improved.

<p align="center">
    <img src="./static/logo.png" alt="PolarForm" style="width: 150px; height: 150px;">
</p>

<p align="center">
<a href="https://github.com/Snowy-Collie/Survey-System/blob/main/LICENSE" target="_blank">
<img src="https://img.shields.io/github/license/Snowy-Collie/Survey-System?style=flat-square" alt="licence" />
</a>
<a href="https://github.com/Snowy-Collie/Survey-System/fork" target="_blank">
<img src="https://img.shields.io/github/forks/Snowy-Collie/Survey-System?style=flat-square" alt="forks"/>
</a>
<a href="https://github.com/Snowy-Collie/Survey-System/stargazers" target="_blank">
<img src="https://img.shields.io/github/stars/Snowy-Collie/Survey-System?style=flat-square" alt="stars"/>
</a>
<a href="https://github.com/Snowy-Collie/Survey-System/issues" target="_blank">
<img src="https://img.shields.io/github/issues/Snowy-Collie/Survey-System?style=flat-square" alt="issues"/>
</a>
<a href="https://github.com/Snowy-Collie/Survey-System/pulls" target="_blank">
<img src="https://img.shields.io/github/issues-pr/Snowy-Collie/Survey-System?style=flat-square" alt="pull-requests"/>
</a>
</p>

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

3. Generate a secret key for app.py and replace the output key into app.py.

    ```bash
    python ./generate_secret_key.py
    ```

4. Run the application.

    ```bash
    python ./app.py
    ```

5. The system and website will be running locally on `http://127.0.0.1:5000`.

## Usage

Once the system is running, you can use the following endpoints:

- **POST** `/register` - Register a new user
- **POST** `/login` - Login with existing credentials
- **POST** `/reset-password` - Reset your password if forgotten

## Contributing

Feel free to fork this repository, open issues, and submit pull requests if you want to contribute. This project is open-source, and contributions are always welcome!

## License

This project is licensed under the MIT License.

