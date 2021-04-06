from functions import scraping_functions
from connect import database_functions

def main():
    keywords = ["masks", "rings", "anime"]
    items = 18000

    scraped_data = scraping_functions.scraper(items, keywords)

    database_functions.connect_database()
    database_functions.drop_tables()
    database_functions.create_tables()
    database_functions.insert_categories(keywords)
    database_functions.insert_information(scraped_data)
    database_functions.export_to_csv()
    print("Data scraped, imported and downloaded as all_items.csv")

if __name__ == "__main__":
    main()
