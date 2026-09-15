# Task 3: Extract book data from Durham County Library

import pandas as pd
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Load the Durham County Library search page
url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get(url)

# Find all book search result entries
book_entries = driver.find_elements(
    By.CSS_SELECTOR,
    "li.row.cp-search-result-item"
)

print("Number of books found:", len(book_entries))

# Create an empty list for the book results
results = []

# Extract information from each book
for entry in book_entries:
    # Get title
    title = entry.find_element(
        By.CLASS_NAME, "title-content"
    ).text

    # Get author(s)
    authors = entry.find_elements(
        By.CLASS_NAME, "author-link"
    )
    author_text = ";".join(
        author.text for author in authors
    )

    # Get format and year
    format_div = entry.find_element(
        By.CLASS_NAME, "cp-format-info"
    )

    format_year = format_div.find_element(
        By.CLASS_NAME, "display-info-primary"
    ).text

    # Store the book information
    book = {
        "Title": title,
        "Author": author_text,
        "Format-Year": format_year
    }

    results.append(book)


# Create and print DataFrame
df = pd.DataFrame(results)

print(df)

# Task 4: Write out the data

# Save DataFrame as CSV
df.to_csv("get_books.csv", index=False)

# Save results as JSON
with open("get_books.json", "w") as json_file:
    json.dump(results, json_file, indent=4)