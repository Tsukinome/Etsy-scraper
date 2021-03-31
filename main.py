from functions import database_functions, scraping_functions


def main():
    keywords = ["masks", "rings", "anime"]
    items = 3100

    scraped_data = scraping_functions.scraper(items, keywords)

    database_functions.connect_database()
    database_functions.drop_tables()
    database_functions.create_tables()
    database_functions.insert_categories(keywords)
    database_functions.insert_information(scraped_data)
    database_functions.export_to_csv()
    print("Data scraped, imported and downloaded as all.csv")


if __name__ == "__main__":
    main()