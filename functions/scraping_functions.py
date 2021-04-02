import math
from bs4 import BeautifulSoup
import time
import requests
import pandas as pd
from fake_useragent import UserAgent

def scraper(items: int, keywords: list) -> pd.DataFrame:
    """
    Scrapes etsy.com website and returns keyword_id, title, rating,
    price, item_url, urls_of_images
    :param items: number of items to scrape of each category. Min - 50.
    :param keywords: list of categories to scrape
    :return: DataFrame
    """

    ua = UserAgent()
    category_id, titles, ratings, prices, items_url, urls_of_image = ([] for i in range(6))
    pages = math.ceil(items / 50)

    for keyword in keywords:

        for page in range(1, pages + 1):

            url = f'https://www.etsy.com/search?q={keyword}&page={page}'
            page = requests.get(url, headers={'User-Agent': ua.chrome})
            soup = BeautifulSoup(page.content, "html.parser")
            time.sleep(1)


            for container in soup.select(".js-merch-stash-check-listing.v2-listing-card"):

                category_id.append(keywords.index(keyword) + 1)

                title = container.find("h3").text.strip().replace("'", "")
                titles.append(title)

                price = container.find("span", class_="currency-value").text
                prices.append(price)

                try:
                    rating = float(container.find("input").get('value'))
                except:
                    rating = 0
                    pass

                ratings.append(rating)

                item_url = container.find("a").get('href')
                items_url.append(item_url)

                url_of_image = container.find("img").get('src')
                if not url_of_image:
                    url_of_image = container.find("img").get('data-src')
                urls_of_image.append(url_of_image)

    collected_data = list(zip(category_id, titles, ratings, prices, items_url, urls_of_image))

    return pd.DataFrame(collected_data, columns= ['category_id', 'title', 'rating', 'price', 'item_url', 'url_of_image'])

