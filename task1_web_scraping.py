import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    books_list = []
    books = soup.find_all('article', class_='product_pod')
    
    for book in books:
        title = book.h3.a['title']
        price_raw = book.find('p', class_='price_color').text
        price = float(price_raw.replace('£', '').replace('Â', ''))
        availability = book.find('p', class_='instock availability').text.strip()
        
        books_list.append({
            'Book_Title': title,
            'Price_In_Pounds': price,
            'Status': availability
        })
    
    df = pd.DataFrame(books_list)
    df.to_csv('extracted_books_data.csv', index=False)
    print("✓ TASK 1 Completed!")
