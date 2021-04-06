import requests
from bs4 import BeautifulSoup

url = 'https://ecampus.kangnam.ac.kr'

response = requests.get(url)
if response:
    print("response is OK")
    print("response status code : ", response.status_code)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)
else:
    print("X")

