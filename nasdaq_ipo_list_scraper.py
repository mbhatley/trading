import pandas as pd
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from helper_lists import chromeDriverPath
from selenium.webdriver.common.by import By

service = Service(chromeDriverPath)
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
options.add_argument("--incognito")
driver = webdriver.Chrome(service=service, options=options)

ipo_priced = pd.read_csv("/Users/michael/Documents/Trading/IPO/ipo_priced.csv")
ipo_upcoming = pd.read_csv("/Users/michael/Documents/Trading/IPO/ipo_upcoming.csv")
ipo_filings = pd.read_csv("/Users/michael/Documents/Trading/IPO/ipo_filings.csv")
ipo_withdrawn = pd.read_csv("/Users/michael/Documents/Trading/IPO/ipo_withdrawn.csv")

# Find all containers with the shadow-root tables
containers = driver.find_elements(By.CSS_SELECTOR, "div.jupiter22-ipo-calendar__priced_table")
# Iterate over each container and extract data
for container in containers:
    # Locate the shadow host (nsdq-table-sort)
    shadow_host = container.find_element(By.CSS_SELECTOR, "nsdq-table-sort")
    # Access the shadow root using JavaScript
    shadow_root = driver.execute_script("return arguments[0].shadowRoot", shadow_host)
    # Find the table inside the shadow root
    table_rows = shadow_root.find_elements(By.CSS_SELECTOR, "div[role='row']")

    data_price = []
    # Extract and print table data
    for row in table_rows:
        cells = row.find_elements(By.CSS_SELECTOR, "div[role='cell']")
        row_data = [cell.text for cell in cells]
        if row_data:  # Exclude empty rows
            data_price.append(row_data)

    df_priced = pd.DataFrame(data_price[1:], columns=data_price[0])  # Skipping the first row as it contains headers
    df_priced = pd.concat([ipo_priced, df_priced], ignore_index=True)
    df_priced['Company Name'] = df_priced['Company Name'].fillna('')
    df_priced = df_priced.drop_duplicates(subset=['Company Name'], keep='last')
    print(df_priced)
    df_priced.to_csv("/Users/michael/Documents/Trading/IPO/ipo_priced.csv", index=False, encoding='utf-8-sig')

# Find all containers with the shadow-root tables
containers = driver.find_elements(By.CSS_SELECTOR, "div.jupiter22-ipo-calendar__upcoming_table")
# Iterate over each container and extract data
for container in containers:
    # Locate the shadow host (nsdq-table-sort)
    shadow_host = container.find_element(By.CSS_SELECTOR, "nsdq-table-sort")
    # Access the shadow root using JavaScript
    shadow_root = driver.execute_script("return arguments[0].shadowRoot", shadow_host)
    # Find the table inside the shadow root
    table_rows = shadow_root.find_elements(By.CSS_SELECTOR, "div[role='row']")

    data_upcoming = []
    # Extract and print table data
    for row in table_rows:
        cells = row.find_elements(By.CSS_SELECTOR, "div[role='cell']")
        row_data = [cell.text for cell in cells]
        if row_data:  # Exclude empty rows
            data_upcoming.append(row_data)

    df_upcoming = pd.DataFrame(data_upcoming[1:], columns=data_upcoming[0])  # Skipping the first row as it contains headers
    df_upcoming = pd.concat([ipo_upcoming, df_upcoming], ignore_index=True)
    df_upcoming['Company Name'] = df_upcoming['Company Name'].fillna('')
    df_upcoming = df_upcoming.drop_duplicates(subset=['Company Name'], keep='last')
    print(df_upcoming)
    df_upcoming.to_csv("/Users/michael/Documents/Trading/IPO/ipo_upcoming.csv", index=False, encoding='utf-8-sig')

    # Find all containers with the shadow-root tables
containers = driver.find_elements(By.CSS_SELECTOR, "div.jupiter22-ipo-calendar__filings")
# Iterate over each container and extract data
for container in containers:
    # Locate the shadow host (nsdq-table-sort)
    shadow_host = container.find_element(By.CSS_SELECTOR, "nsdq-table-sort")
    # Access the shadow root using JavaScript
    shadow_root = driver.execute_script("return arguments[0].shadowRoot", shadow_host)
    # Find the table inside the shadow root
    table_rows = shadow_root.find_elements(By.CSS_SELECTOR, "div[role='row']")

    data_filings = []
    # Extract and print table data
    for row in table_rows:
        cells = row.find_elements(By.CSS_SELECTOR, "div[role='cell']")
        row_data = [cell.text for cell in cells]
        if row_data:  # Exclude empty rows
            data_filings.append(row_data)

    df_filings = pd.DataFrame(data_filings[1:], columns=data_filings[0])  # Skipping the first row as it contains headers
    df_filings = pd.concat([ipo_filings, df_filings], ignore_index=True)
    df_filings['Company Name'] = df_filings['Company Name'].fillna('')
    df_filings = df_filings.drop_duplicates(subset=['Company Name'], keep='last')
    print(df_filings)
    df_filings.to_csv("/Users/michael/Documents/Trading/IPO/ipo_filings.csv", index=False, encoding='utf-8-sig')

    # Find all containers with the shadow-root tables
containers = driver.find_elements(By.CSS_SELECTOR, "div.jupiter22-ipo-calendar__withdrawn_table")
# Iterate over each container and extract data
for container in containers:
    # Locate the shadow host (nsdq-table-sort)
    shadow_host = container.find_element(By.CSS_SELECTOR, "nsdq-table-sort")
    # Access the shadow root using JavaScript
    shadow_root = driver.execute_script("return arguments[0].shadowRoot", shadow_host)
    # Find the table inside the shadow root
    table_rows = shadow_root.find_elements(By.CSS_SELECTOR, "div[role='row']")

    data_withdrawn = []
    # Extract and print table data
    for row in table_rows:
        cells = row.find_elements(By.CSS_SELECTOR, "div[role='cell']")
        row_data = [cell.text for cell in cells]
        if row_data:  # Exclude empty rows
            data_withdrawn.append(row_data)

    df_withdrawn = pd.DataFrame(data_withdrawn[1:], columns=data_withdrawn[0])  # Skipping the first row as it contains headers
    df_withdrawn = pd.concat([ipo_withdrawn, df_withdrawn], ignore_index=True)
    df_withdrawn['Company Name'] = df_withdrawn['Company Name'].fillna('')
    df_withdrawn = df_withdrawn.drop_duplicates(subset=['Company Name'], keep='last')
    print(df_withdrawn)
    df_withdrawn.to_csv("/Users/michael/Documents/Trading/IPO/ipo_withdrawn.csv", index=False, encoding='utf-8-sig')
