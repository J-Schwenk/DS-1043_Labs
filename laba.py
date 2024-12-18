import time
import random
import requests
import csv
from bs4 import BeautifulSoup as Soup
from urllib.parse import urljoin

# Constants
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}
DOMAIN = 'http://books.toscrape.com/catalogue/page-{}.html'
BASE_URL = 'http://books.toscrape.com/catalogue/'
OUTPUT_FILENAME = 'books.csv'
DEFAULT_SLEEP = 3.0
SIGMA = 1.0

def get(url: str) -> requests.Response:
    """Waits a random amount of time, then sends a GET request."""
    time.sleep(random.gauss(DEFAULT_SLEEP, SIGMA))
    response = requests.get(url, headers=HEADERS)
    response.encoding = 'utf-8'  # Ensure proper encoding
    return response

def extract_books_from_page(soup: Soup) -> list[dict]:
    """Extract book links from the current page."""
    books = []
    for product in soup.find_all('article', class_='product_pod'):
        book_data = {}

        # Title and Link
        title_tag = product.find('h3').find('a')
        if title_tag:
            book_data['title'] = title_tag['title']
            book_data['link'] = urljoin(BASE_URL, title_tag['href'])

        books.append(book_data)
    return books

def extract_book_details(book_url: str) -> dict:
    """Extract detailed information about a single book."""
    response = get(book_url)
    if response.status_code != 200:
        print(f"Failed to retrieve book details from {book_url}")
        return {}

    soup = Soup(response.text, 'html.parser')
    book_details = {}

    # Title
    title_tag = soup.find('h1')
    book_details['title'] = title_tag.text.strip() if title_tag else 'N/A'

    # Category
    category_tag = soup.find('ul', class_='breadcrumb').find_all('li')[-2]
    book_details['category'] = category_tag.text.strip() if category_tag else 'N/A'

    # Product Information (UPC, Price, Tax, Availability, Reviews)
    product_table = soup.find('table', class_='table')
    if product_table:
        rows = product_table.find_all('tr')
        for row in rows:
            header = row.find('th').text.strip()
            value = row.find('td').text.strip()
            if header == 'UPC':
                book_details['upc'] = value
            elif header == 'Price (excl. tax)':
                book_details['price_excl_tax'] = value
            elif header == 'Price (incl. tax)':
                book_details['price_incl_tax'] = value
            elif header == 'Tax':
                book_details['tax'] = value
            elif header == 'Availability':
                book_details['availability'] = value
            elif header == 'Number of reviews':
                book_details['reviews'] = value

    return book_details

def write_to_csv(filename: str, books: list[dict], headers: list[str]) -> None:
    """Write book data to the CSV file."""
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for book in books:
            writer.writerow(book)

if __name__ == '__main__':
    # CSV Headers, including all the required fields
    headers = ['title', 'category', 'upc', 'price_excl_tax', 'price_incl_tax', 'tax', 'availability', 'reviews']

    # Generate page URLs for the first 50 pages
    page_urls = [DOMAIN.format(i) for i in range(1, 51)]  # Pages 1 to 50

    # Store all book data
    all_books = []

    for page_url in page_urls:
        print(f"Scraping {page_url}...")
        response = get(page_url)

        if response.status_code != 200:
            print(f"Failed to retrieve {page_url}")
            continue

        # Parse the page content
        soup = Soup(response.text, 'html.parser')

        # Extract book links from the page
        books = extract_books_from_page(soup)

        # Visit each book's detail page to get full information
        for book in books:
            if 'link' in book:
                print(f"Scraping details for {book['title']}...")
                details = extract_book_details(book['link'])
                all_books.append(details)

    # Write all books to the CSV file
    write_to_csv(OUTPUT_FILENAME, all_books, headers)
    print(f"Scraping complete. Data saved to {OUTPUT_FILENAME}.")
