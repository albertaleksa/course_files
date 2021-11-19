import requests
from bs4 import BeautifulSoup
import random
import time
from pyfiglet import figlet_format
from termcolor import colored
from csv import DictWriter
from csv import DictReader


class WebParser:
    """
    Class for parsing data (quotes) from website
    """
    def __init__(self, url):
        self._url = url
        self._current_url = ''
        self._html = ''
        self._results = []
        self._rnd_quote = {}

    @property
    def quote(self):
        return self._rnd_quote["quote"]

    @property
    def author(self):
        return self._rnd_quote["author"]

    @property
    def link(self):
        return self._rnd_quote["link"]

    @property
    def born_date(self):
        return self._rnd_quote["born_date"]

    @property
    def born_loc(self):
        return self._rnd_quote["born_loc"]

    @property
    def description(self):
        return self._rnd_quote["description"]

    def _get_html(self):
        """
        Put html info from website using get request and BeautifulSoup into var _html
        """
        response = requests.get(self._current_url)
        self._html = BeautifulSoup(response.text, "html.parser")

    def _get_quotes(self):
        """
        Get quotes from single page and add to list _results
        """
        quotes = self._html.find_all("div", class_="quote")
        for quote in quotes:
            text = quote.find(class_="text").get_text(strip=True)
            author = quote.find(class_="author").get_text(strip=True)
            auth_link = quote.find("a")["href"]
            self._results.append({
                'quote': text,
                'author': author,
                'link': auth_link
            })

    def get_all_quotes(self):
        """
        Get quotes from all pages.
        Used function _get_quotes()
        """
        link = "/page/1"
        while link:
            self._current_url = f"{self._url}{link}"
            self._get_html()
            self._get_quotes()
            # time.sleep(random.random())
            next_btn = self._html.find(class_="next")
            link = next_btn.find("a")["href"] if next_btn else None

    def get_random_quote(self):
        """
        Choose randomly quote from list _results and put it into var _rnd_quote
        """
        self._rnd_quote = random.choice(self._results)

    def _get_author_details(self):
        """
        Get info about author  (born date, born location and description)
        and add it into dictionary _rnd_quote
        """
        author_born_date = self._html.find(class_="author-born-date").get_text(strip=True)
        author_born_loc = self._html.find(class_="author-born-location").get_text(strip=True)[3:]
        author_desc = self._html.find(class_="author-description").get_text(strip=True)
        self._rnd_quote["born_date"] = author_born_date
        self._rnd_quote["born_loc"] = author_born_loc
        self._rnd_quote["description"] = author_desc

    def get_author_info(self):
        """
        Get info about author.
        Create correct url. Get needed html and then run func _get_author_details()
        """
        self._current_url = f"{self._url}{self._rnd_quote['link']}"
        self._get_html()
        self._get_author_details()

    def write_to_csv(self, filename):
        """
        Write quotes into file
        :param filename: file name of csv file
        """
        with open(filename, "w") as file:
            headers = ["quote", "author", "link"]
            csv_writer = DictWriter(file, fieldnames=headers)
            csv_writer.writeheader()
            for quote in self._results:
                csv_writer.writerow(quote)

    def read_from_csv(self, filename):
        """
        Read quotes from csv file into var _results
        :param filename: file name of csv file
        """
        with open(filename, "r") as file:
            csv_reader = DictReader(file)
            self._results = list(csv_reader)


class Game:
    """
    Class contains the whole logic of the game.
    The main goal of the game is to guess the whole name name of the author of the given quote.
    """

    def __init__(self):
        """
        Create the instance of the class WebParser and equal it to var _my_parser
        Than get all quotes from website (or from csv file)
        (and write all quotes to csv file)
        """
        self._my_parser = WebParser("https://quotes.toscrape.com/")
        self._my_parser.get_all_quotes()
        # self._my_parser.write_to_csv("quotes.csv")
        # self._my_parser.read_from_csv("quotes.csv")

    @staticmethod
    def print_game_name():
        """
        Print The Game name
        """
        header = figlet_format("Quotes Guessing Game")
        header = colored(header, color="magenta")
        print(header)

    def _play(self):
        """
        Check if the player guesses the author
        """
        remain_guesses = 4
        print("Here's a quote:")
        self._my_parser.get_random_quote()
        print(self._my_parser.quote)
        name_guess = ''
        while name_guess.lower() != self._my_parser.author.lower() and remain_guesses > 0:
            name_guess = input(f"Who said this? Guesses remaining: {remain_guesses}.\n")
            if name_guess.lower() == self._my_parser.author.lower():
                print("You guessed correctly! Congratulations!")
                break
            remain_guesses -= 1
            print()
            self._print_hint(remain_guesses)

    def _print_hint(self, val):
        """
        Print hints depending on the number of remaining guesses
        :param val: number of remaining guesses
        """
        if val == 3:
            self._my_parser.get_author_info()
            print(f"Here's a hint: The author was born on {self._my_parser.born_date} in {self._my_parser.born_loc}")
        elif val == 2:
            print(f"Here's a hint: The author's first name starts with {self._my_parser.author[0]}")
        elif val == 1:
            print(f"Here's a hint: The author's last name starts with {self._my_parser.author.split()[1][0]}")
        else:
            print(f"Sorry... Right answer: {self._my_parser.author}")
            print("Wish to win next time!")

    def _play_game(self):
        """
        Run game again if player wants it
        """
        self._play()
        again = ''
        while again.lower() not in ('y', 'yes', 'n', 'no'):
            again = input("Would you like to play again (y/n)?")
        if again.lower() in ('y', 'yes'):
            print("Great! Here we go again...")
            print()
            return self._play_game()
        else:
            print("Ok! See you next time!")

    def run(self):
        """
        For run game
        """
        Game.print_game_name()
        self._play_game()


if __name__ == "__main__":
    game = Game()
    game.run()

