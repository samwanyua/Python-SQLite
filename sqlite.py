# sqlite.py
import sqlite3
from main import Employee

# create a variable - conn
# conn = sqlite3.connect(':memory:') # in memory database
conn = sqlite3.connect('employee.db') # creating a connection

# create a cursor
c = conn.cursor()

# Employee table
# c.execute("""
#     CREATE TABLE employees(
#           first TEXT,
#           last TEXT,
#           pay INTEGER
#     )""")

# adding records
# c.execute("INSERT INTO employees VALUES ('Cory', 'Asbury', 56000)")
# conn.commit()

emp_1 = Employee('John', 'Doe', 90000)
emp_2 = Employee('Jane', 'Doe', 90000)

# c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))

# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay })
# Query
c.execute("SELECT * FROM employees WHERE last = ?", ('Asbury',))

print(c.fetchall())

c.execute("SELECT * FROM employees WHERE last = :last", {'last': 'Wanyua'})

print(c.fetchall())


# to save
conn.commit()
conn.close()
