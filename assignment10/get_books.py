import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")

#Task 3: Write a Program to Extract this Data


#Find all li elements
li_elements = driver.find_elements(By.CSS_SELECTOR, "li.row.cp-search-result-item")
print(len(li_elements))

results = []

#Loop through each book entry
for li in li_elements:
    #Get book title
    title_elem = li.find_element(By.CSS_SELECTOR, "h3.cp-title")
    title = title_elem.text
    print(title)

    #Get all authors
    author_elems = li.find_elements(By.CSS_SELECTOR, "a.author-link")
    authors = [a.text for a in author_elems]
    authors_text = "; ".join(authors)
    print(authors_text)

    #Get format and year
    format_elem = li.find_element(By.CSS_SELECTOR, "span.display-info-primary")
    format_year = format_elem.text
    print(format_year)
    
    #Store data in a dictionary
    book = {
        "Title": title,
        "Author": authors_text,
        "Format-Year": format_year
    }

    #Add book to results list
    results.append(book)

print(results)

#Task 4: Write out the Data

df = pd.DataFrame(results)
#Save DataFrame to CSV file  
df.to_csv("get_books.csv", index=False)
#Save DataFrame to JSON file
df.to_json("get_books.json", orient="records", force_ascii=False, indent=4)