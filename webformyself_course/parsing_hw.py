from webformyself_course.website_parsing import WebParser


def main():
    my_parsing = WebParser("https://www.ua-football.com/sport", 'news.txt')
    my_parsing.run()
    print(my_parsing.html)


if __name__ == '__main__':
    main()