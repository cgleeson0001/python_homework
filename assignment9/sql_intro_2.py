import sqlite3
import pandas as pd

try:
    conn = sqlite3.connect("../db/lesson.db")

    query = """
        SELECT
            line_items.line_item_id,
            line_items.quantity,
            products.product_id,
            products.product_name,
            products.price
        FROM line_items
        JOIN products
        ON line_items.product_id = products.product_id
    """

    # Read SQL data into a DataFrame
    df = pd.read_sql_query(query, conn)

    print("\nOriginal DataFrame:")
    print(df.head())

    # Add total column
    df["total"] = df["quantity"] * df["price"]

    print("\nDataFrame with Total:")
    print(df.head())

    # Group by product
    summary_df = df.groupby("product_id").agg({
        "line_item_id": "count",
        "total": "sum",
        "product_name": "first"
    }).reset_index()

    print("\nGrouped DataFrame:")
    print(summary_df.head())

    # Sort by product name
    summary_df = summary_df.sort_values("product_name")

    # Save to CSV
    summary_df.to_csv("order_summary.csv", index=False)

    print("\norder_summary.csv created successfully.")

except (sqlite3.Error, pd.errors.DatabaseError) as e:
    print("Database error:", e)

finally:
    if "conn" in locals():
        conn.close()