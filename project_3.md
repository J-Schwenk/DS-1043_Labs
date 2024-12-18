# Webscraping Data using Python
### Jack Schwenkler

#### Introduction
The web scraping assignment involved learning web scraping through
experience by extracting data from a website designed for web scraping - 
books.toscrape.com. The goal was to scrape book details (title, price, etc.)
from the website using Python. The main tools that I used were the requests
function for sending HTTP requests and BeautifulSoup, a group of functions
designed for parsing HTML.

#### Assignment
There were seven details that I had to extract for each book - Title,
Category, UPC, Price, Tax, Availability, and Number of Reviews. This
data was then saved to an extracted data to CSV file which I called
books.csv.

#### Approach
In my initial setup, I installed both requests and BeautifulSoup as I
already described. I then created a constant DOMAIN to build URLs for each
page of books, as the website was formatted from https://books.toscrape.com/catalogue/page-1.html
all the way to page 50. The main loop loops over all 50 pages of the website
to scrape the book data, with each page url constructed using DOMAIN.format(i),
where i is the page number 1-50. 

In order to extract book information from each page, I created two functions:
extract_books_from_page and extract_book_details. The extract_books_from_page
extracted all 20 book titles for each page in order to generate the url for
each book, which were all formatted the same way. The extract_book_details
function looped through the generated book urls and got all the necessary
data from them using the find() method to locate each piece of information.

Each book's details were stored in a dictionary, and a list accumalates
all the dictionaries for each book across all of the pages. Once the data
was all collected, it was written to a CSV file using csv.DictWriter().
I initially set the script to just scrape the first 5 pages for quicker
testing, and only when it was completed did I adjust it to loop through all
50 pages to collect all of the data.

#### Results
The final output, as I already described, is a CSV file (books.csv), with each
row representing the data for an individual book. It contains the following columns:
title, category, upc, price_excl_tax, price_incl_tax, tax, availability, and reviews.

#### Future Work
One possible improvement that could be made is the implementation of some kind of
retry logic that could look for simple syntax differences that might lead to an
error by trial-and-error instead of simply giving up. Another addition could be
scraping additional details, such as book descriptions, or implementing a TD-IDF
algorithm to detect the key concepts of the description.

#### Conclusion
I was successfully able to scrape all of the request book data from the
website for all 50 pages, and I was able to extract all of the requested
information and save it into a CSV file. This project, while it was difficult,
gave me hands-on experience with web scraping and really forced me to learn
how it works, as well as showing me the other minor errors that I tended to
overlook in my codes, because they never had mattered before.