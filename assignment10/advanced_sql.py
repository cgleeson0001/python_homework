import sqlite3

# Connect to the database
conn = sqlite3.connect("../db/lesson.db")
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()


# Task 1: Complex JOINs with Aggregation

query = """
SELECT
    orders.order_id,
    SUM(products.price * line_items.quantity) AS total_price
FROM orders
JOIN line_items
    ON orders.order_id = line_items.order_id
JOIN products
    ON line_items.product_id = products.product_id
GROUP BY orders.order_id
ORDER BY orders.order_id
LIMIT 5;
"""

cursor.execute(query)
results = cursor.fetchall()

print("First 5 Order Totals:")

for order_id, total_price in results:
    print(f"Order ID: {order_id}, Total Price: ${total_price:.2f}")


# Task 2: Understanding Subqueries

query = """
SELECT
    customers.customer_name,
    AVG(order_totals.total_price) AS average_total_price
FROM customers
LEFT JOIN (
    SELECT
        orders.customer_id AS customer_id_b,
        SUM(products.price * line_items.quantity) AS total_price
    FROM orders
    JOIN line_items
        ON orders.order_id = line_items.order_id
    JOIN products
        ON line_items.product_id = products.product_id
    GROUP BY orders.order_id
) AS order_totals
    ON customers.customer_id = order_totals.customer_id_b
GROUP BY customers.customer_id;
"""

cursor.execute(query)
results = cursor.fetchall()

print("\nAverage Order Price by Customer:")

for customer_name, average_total_price in results:
    if average_total_price is not None:
        print(f"{customer_name}: ${average_total_price:.2f}")
    else:
        print(f"{customer_name}: No orders")


# Task 3: An Insert Transaction Based on Data

# Get the customer_id for Perez and Sons
cursor.execute(
    """
    SELECT customer_id
    FROM customers
    WHERE customer_name = ?
    """,
    ("Perez and Sons",)
)
customer_id = cursor.fetchone()[0]

# Get the employee_id for Miranda Harris
cursor.execute(
    """
    SELECT employee_id
    FROM employees
    WHERE first_name = ? AND last_name = ?
    """,
    ("Miranda", "Harris")
)
employee_id = cursor.fetchone()[0]

# Get the product_ids of the 5 least expensive products
cursor.execute(
    """
    SELECT product_id
    FROM products
    ORDER BY price
    LIMIT 5
    """
)
product_ids = [row[0] for row in cursor.fetchall()]

# Create the order and its line items in one transaction
try:
    cursor.execute(
        """
        INSERT INTO orders (customer_id, employee_id)
        VALUES (?, ?)
        RETURNING order_id
        """,
        (customer_id, employee_id)
    )

    order_id = cursor.fetchone()[0]

    for product_id in product_ids:
        cursor.execute(
            """
            INSERT INTO line_items (order_id, product_id, quantity)
            VALUES (?, ?, ?)
            """,
            (order_id, product_id, 10)
        )

    conn.commit()

except sqlite3.Error:
    conn.rollback()
    raise

# Display the line items for the new order
cursor.execute(
    """
    SELECT
        line_items.line_item_id,
        line_items.quantity,
        products.product_name
    FROM line_items
    JOIN products
        ON line_items.product_id = products.product_id
    WHERE line_items.order_id = ?
    """,
    (order_id,)
)

print("\nNew Order for Perez and Sons:")

for line_item_id, quantity, product_name in cursor.fetchall():
    print(
        f"Line Item ID: {line_item_id}, "
        f"Quantity: {quantity}, "
        f"Product: {product_name}"
    )


# Task 4: Aggregation with HAVING

cursor.execute(
    """
    SELECT
        employees.employee_id,
        employees.first_name,
        employees.last_name,
        COUNT(orders.order_id) AS order_count
    FROM employees
    JOIN orders
        ON employees.employee_id = orders.employee_id
    GROUP BY
        employees.employee_id,
        employees.first_name,
        employees.last_name
    HAVING COUNT(orders.order_id) > 5
    """
)

print("\nEmployees With More Than 5 Orders:")

for employee_id, first_name, last_name, order_count in cursor.fetchall():
    print(
        f"Employee ID: {employee_id}, "
        f"Name: {first_name} {last_name}, "
        f"Order Count: {order_count}"
    )


# Close the database connection
conn.close()