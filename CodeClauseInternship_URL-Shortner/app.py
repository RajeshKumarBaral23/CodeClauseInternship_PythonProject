from flask import Flask, request, redirect, make_response
from flask_mysqldb import MySQL
import MySQLdb.cursors
import random
import string

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345678'  # Replace with your MySQL password
app.config['MYSQL_DB'] = 'company'

# Initialize MySQL
mysql = MySQL(app)

def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route('/')
def index():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>URL Shortener</title>
        <link rel="stylesheet" type="text/css" href="/static/css/styles.css">
        <script src="/static/js/scripts.js" defer></script>
    </head>
    <body>
        <div class="container">
            <h1>URL Shortener</h1>
            <form action="/shorten" method="post">
                <label for="long_url">Enter URL to shorten:</label>
                <input type="text" id="long_url" name="long_url" required>
                <button type="submit">Shorten</button>
            </form>
        </div>
    </body>
    </html>
    '''
    return make_response(html)

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form['long_url']
    short_url = generate_short_url()
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('INSERT INTO urls (long_url, short_url) VALUES (%s, %s)', (long_url, short_url))
    mysql.connection.commit()
    cursor.close()
    short_url_full = request.host_url + short_url
    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>URL Shortener</title>
        <link rel="stylesheet" type="text/css" href="/static/css/styles.css">
        <script src="/static/js/scripts.js" defer></script>
    </head>
    <body>
        <div class="container">
            <h1>URL Shortener</h1>
            <p>Short URL is: <a href="{short_url_full}" target="_blank">{short_url_full}</a></p>
            <p>You can copy and paste this link into your browser to access the original URL.</p>
            <form action="/shorten" method="post">
                <label for="long_url">Enter URL to shorten:</label>
                <input type="text" id="long_url" name="long_url" required>
                <button type="submit">Shorten</button>
            </form>
        </div>
    </body>
    </html>
    '''
    return make_response(html)

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT long_url FROM urls WHERE short_url = %s', (short_url,))
    result = cursor.fetchone()
    cursor.close()
    if result:
        return redirect(result['long_url'])
    else:
        return 'URL not found', 404

if __name__ == '__main__':
    app.run(debug=True)