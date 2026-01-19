#Task 1: Create a New SQLite Database

import sqlite3
try:
    conn = sqlite3.connect("../db/magazines.db")
    print("Database created and connected successfully")
    conn.close()
except sqlite3.Error as e:
    print(r"Database error: {e}")


#Task 2: Define Database Structure

with sqlite3.connect("../db/magazines.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS publishers (
        publisher_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS magazines (
        magazine_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        publisher_id INTEGER NOT NULL,
        FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscribers (
        subscriber_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        address TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscriptions (
        subscription_id INTEGER PRIMARY KEY,
        subscriber_id INTEGER NOT NULL,
        magazine_id INTEGER NOT NULL,
        expiration_date TEXT NOT NULL,
        FOREIGN KEY (subscriber_id) REFERENCES subscribers(subscriber_id),
        FOREIGN KEY (magazine_id) REFERENCES magazines(magazine_id)
    )
    """)

    print("All tables created successfully.")


#Task 3: Populate Tables with Data

def add_publisher(cursor, name):
    try:
        cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
    except sqlite3.IntegrityError:
        print(f"Publisher '{name}' is already in the database.")


def add_magazine(cursor, name, publisher_id):
    try:
        cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?,?)", (name,publisher_id))
    except sqlite3.IntegrityError:
        print(f"Magazine '{name}' is already in the database.")


def add_subcriber(cursor, name, address):
    cursor.execute ("SELECT * FROM subscribers WHERE name=? AND address=?", (name, address))
    results = cursor.fetchall()
    if len(results) > 0:
        print(f"Subcriber '{name}' at '{address}' alredy exists.")
        return
    cursor.execute("INSERT INTO subscribers (name, address) VALUES (?,?)", (name,address))

def add_subscription(cursor, subscriber_id, magazine_id, expiration_date):
    cursor.execute("SELECT * FROM subscriptions WHERE subscriber_id=? AND magazine_id=?", (subscriber_id, magazine_id))
    results = cursor.fetchall()
    if len(results) > 0:
        print(f"Subscription already exists for subcsriber {subscriber_id} and magazine {magazine_id}.")
        return
    cursor.execute("INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?,?,?)", (subscriber_id, magazine_id, expiration_date))
    


add_publisher(cursor, "TechWorld Publishing")
add_publisher(cursor, "Health & Fitness Media")
add_publisher(cursor, "Fashion Forward")

cursor.execute("SELECT publisher_id FROM publishers WHERE name=?", ("TechWorld Publishing",))
tech_id = cursor.fetchall()[0][0]
cursor.execute("SELECT publisher_id FROM publishers WHERE name=?", ("Health & Fitness Media",))
health_id = cursor.fetchall()[0][0]
cursor.execute("SELECT publisher_id FROM publishers WHERE name=?", ("Fashion Forward",))
fashion_id = cursor.fetchall()[0][0]

add_magazine(cursor, "Tech Today", tech_id)
add_magazine(cursor, "Healthy Living", health_id)
add_magazine(cursor, "Style Weekly", fashion_id)
add_magazine(cursor, "Gadget Guide", tech_id)

add_subcriber(cursor, "Alice Johnson", "123 Main St, New York, NY")
add_subcriber(cursor, "Bob Smith", "456 Oak Ave, Chicago, IL")
add_subcriber(cursor, "Charlie Brown", "789 Pine Rd, San Francisco, CA")
add_subcriber(cursor, "Alice Jameson", "321 Elm St, Boston, MA")

cursor.execute("SELECT subscriber_id FROM subscribers WHERE name=? AND address=?", ("Alice Johnson", "123 Main St, New York, NY"))
alice_ny_id = cursor.fetchall()[0][0]
cursor.execute("SELECT subscriber_id FROM subscribers WHERE name=? AND address=?", ("Bob Smith", "456 Oak Ave, Chicago, IL"))
bob_id = cursor.fetchall()[0][0]
cursor.execute("SELECT subscriber_id FROM subscribers WHERE name=? AND address=?", ("Charlie Brown", "789 Pine Rd, San Francisco, CA"))
charlie_id = cursor.fetchall()[0][0]
cursor.execute("SELECT subscriber_id FROM subscribers WHERE name=? AND address=?", ("Alice Jameson", "321 Elm St, Boston, MA"))
alice_boston_id = cursor.fetchall()[0][0]

cursor.execute("SELECT magazine_id FROM magazines WHERE name=?", ("Tech Today",))
tech_today_id = cursor.fetchall()[0][0]
cursor.execute("SELECT magazine_id FROM magazines WHERE name=?", ("Healthy Living",))
healthy_living_id = cursor.fetchall()[0][0]
cursor.execute("SELECT magazine_id FROM magazines WHERE name=?", ("Style Weekly",))
style_weekly_id = cursor.fetchall()[0][0]
cursor.execute("SELECT magazine_id FROM magazines WHERE name=?", ("Gadget Guide",))
gadget_guide_id = cursor.fetchall()[0][0]

add_subscription(cursor, alice_ny_id, tech_today_id, "2026-12-31")
add_subscription(cursor, bob_id, healthy_living_id, "2025-06-30")
add_subscription(cursor, charlie_id, style_weekly_id, "2025-11-15")
add_subscription(cursor, alice_boston_id, gadget_guide_id, "2026-01-31")
add_subscription(cursor, bob_id, tech_today_id, "2026-03-15")

conn.commit()
print("Sample data inserted successfully")


#Task 4: Write SQL Queries

#All subscribers
cursor.execute("SELECT * FROM subscribers")
all_subscribers = cursor.fetchall()
print(all_subscribers)

#All magazines sorted by name
cursor.execute("SELECT * FROM magazines ORDER BY name")
magazines = cursor.fetchall()
print(magazines)

#Magazines for a particular publisher
cursor.execute("SELECT magazines.name FROM magazines JOIN publishers ON magazines.magazine_id = publishers.publisher_id WHERE publishers.name=?", ("Fashion Forward",))
publisher_magazines = cursor.fetchall()
print(publisher_magazines)

