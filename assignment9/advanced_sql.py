import sqlite3

conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM employees")
result = cursor.fetchall()
print(result)

conn.close()


#Task 1: Complex JOINs with Aggregation

#Connect to the database
conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

cursor.execute("""SELECT o.order_id, SUM(p.price * l.quantity) AS total_price
               FROM orders o
               JOIN line_items l ON o.order_id = l.order_id
               JOIN products p ON l.product_id = p.product_id
               GROUP BY o.order_id
               ORDER BY o.order_id
               LIMIT 5
               """)
result1 = cursor.fetchall()
print(result1)

conn.close()


#Task 2: Understanding Subqueries

#Connect to the database
conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

#Calculate the average order price for each customer
cursor.execute("""SELECT c.customer_name, AVG(order_totals.total_price) AS average_total_price
               FROM customers c
               LEFT JOIN (
               SELECT o.customer_id AS customer_id_b,
               SUM(p.price * l.quantity) AS total_price
               FROM orders o
               JOIN line_items l ON o.order_id = l.order_id
               JOIN products p ON l.product_id = p.product_id
               GROUP BY o.order_id
               ) AS order_totals
               ON c.customer_id = order_totals.customer_id_b
               GROUP BY c.customer_id
                """)
result2 = cursor.fetchall()
print(result2)


#Task 3: An Insert Transaction Based on Data

#Connect to the database 
conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

#Enable foreign key constraints
conn.execute("PRAGMA foreign_keys = 1")

#Get customer_id for 'Perez and Sons'
cursor.execute("""SELECT customer_id 
               FROM customers 
               WHERE customer_name = 'Perez and Sons'
               """)
customer_id = cursor.fetchall()[0][0]              

#Get employee_id for Miranda Harris
cursor.execute("""SELECT employee_id 
               FROM employees 
               WHERE first_name = 'Miranda' AND last_name = 'Harris'
               """)    
employee_id = cursor.fetchall()[0][0]        

#Get product_ids of the 5 least expensive products            
cursor.execute("""SELECT product_id 
               FROM products 
               ORDER BY price ASC 
               LIMIT 5
               """) 
product_ids = [row[0] for row in cursor.fetchall()]

#Create a new order and return the generated order_id
cursor.execute("""INSERT INTO orders (customer_id, employee_id, date)
               VALUES (?, ?, DATE('now'))
               RETURNING order_id
               """, (customer_id, employee_id))
order_id = cursor.fetchone()[0]

#Insert line items for the order
for id in product_ids:
    cursor.execute("""INSERT INTO line_items (order_id, product_id, quantity)
                   VALUES (?, ?, ?)
                   """, (order_id, id, 10))
    
conn.commit()

#Retrieve and display the created line items
cursor.execute("""SELECT li.line_item_id, li.quantity, p.product_name
               FROM line_items li
               JOIN products p ON li.product_id = p.product_id
               WHERE li.order_id = ?
               """, (order_id,))
print(cursor.fetchall())


#Task 4: Aggregation with HAVING

#Connect to the database
conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

#Count orders per employee, filter those with >5 orders
cursor.execute("""SELECT e.employee_id, e.first_name, e.last_name, COUNT(o.order_id) AS order_count
               FROM employees e
               JOIN orders o ON e.employee_id = o.employee_id
               GROUP BY e.employee_id
               HAVING COUNT(o.order_id) > 5
               """)

print(cursor.fetchall())
conn.close()
