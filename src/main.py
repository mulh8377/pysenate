
import requests
import urllib3

from bs4 import BeautifulSoup
import logging

sites = [
    'https://flsenate.gov/Session/Bills/2023'
]


requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'

try:
    requests.packages.urllib3.contrib.pyopenssl.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
except AttributeError:
    # no pyopenssl support used / needed / available
    pass

def grab_text(url):
    r = requests.get(url)
    logging.info(f'Grabbing {r.text} from {url}')
    return r.text

def get_soup(text):
    return BeautifulSoup(text, 'html.parser')

def find_column(soup) -> bool:
    title_columns = soup.findAll('td')
    # find each element in increments of 3
    for i in title_columns:
        print(f'{i.text}')

        # transform text into lowercase
        if 'cybersecurity' in i.text.lower():
            return True
    


def find_keyword(text, keyword='cybersecurity'):
    if keyword in text:
        logging.info(f'Found {keyword} in {text}')
        return True
    else:
        logging.info(f'Could not find {keyword} in {text}')
        return False

def main():
    for site in sites:
        text = grab_text(site)
        s = get_soup(text)
        find_column(s)
        """if find_keyword(text):
            print(f'Found {keyword} in {site}')
        """

if __name__ == "__main__":
    main()