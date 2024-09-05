#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import bs4

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from helper_lists import chromeDriverPath

service = Service(chromeDriverPath)
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
options.add_argument("--incognito")
driver = webdriver.Chrome(service=service, options=options)

ipos = pd.read_csv("/Users/michael/Trading/IPO/ipo_list.csv")

soup = bs4.BeautifulSoup(driver.page_source, "html.parser")

# table = soup.find('table', {'class': 'market-calendar-table__table'})

tables = soup.find_all('table', {'class': 'market-calendar-table__table'})

if len(tables) >= 2:
    # Extract data from the second table
    table = tables[2]

    data = []

    for row in table.find_all('tr'):
        # Extracting data from the row cells
        row_data = [cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])]
        if row_data:  # Exclude empty rows
            data.append(row_data)

    df = pd.DataFrame(data[1:], columns=data[0])  # Skipping the first row as it contains headers

    df = pd.concat([ipos, df], ignore_index=True)

    df = df.drop_duplicates()

    print(df)

    df.to_csv("/Users/michael/Trading/IPO/ipos.csv", index=False, encoding='utf-8-sig')