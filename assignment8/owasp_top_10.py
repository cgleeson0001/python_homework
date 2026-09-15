# Task 6: Scrape the OWASP Top 10

import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


url = "https://owasp.org/Top10/2025/"

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get(url)

# Find the OWASP Top 10 vulnerability links using XPath
vulnerabilities = driver.find_elements(
    By.XPATH,
    '//*[@id="top-102025-list"]/following-sibling::ol[1]/li/a'
)

# Create an empty list
results = []

# Extract the title and hyperlink for each vulnerability
for vulnerability in vulnerabilities:
    title = vulnerability.text
    link = vulnerability.get_attribute("href")

    results.append({
        "Title": title,
        "Link": link
    })

# Print the results
print(results)

# Create a DataFrame
df = pd.DataFrame(results)

# Save to CSV
df.to_csv("owasp_top_10.csv", index=False)

driver.quit()