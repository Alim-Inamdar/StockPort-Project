import sqlite3
import pyodbc


def get_db_connection():
    server = 'your-server-name.database.windows.net'
    database = 'stock_portfoliodb'
    username = 'your-username'
    password = 'your-password'
    driver = '{ODBC Driver 17 for SQL Server}' 
    
    # Create the connection string
    connection_string = f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}'
    
    # Connect to the Azure SQL Database
    conn = pyodbc.connect(connection_string)
    return conn

# Functions to handle user login validation
def validate_login(username, password):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
    conn.close()
    return user

# Functions to create a new user
def create_user(username, password):
    conn = get_db_connection()
    conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()

# Functions to add a stock to a user's portfolio
def add_stock_to_portfolio(user_id, stock_data):
    conn = get_db_connection()
    conn.execute('INSERT INTO portfolio (user_id, stock_name, stock_price) VALUES (?, ?, ?)',
                 (user_id, stock_data['stock_name'], stock_data['stock_price']))
    conn.commit()
    conn.close()

# Functions to retrieve a user's portfolio
def get_portfolio(user_id):
    conn = get_db_connection()
    stocks = conn.execute('SELECT * FROM portfolio WHERE user_id = ?', (user_id,)).fetchall()
    conn.close()
    return stocks

