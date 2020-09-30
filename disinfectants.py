import requests
from bs4 import BeautifulSoup

URL = 'https://www.epa.gov/pesticide-registration/list-n-disinfectants-use-against-sars-cov-2'
page = requests.get(URL)
soup = BeautifulSoup(page.content,'html.parser')
tables = [x for x in soup.find_all('table')]
disenfectants = tables[1]
