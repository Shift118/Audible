# Import necessary modules from selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

# URL to be opened
web = 'https://www.audible.com/search'

# Path to the ChromeDriver executable
# Just download the driver then copy it to the project dir
# https://storage.googleapis.com/chrome-for-testing-public/132.0.6834.83/win64/chromedriver-win64.zip
path = 'chromedriver.exe'

# Create a Service object with the path to the ChromeDriver executable
service = Service(executable_path=path)

# Initialize the Chrome WebDriver with the specified service
driver = webdriver.Chrome(service=service)

# Open the web driver and open the web browser
driver.get(web)

# //li[contains(@class, "productListItem")] #Products list
# //h3[contains(@class, "bc-heading")] #Title
# //li[contains(@class, "authorLabel")] #Author
# //li[contains(@class, "runtimeLabel")] #Length of the audible
products = driver.find_elements(by = 'xpath', value = '//li[contains(@class, "productListItem")]')
book_title = []
book_author = []
book_length = []

#adding a dot in the begining of value as we are referencing another elements
for product in products:
    book_title.append(product.find_element(by = 'xpath', value = './/h3[contains(@class, "bc-heading")]').text)
    book_author.append(product.find_element(by = 'xpath', value ='.//li[contains(@class, "authorLabel")]').text)
    book_length.append(product.find_element(by = 'xpath', value ='.//li[contains(@class, "runtimeLabel")]').text)

driver.quit()

df_books = pd.DataFrame({'Title': book_title,'Author':book_author,'Length':book_length})
df_books.to_csv('books.csv',index = False)
print("Data Saved Successfully!")
