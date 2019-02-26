from time import sleep

import requests
from pyquery import PyQuery as pq

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}
base_url = "https://www.shi-ci.com"

def get_index_page():
    urls = []
    response = requests.get(base_url, headers=headers)
    if response.status_code == 200:
        doc = pq(response.text)
        title= doc("#poem h1").text()
        poet = doc("#poem h3").text()
        poet_details = doc(".uk-width-1-3 p").text()
        poem = doc("#poem div p").text()
        # print(title,poet,poem,poet_details)
        result = {
            "title":title,
            "poet":poet,
            "poem":poem,
            "poet_details":poet_details
        }
        return result
    return None

if __name__ == "__main__":
    str=get_index_page()
    print(str["poem"])