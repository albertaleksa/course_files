import requests
from bs4 import BeautifulSoup
import mysql.connector
import dbs.cfg as cfg

sql_create_books = """CREATE TABLE `books` (
        `id` INT(11) NOT NULL AUTO_INCREMENT,
        `title` VARCHAR(255) NOT NULL,
        `price` DECIMAL(5, 2) NOT NULL,
        `rating` INT(1) NOT NULL,
        `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB
    
    """


def scrape_books(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    all_books = []
    for book in books:
        book_data = (get_title(book), get_price(book), get_rating(book))
        all_books.append(book_data)

    print(all_books)
    save_books(all_books)


def save_books(all_books):
    my_cfg = cfg.CONFIG.copy()
    my_cfg["database"] = "python"

    connection = mysql.connector.connect(**my_cfg)
    cursor = connection.cursor()
    # cursor.execute(sql_create_books)
    cursor.executemany("INSERT INTO books (title, price, rating) VALUES (%s, %s, %s)", all_books)
    connection.commit()
    rowcount = cursor.rowcount
    cursor.close()
    connection.close()
    print(rowcount)


def get_title(book):
    return book.find("h3").find("a")["title"]


def get_price(book):
    price = book.find(class_="price_color").get_text()
    return float(price.replace("£", "").replace("Â", ""))


def get_rating(book):
    ratings = {
        "Zero": 0,
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    paragraph = book.select(".star-rating")[0]
    rating = paragraph.get_attribute_list("class")[-1]
    return ratings[rating]


if __name__ == "__main__":
    scrape_books("https://books.toscrape.com")
