import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
}


def get_data(url):
    r = requests.get(url=url, headers=headers)

    with open("index.html", "w", encoding="utf-8") as file:
        file.write(r.text)


def get_text():
    with open("index.html", encoding="utf8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    body = soup.find("div", class_="gu gv gw gx gy")
    res = body.get_text()

    with open("res.doc", "w", encoding="utf8") as file:
        file.write(res)


def main():
    get_data(url='https://medium.com/@talecky/%D0%B7%D0%B0%D1%87%D0%B5%D0%BC-%D0%BD%D1%83%D0%B6%D0%BD%D1%8B-%D0%B1%D0%B0%D0%B7%D1%8B-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85-%D0%B8-%D1%87%D1%82%D0%BE-%D1%8D%D1%82%D0%BE-%D0%B2%D0%BE%D0%BE%D0%B1%D1%89%D0%B5-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-part-1-2b1bde3fdfc')
    get_text()


if __name__ == '__main__':
    main()
