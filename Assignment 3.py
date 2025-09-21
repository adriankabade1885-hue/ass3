"""R244530h"""
"Assignment 3"

def classify_number(num):
    """Classify a number as Positive, Negative, or Zero."""
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"


"""Keep asking until valid integer is entered"""
while True:
    user_input = input("Enter an integer: ")
    try:
        number = int(user_input)  # try converting to integer
        print("Classification:", classify_number(number))
        break  # exit loop after valid integer is entered
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

"Question 2"
def calculate_average(*args):
    """
    Calculates the average of a variable number of numeric arguments.

    Parameters:
        *args (int or float): One or more numeric values.

    Returns:
        float: The average of the input numbers.
        None: If no arguments are provided.

    Example:
        >>> calculate_average(1, 3, 18)
        9.0
    """
    if not args:
        return None  # Avoid division by zero

    total = sum(args)
    count = len(args)
    return total / count

"Question 3"
def get_valid_number():
    """
    Continuously prompt the user for a number until a valid one is entered.

    Uses a try-except block to handle invalid (non-numeric) input.
    """
    while True:
        try:
            number = float(input("Enter a number: "))
            print(f"You entered: {number}")
            return number
        except ValueError:
            print("You've entered invalid input! Please enter a correct number.")

# Run the program
get_valid_number()


"Question 4"
# Write the names to a file called names.txt
with open("names.txt", "w") as file:
    file.write("Tatenda\n")
    file.write("Jonathan\n")
    file.write("Chipo\n")
    file.write("Alex\n")
    file.write("Adrian\n")

# Read the file and print each name to the console
with open("names.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes the newline character


"Question 5"

"sample list of Celsius temperatures"
celsius_temps = [1, 2, 3, 40, 10]

# Use lambda and map to convert Celsius to Fahrenheit
fahrenheit_temps = list(map(lambda c: c * 9/5 + 32, celsius_temps))

# Print the converted list
print("Celsius temperatures:", celsius_temps)
print("Fahrenheit temperatures:", fahrenheit_temps)


"question 6"

def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Both numerator and denominator must be numbers.")
        print(divide_numbers(20, 2))  # Output: 10.0
        print(divide_numbers(20, 0))  # Output: Error: Cannot divide by zero.
        print(divide_numbers("20", 2))  # Output: Error: Both numerator and denominator must be numbers.


"Question 7"
# Define a custom exception
class NegativeNumberError(Exception):
    """Exception raised when a negative number is encountered."""
    pass

# Function to check if a number is positive
def check_positive(number):
    if number < 0:
        raise NegativeNumberError("Error: Negative numbers arent acceptable, try again.")
    else:
        print(f"{number} is positive.")

# Example usage
try:
    check_positive(15)   # ✅ Will print "15 is positive."
    check_positive(-15)   # ⚠ Will raise NegativeNumberError
except NegativeNumberError as e:
    print(e)

    "Question 8"

    import random


    # Function to generate a list of random integers
    def generate_random_numbers(count, start, end):
        return [random.randint(start, end) for _ in range(count)]


    # Function to calculate the average of a list
    def calculate_average(numbers):
        return sum(numbers) / len(numbers)


    # Main program
    random_numbers = generate_random_numbers(10, 1, 100)
    average = calculate_average(random_numbers)

    print("Generated numbers:", random_numbers)
    print("Average:", average)


"Question 9"

import re

# I. Extract all email addresses from a given text
def extract_emails(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(pattern, text)

# II. Validate a date in the format "YYYY-MM-DD"
def validate_date(date_str):
    pattern = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$"
    return bool(re.match(pattern, date_str))

# III. Replace all occurrences of a word with another word
def replace_word(text, old_word, new_word):
    pattern = rf"\b{old_word}\b"
    return re.sub(pattern, new_word, text)

# IV. Split a string by all non-alphanumeric characters
def split_non_alphanumeric(text):
    pattern = r"[^a-zA-Z0-9]+"
    return [word for word in re.split(pattern, text) if word]

# -------------------------------
# Demonstration
# -------------------------------

sample_text = "Contact us at support@example.com or sales@example.org."
print("Extracted emails:", extract_emails(sample_text))

print("Valid date (2025-09-12):", validate_date("2025-09-12"))
print("Invalid date (2025-13-40):", validate_date("2025-13-40"))

sentence = "Zimbabweans are awesome"
print("Replaced text:", replace_word(sentence, "Zimbabweans", "Americans"))

split_text = "Hello, world! +_2.63 is awesome."
print("Split result:", split_non_alphanumeric(split_text))

Extracted emails: ['support@example.com', 'sales@example.org']
Valid date (2025-09-12): True
Invalid date (2025-13-40): False
Replaced text: Americans are awesome
Split result: ['Hello', 'world', '+', '2', '63', 'is', 'awesome']


"Question 10"

import socket

def start_server(host="127.0.0.1", port=65432):
    try:
        # Create a TCP/IP socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(1)

        print(f"Server is listening on {host}:{port} ...")

        # Wait for a connection
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")

        # Send a welcome message
        message = "Hello from server!"
        conn.sendall(message.encode())

        # Close the connection
        conn.close()
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()

"Question 11"
"API stands for Application Programming Interface"
" is a set of rules and protocols that allows different software applications to communicate with each otheR"
"It acts as a messenger or intermediary between them to exchange data"
"It does this without needing to know the internal workings of the other system"
"eg in Zim context"
"APIS Can be used to"
"Access exchange rates for the Zimbabwean dollar from financial services."


"Question 12"
import sqlite3

# Step 2: Connect
connection = sqlite3.connect("example.db")

# Step 3: Create cursor
cursor = connection.cursor()

# Step 4: Execute SQL commands
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Adrian", 25))

# Step 5: Commit changes
connection.commit()

# Step 6: Fetch data
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Step 7: Close connection
connection.close()



"explanation"
#Connecting to a SQLite Database using Python
#To connect to a SQLite database using Python, you'll need to follow these steps:

#Step 1: Import the sqlite3 Module
#- Purpose: The sqlite3 module is a built-in Python library that provides a SQL database engine.
#- Code: import sqlite3

#Step 2: Establish a Connection
#- Purpose: Create a connection object that represents the database.
#- Code: conn = sqlite3.connect('database_name.db')
#- Explanation: Replace 'database_name.db' with the name of your SQLite database file. If the file doesn't exist, SQLite will create a new one.

#Step 3: Create a Cursor Object
#- Purpose: A cursor object allows you to execute SQL queries and retrieve results.
#- Code: cur = conn.cursor()

#Step 4: Execute SQL Queries
#- Purpose: Use the cursor object to execute SQL queries, such as creating tables, inserting data, or retrieving data.
#- Code: cur.execute('SQL query')

#Step 5: Commit Changes
#- Purpose: Save changes made to the database.
#- Code: conn.commit()

#Step 6: Close the Connection
#- Purpose: Release system resources and close the connection to the database.
#- Code: conn.close()

#Example Code

import sqlite3

# Establish a connection
conn = sqlite3.connect('example.db')
cur = conn.cursor()

# Create a table
cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
    )
''')

# Insert data
cur.execute("INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com')")

# Commit changes
conn.commit()

# Close the connection
conn.close()


By following these steps, you can connect to a SQLite database using Python and perform various database operations.