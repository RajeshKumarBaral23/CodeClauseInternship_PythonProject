

# URL Shortener Project

## Overview

This project is a simple URL Shortener application that allows users to shorten long URLs for easier sharing and management. It is built using HTML, CSS, JavaScript for the frontend, Python for the backend, and MySQL for the database.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask framework)
- **Database**: MySQL

## Features

- Shorten long URLs
- Redirect from short URLs to original URLs
- Track number of clicks on each shortened URL

## Project Structure

```
URL-Shortener/
│
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── scripts.js
│
├── templates/
│   └── index.html
│
├── app.py
└── README.md
```

## Prerequisites

- Python 3.x
- MySQL Server
- pip (Python package installer)

## Installation and Setup

### Step 1: Clone the repository

### Step 2: Set up the virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install required Python packages

```bash
pip install flask flask-mysqldb
```

### Step 4: Set up the MySQL database

1. **Start MySQL Server**:
   Ensure your MySQL server is running.

2. **Create a Database**:
   ```sql
   CREATE DATABASE url_shortener;
   ```

3. **Import the Database Schema**:
   Use the schema provided in the `db.sql` file or create your own:
   ```sql
   CREATE TABLE urls (
       id INT AUTO_INCREMENT PRIMARY KEY,
       long_url TEXT NOT NULL,
       short_url VARCHAR(6) NOT NULL,
       clicks INT DEFAULT 0
   );
   ```

4. **Configure Database Connection**:
   Update the database configurations in `app.py` file with your database credentials:
   ```python
   app.config['MYSQL_HOST'] = 'localhost'
   app.config['MYSQL_USER'] = 'root'
   app.config['MYSQL_PASSWORD'] = 'root'
   app.config['MYSQL_DB'] = 'url_shortener'
   ```

### Step 5: Run the Application

```bash
python app.py
```

### Step 6: Access the Application

Open your web browser and navigate to `http://127.0.0.1:5000/`

## Usage

1. **Shorten a URL**:
   - Enter a long URL into the input field on the homepage and click "Shorten URL".
   - The application will generate a short URL and display it.

2. **Redirect**:
   - Use the generated short URL to be redirected to the original long URL.

## Project Files

- `app.py`: The main application file where the Flask app is created and routes are defined.
- `static/`: Contains static files such as CSS and JavaScript.
- `templates/`: Contains HTML template files.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. 


