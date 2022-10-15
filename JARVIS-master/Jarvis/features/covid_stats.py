import requests
import json
from bs4 import BeautifulSoup
from plyer import notification



def get_covidStats():
    html_data = make_request('https://www.worldometers.info/coronavirus/')
            # print(html_data)
    soup = BeautifulSoup(html_data, 'html.parser')
    total_global_row = soup.find_all('tr', {'class': 'total_row'})[-1]
    total_cases = total_global_row.find_all('td')[2].get_text()
    new_cases = total_global_row.find_all('td')[3].get_text()
    total_recovered = total_global_row.find_all('td')[6].get_text()
    try:
        return total_cases, new_cases, total_recovered
    except:
        return False

def make_request(url):
  response = requests.get(url)
  return response.text

