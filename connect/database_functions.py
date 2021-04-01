import pandas as pd
import psycopg2

def connect_database() -> psycopg2.connect:
    """
    Creates connection with Heroku database
    :return: connection
    """
    connection = psycopg2.connect(
        database="d2ullgp5g77deq",
        user="gjombjapnlozqc",
        password="6c51bcf6db99739225d282c0be180f52fe0122e28f01ad6b5e66823a1cc9d625",
        host="ec2-108-128-104-50.eu-west-1.compute.amazonaws.com",
        port="5432")

    return connection

def drop_tables() -> None:
    """
    Drops existing tables
    :return: None
    """
    connect = connect_database()
    cur = connect.cursor()

    cur.execute('''
    DROP TABLE IF EXISTS categories CASCADE;
    DROP TABLE IF EXISTS items CASCADE;''')

    connect.commit()


def create_tables() -> None:
    """
    Creates two tables in the database:
    categories stores item category,
    items stores information about item
    :return: None
    """
    connect = connect_database()
    cur = connect.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        id SERIAL PRIMARY KEY,
        keyword VARCHAR(255));
        ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS items (
        id SERIAL PRIMARY KEY,
        keyword_id INT,
        title VARCHAR (255),
        rating FLOAT,
        price VARCHAR(20),
        reviews_count INT,
        item_url TEXT,
        image_url TEXT,
        FOREIGN KEY (keyword_id) REFERENCES categories(id));
        ''')

    connect.commit()

def insert_categories(keywords) -> None:
    """
    Inserts items categories into categories table
    :return: None
    """
    connect = connect_database()
    cur = connect.cursor()

    for keyword in keywords:
        cur.execute(f"INSERT INTO categories(keyword) VALUES('{keyword}');")

    connect.commit()


def insert_information(scraped_data) -> None:
    """
    Inserts all scraped data into items table
    :param scraped_data: scraped dataframe
    :return: None
    """

    connect = connect_database()
    cur = connect.cursor()

    for row in scraped_data.to_records(index=False):
        keyword_id, title, rating, price, reviews_count, item_url, url_of_image = row
        cur.execute(f"INSERT INTO items(keyword_id, title, rating, price, reviews_count, item_url, url_of_image)\
        VALUES ('{keyword_id}', '{title}', '{rating}', '{price}', '{reviews_count}', '{item_url}', '{url_of_image}');")
    connect.commit()


def export_to_csv() -> None:
    """
    Exports scraped data to .csv file
    :return: .csv file
    """
    connect = connect_database()
    cur = connect.cursor()

    cur.execute('''SELECT items.id, categories.keyword, title, rating, price, reviews_count, item_url, url_of_image
    FROM items
    LEFT JOIN categories ON items.keyword_id = keyword.id
    ORDER BY items.id''')

    all_information = cur.fetchall()

    columns = ['id', 'keyword', 'title', 'rating', 'price', 'reviews_count', 'item_url', 'url_of_image']
    pd.DataFrame(all_information).to_csv("all.csv", index=False, header=columns)

    connect.commit()