#Task 6: Scraping Structured Data

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://owasp.org/Top10/2025/")

#Find A01-A10 links
links = driver.find_elements(By.XPATH, "//a[starts-with(normalize-space(text()), 'A0') or starts-with(normalize-space(text()), 'A10')]")

results = []

for link in links:
    title = link.text.strip()
    href = link.get_attribute("href")

    results.append({
        "title": title,
        "link": href
    })

driver.quit()

print(results)

df = pd.DataFrame(results)

df.to_csv("owasp_top_10.csv", index=False)
