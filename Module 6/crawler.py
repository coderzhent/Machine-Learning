import logging
import requests
import os
from bs4 import BeautifulSoup

logging.basicConfig(filename='./Module 6/web_get_info.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def crawl(url):
    # Send an HTTP request to the provided URL
    try:
        response = requests.get(url)
        if response.status_code == 200:
            logging.info(f"Successfully fetched: {url}")
            
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all links on the page
            links = soup.find_all('a', href=True)

            # Log all the links found on the page
            for link in links:
                logging.info(f"Found link: {link['href']}")
        else:
            logging.error(f"Failed to fetch: {url}, Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed for {url} with error: {e}")

def get_txt(url, path):
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            with open(path, 'wb') as file:
                file.write(resp.content)
            logging.info(f"Successfully fetch: {url} and saved it to: {path}")
        else:
            logging.error(f"Failed to download file from: {url} with HTTP status code: {resp.status_code}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch: {url}, with error: {e}")

dest_dir = "./Module 6/data/"
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

total = 76001
batch_size = 1000
batch_inc = 0

for i in range(1, total):
    base_url = 'https://www.gutenberg.org/cache/epub/'
    dest_url = base_url + str(i) + '/pg' + str(i) + '.txt'
    batch_dir = dest_dir + '000' + str(batch_inc) + '/'
    dest_file = batch_dir + 'pg' + str(i) + '.txt'
    if os.path.exists(dest_file):
        logging.error(f"File {dest_file} already exists for link: {dest_url}")
    else:
        get_txt(dest_url, dest_file)

    if i % 100 == 0:
        print(f"Processed {i} elements ||  %{(i / total) * 100}")
        
    if (i > 1) and ((i - 1) % batch_size == 0):
        batch_inc += 1
    # print(f"URL: {dest_url}")

# if __name__ == "__main__":
#     start_url = 'https://example.com'  # Replace with the URL you want to crawl
#     crawl(start_url)
