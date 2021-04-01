import math
from bs4 import BeautifulSoup
import time
import requests
import pandas as pd
from fake_useragent import UserAgent
from connect import database_functions


def scraper(items: int, keywords: list) -> pd.DataFrame:
    """
    Scrapes etsy.com website and returns keyword_id, title, rating,
    price, reviews count, item_url, urls_of_images
    :param items: number of items to crape of each category. Min - 64.
    :param keywords: list of categories to scrape
    :return: DataFrame
    """

    ua = UserAgent()
    keyword_id, title, rating, prices, reviews_count, item_url, urls_of_image = ([] for i in range(6))
    pages = math.ceil(items / 64)

    for keyword in keywords:

        for page in range(1, pages + 1):

            url = f'https://www.etsy.com/search?q={keyword}&page={page}'
            page = requests.get(url, headers={'User-Agent': ua.chrome})
            soup = BeautifulSoup(page.content, "html.parser")
            time.sleep(1)

            for _ in soup.select("div.description > h2"):
                keyword_id.append(keywords.index(keyword) + 1)
            for title in soup.select("div.description > h3"):
                title.append(title.text.replace("'", "''"))
            for rating in soup.select("div.description > span"):
                rating.append(rating.text.replace("'", "''"))
            for price in soup.find_all("p", class_="wt-text-title-01"):
                prices.append(price.text.replace(" USD", ""))
            for url_of_image in soup.select("img.img-responsive"):
                urls_of_image.append(url_of_image["src"])
            for item_url in soup.select("div.description > h3 > a"):
                item_url.append("https://etsy.com/" + item_url["href"])

    collected_data = list(zip(keyword_id, title, rating, prices, reviews_count, item_url, urls_of_image))

    return pd.DataFrame(collected_data, columns= ['keyword_id', 'title', 'rating', 'price',
                                                 'reviews_count', 'item_url', 'url_of_image'])