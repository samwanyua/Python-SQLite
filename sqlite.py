import sqlite3

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


# Query
c.execute("SELECT * FROM employees WHERE last = 'Asbury'")

print(c.fetchone())


# to save
conn.commit()
conn.close()
