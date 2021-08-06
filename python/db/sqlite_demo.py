import sqlite3
from employee import Employee

# conn = sqlite3.connect(":memory:")
conn = sqlite3.connect("employee.db")
cursor = conn.cursor()


def insert_emp(emp: Employee):
    with conn:
        cursor.execute(
            "INSERT INTO employees VALUES (?, ?, ?)", (emp.first, emp.last, emp.pay)
        )


def get_emps_by_lastname(lastname: str):
    with conn:
        cursor.execute("SELECT * FROM employees WHERE last=:last", {"last": lastname})
        return cursor.fetchall()


def update_pay(emp: Employee, pay: int):
    with conn:
        cursor.execute(
            "UPDATE employees SET pay = :pay WHERE first = :first AND last = :last",
            {"first": emp.first, "last": emp.last, "pay": pay},
        )


def remove_emp(emp: Employee):
    with conn:
        cursor.execute(
            "DELETE FROM employees WHERE first = :first AND last = :last",
            {"first": emp.first, "last": emp.last},
        )


cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS employees (
        first TEXT,
        last TEXT,
        pay INTEGER
    )"""
)


# cursor.execute("INSERT INTO employees VALUES ('John', 'Smith', 50000)")
# cursor.execute("INSERT INTO employees VALUES ('Jane', 'Smith', 40000)")

# cursor.execute("SELECT * FROM employees WHERE last='Smith'")
# print(cursor.fetchall())


emp_1 = Employee("Sam", "Rock", 80000)
emp_2 = Employee("Alice", "Rock", 60000)

# cursor.execute(
#     "INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay)
# )
# cursor.execute(
#     "INSERT INTO employees VALUES (:first, :last, :pay)",
#     {"first": emp_1.first, "last": emp_1.last, "pay": emp_1.pay},
# )

# cursor.execute("SELECT * FROM employees WHERE last=?", ("Rock",))
# print(cursor.fetchall())

cursor.execute(
    "SELECT * FROM employees WHERE last=:last",
    {"last": "Smith"},
)
print(cursor.fetchall())

conn.commit()

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_lastname("Rock")
print(emps)

update_pay(emp_1, 100000)
remove_emp(emp_2)

emps = get_emps_by_lastname("Rock")
print(emps)

conn.close()
