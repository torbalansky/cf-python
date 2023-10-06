# Imports MySQL connector
import mysql.connector

# Initializes connection to the MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="cf-python",
    passwd="password"
)

# Initializes the cursor object from the connection
cursor = conn.cursor()

# Creates the database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")

# Connects to the database using the USE statement
cursor.execute("USE task_database")

# Creates the Recipes table with specified columns
cursor.execute("CREATE TABLE IF NOT EXISTS Recipes ("
               "id INT AUTO_INCREMENT PRIMARY KEY,"
               "name VARCHAR(50),"
               "ingredients VARCHAR(255),"
               "cooking_time INT,"
               "difficulty VARCHAR(20)"
               ")")
