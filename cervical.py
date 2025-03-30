import requests
from bs4 import BeautifulSoup

def atlas(URL:str):
    r = requests.get(URL, timeout=25)
    if r.status_code != 200:
        return f"Failed to request: {r.status_code}"
    else:
        return r.text

def spinal(content:str, url:str):
    paths = []
    archives = []
    soup = BeautifulSoup(content, "html.parser")
    table = soup.find("table")
    for td in table.find_all("td"):
        try:
            href = link['href']
            #verify_ext = lambda href: any(href.endswith(ext) or href.endswith(ext.upper()) for ext in exts)
            if href[-1] != "/": # check the type
                archives.append(f'{url}{href}')
            else:
                paths.append(f'{url}{href}')
        except Exception as err:
            None
    return paths, archives

