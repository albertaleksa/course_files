from bs4 import BeautifulSoup
import urllib.request
import ssl

# Documentation
# https://www.crummy.com/software/BeautifulSoup/bs4/doc.ru/bs4ru.html#


class WebParser:

    def __init__(self, url, path):
        self.__url = url
        self.__path = path
        self.__raw_html = ''
        self.__html = ''
        self.__results = []

    def get_html(self):
        context = ssl._create_unverified_context()
        req = urllib.request.urlopen(self.__url, context=context)
        self.__raw_html = req.read()

    def raw_to_beauty_html(self):
        self.__html = BeautifulSoup(self.__raw_html, "html.parser")

    def parse_html(self):
        news = self.__html.find_all('li', class_='liga-news-item')

        for item in news:
            title = item.find('span', class_='d-block').get_text(strip=True)
            desc = item.find('span', class_='name-dop').get_text(strip=True)
            href = item.find('a', class_='liga-news-item-link').get('href')
            self.__results.append({
                'title': title,
                'desc': desc,
                'href': href
            })

    def write_to_file(self):
        with open(self.__path, 'w', encoding='utf-8') as f:
            i = 1
            for item in self.__results:
                f.write(f"News N {i}\n\n Name: {item['title']}\n Description: {item['desc']}\n Link: {item['href']}\n\n"
                        f"*************************\n")
                i += 1

    def run(self):
        self.get_html()
        self.raw_to_beauty_html()
        self.parse_html()
        self.write_to_file()

    @property
    def html(self):
        return self.__html.prettify()


