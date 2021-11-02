from bs4 import BeautifulSoup
import urllib.request
import ssl

# Documentation
# https://www.crummy.com/software/BeautifulSoup/bs4/doc.ru/bs4ru.html#


def get_html(url):
    context = ssl._create_unverified_context()
    req = urllib.request.urlopen(url, context=context)
    html = req.read()

    return html


def parse_html(html_to_parse):
    soup = BeautifulSoup(html_to_parse, "html.parser")
    # print(soup.prettify())

    news = soup.find_all('li', class_='liga-news-item')
    results = []

    for item in news:
        title = item.find('span', class_='d-block').get_text(strip=True)
        desc = item.find('span', class_='name-dop').get_text(strip=True)
        href = item.find('a', class_='liga-news-item-link').get('href')
        results.append({
            'title': title,
            'desc': desc,
            'href': href
        })

    return results


def write_to_file(lst):
    with open('news.txt', 'w', encoding='utf-8') as f:
        i = 1
        for item in lst:
            f.write(f"News N {i}\n\n Name: {item['title']}\n Description: {item['desc']}\n Link: {item['href']}\n\n"
                    f"*************************\n")
            i += 1


def main():
    html = get_html('https://www.ua-football.com/sport')
    result_lst = parse_html(html)
    write_to_file(result_lst)


if __name__ == '__main__':
    main()
