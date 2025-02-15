import requests
from bs4 import BeautifulSoup
from settings import *
from utils import save_to_logs, save_to_json, write_to_xlsx
import time
import datetime


url = 'https://scrapingclub.com/exercise/list_basic/'
all_product_list = []


def get_soup(url):
    try:
        req = requests.get(url, headers=HEADERS)
        src = req.text
        soup = BeautifulSoup(src, "lxml")
        return soup
    except Exception as e:
        save_to_logs(f"ERROR during soup getting:\n{e}")
        return False


def get_product_links(url):
    product_links = []
    current_page = 1
    soup = get_soup(f"{url}?page={current_page}")
    pages_qty = int(soup.find_all('span', class_='page')[-2].text.strip())
    while current_page <= pages_qty:
        save_to_logs(f"Processing page №{current_page}")
        h4_titles = soup.find_all('h4')
        for h4 in h4_titles:
            product_link = f"https://scrapingclub.com{h4.find('a').get('href')}"
            product_links.append(product_link)
        current_page += 1
        time.sleep(1)
    save_to_logs(
        f"Products links collecting has been ended. Collected links quantity: {len(product_links)}")
    return product_links


def get_product_data(link):
    save_to_logs(f"Processing link: {link}")
    try:
        soup = get_soup(link)
        product_title = soup.find('h3', class_='card-title').text.strip()
        product_link = link
        product_price = float(
            soup.find('h4', class_='my-4 card-price').text.replace('$', ''))
        product_description = soup.find(
            'p', class_='card-description').text.strip()
        product_img = f"https://scrapingclub.com{soup.find('img', class_='card-img-top').get('src')}"
        product_data = {
            'product_title': product_title,
            'product_link': product_link,
            'product_price': product_price,
            'product_description': product_description,
            'product_img': product_img
        }
        all_product_list.append(product_data)
    except Exception as e:
        save_to_logs(f"ERROR during processing link ({link}):\n{e}")


def main():
    start_time = datetime.datetime.now()
    for link in get_product_links(url):
        get_product_data(link)
    save_to_logs(f"Collected goods qty: {len(all_product_list)}")
    if save_to_json(all_product_list):
        write_to_xlsx('parsed_data.json')
    end_time = datetime.datetime.now()
    execution_time = end_time - start_time
    save_to_logs(
        f"Processing time is: {str(execution_time).split('.')[0]}")


if __name__ == '__main__':
    main()
