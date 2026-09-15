import sqlite3

try:
    conn = sqlite3.connect("../db/magazines.db")
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    # Create tables
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
            name TEXT NOT NULL,
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

    print("Tables created successfully.")

    # Functions for adding data
    def add_publisher(name):
        try:
            cursor.execute(
                "INSERT OR IGNORE INTO publishers (name) VALUES (?)",
                (name,)
            )
        except sqlite3.Error as e:
            print("Error adding publisher:", e)


    def add_magazine(name, publisher_id):
        try:
            cursor.execute(
                "INSERT OR IGNORE INTO magazines (name, publisher_id) VALUES (?, ?)",
                (name, publisher_id)
            )
        except sqlite3.Error as e:
            print("Error adding magazine:", e)


    def add_subscriber(name, address):
        try:
            cursor.execute(
                """
                SELECT subscriber_id
                FROM subscribers
                WHERE name = ? AND address = ?
                """,
                (name, address)
            )

            if cursor.fetchone() is None:
                cursor.execute(
                    "INSERT INTO subscribers (name, address) VALUES (?, ?)",
                    (name, address)
                )

        except sqlite3.Error as e:
            print("Error adding subscriber:", e)


    def add_subscription(subscriber_id, magazine_id, expiration_date):
        try:
            cursor.execute(
                """
                SELECT subscription_id
                FROM subscriptions
                WHERE subscriber_id = ?
                AND magazine_id = ?
                AND expiration_date = ?
                """,
                (subscriber_id, magazine_id, expiration_date)
            )

            if cursor.fetchone() is None:
                cursor.execute(
                    """
                    INSERT INTO subscriptions
                    (subscriber_id, magazine_id, expiration_date)
                    VALUES (?, ?, ?)
                    """,
                    (subscriber_id, magazine_id, expiration_date)
                )

        except sqlite3.Error as e:
            print("Error adding subscription:", e)


    # Populate tables
    add_publisher("Condé Nast")
    add_publisher("Hearst")
    add_publisher("National Geographic")

    add_magazine("Vogue", 1)
    add_magazine("Cosmopolitan", 2)
    add_magazine("National Geographic Magazine", 3)

    add_subscriber("Alice Smith", "123 Main Street")
    add_subscriber("Bob Jones", "456 Oak Avenue")
    add_subscriber("Carol Brown", "789 Pine Road")

    add_subscription(1, 1, "2027-01-01")
    add_subscription(1, 2, "2027-02-01")
    add_subscription(2, 3, "2027-03-01")

    conn.commit()
    print("Data added successfully.")

        # Query 1: Retrieve all subscribers
    print("\nAll Subscribers:")
    cursor.execute("SELECT * FROM subscribers")
    for row in cursor.fetchall():
        print(row)

    # Query 2: Retrieve all magazines sorted by name
    print("\nMagazines Sorted by Name:")
    cursor.execute("SELECT * FROM magazines ORDER BY name")
    for row in cursor.fetchall():
        print(row)

    # Query 3: Find magazines for a particular publisher
    print("\nMagazines Published by Hearst:")
    cursor.execute("""
        SELECT magazines.name
        FROM magazines
        JOIN publishers
        ON magazines.publisher_id = publishers.publisher_id
        WHERE publishers.name = ?
    """, ("Hearst",))

    for row in cursor.fetchall():
        print(row)

except sqlite3.Error as e:
    print("Database error:", e)

finally:
    if "conn" in locals():
        conn.close()
        print("Database connection closed.")