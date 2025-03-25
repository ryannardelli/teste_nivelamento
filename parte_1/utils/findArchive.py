import requests
from bs4 import BeautifulSoup

def findArchive(url):
    response = requests.get(url)

    # variable to store the code of response html
    html = response.text

    # use soup for analyzed html
    if(response.status_code == 200):
        soup = BeautifulSoup(html, 'html.parser')

        for link in soup.find_all('a', href=True):
            href = link.get('href')

            if 'Anexo I' in link.text or 'Anexo II' in link.text and ('pdf' in href or 'xls' in href):
                return href
    else:
        print("Failed to conect: ", response.status_code)