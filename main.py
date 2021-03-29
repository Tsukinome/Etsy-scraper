from functions import database_functions, scraping_functions


def main():
    keywords = ["techno", "house", "electronix"]
    items = 3100

    scraped_data = scraper.scraper(items, keywords)

    database_func.connect_database()
    database_func.drop_tables()
    database_func.create_tables()
    database_func.insert_categories(keywords)
    database_func.insert_information(scraped_data)
    database_func.export_to_csv()
    print("Data scraped and imported into the database. Data downloaded as all_info.csv")


if __name__ == "__main__":
    main()