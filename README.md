# Etsy scraper
## Table of contents
* [About](#about)
* [Installation](#instalattion)
* [Actions](#actions)
* [Technologies used](#technologies-used)
* [License](#license)

## About

This is a final project for 2.2. in Turing College. The functions scrape Etsy website, connects to a database created on Heroku, creates two tables and inserts the information into these tables.

With this scraper you can scrape data about product listings such as title, price, rating, item url, and image url with selected keyword.

## Installation

```python
!pip install git+https://github.com/Tsukinome/Scraper_225
```

* The scraping function: 
```python
from functions import scraper
```

* The database functions: 
```python
from connect import database_func
```

## Actions

* `connect_database()` - connects to Heroku. 
* `drop_tables()` - drops categories and items tables.
* `create_tables()` - creates categories and items tables.
* `inset_categories()` - inserts keywords into categories table in the database.
* `insert_information()` - inserts scraped data to items table in the database.
* `export_to_csv()` - exports data from database as .csv file.


## Technologies used
* Python - version 3.9 
* BeautifulSoup4

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

