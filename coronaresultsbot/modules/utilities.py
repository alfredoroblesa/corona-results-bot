from coronaresultsbot.settings import config
import requests
from bs4 import BeautifulSoup


def get_html_soup(url):
    try:
        html_doc = requests.get(url).content
        # Create HTML soup
        soup = BeautifulSoup(html_doc, 'html.parser')
        return soup
    except:
        print("ERROR Can not access URL " + url)
    

def clean_string(string):
    return string.strip().replace(',','.')
