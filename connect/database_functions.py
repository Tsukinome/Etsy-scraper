import pandas as pd
import psycopg2

def connect_database() -> psycopg2.connect:
    """
    Creates connection with Heroku database
    :return: connection
    """
    connection = psycopg2.connect(
        database="damd6174knjssi",
        user="gbeqdxpsyxujjo",
        password="ddcbdd824a39f17b153860d89bdc75a62de66ab18cc3ed0e283a8dbe8f815460",
        host="ec2-54-220-35-19.eu-west-1.compute.amazonaws.com",
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
    connect.close()


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
        category_id INT,
        title VARCHAR (255),
        rating FLOAT,
        price VARCHAR(200),
        item_url TEXT,
        url_of_image TEXT,
        FOREIGN KEY (category_id) REFERENCES categories(id));
        ''')

    connect.commit()
    connect.close()

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
    connect.close()


def insert_information(scraped_data) -> None:
    """
    Inserts all scraped data into items table
    :param scraped_data: scraped dataframe
    :return: None
    """

    connect = connect_database()
    cur = connect.cursor()

    for row in scraped_data.to_records(index=False):
        category_id, title, rating, price, item_url, url_of_image = row
        cur.execute(f"INSERT INTO items(category_id, title, rating, price, item_url, url_of_image)\
        VALUES ('{category_id}', '{title}', '{rating}', '{price}', '{item_url}', '{url_of_image}');")

    connect.commit()
    connect.close()


def export_to_csv() -> None:
    """
    Exports scraped data to .csv file
    :return: .csv file
    """
    connect = connect_database()
    cur = connect.cursor()

    cur.execute('''SELECT items.id, categories.keyword, title, rating, price, item_url, url_of_image
    FROM items
    LEFT JOIN categories ON items.category_id = categories.id
    ORDER BY items.id''')

    all = cur.fetchall()

    pd.DataFrame(all).to_csv("all_items.csv", index=False)

    connect.commit()
    connect.close()
