import requests
import random
from pyfiglet import figlet_format
from termcolor import colored

# url = "https://icanhazdadjoke.com/search"
# url = "https://news.ycombinator.com/"


class Joke:

    def __init__(self):
        self._url = "https://icanhazdadjoke.com/search"
        self._term = ''
        self._response = None

    @staticmethod
    def print_game_name():
        header = figlet_format("Dad Joke 3000")
        header = colored(header, color="magenta")
        print(header)

    def get_term(self):
        self._term = input("Let me tell you a joke! Give me a topic: ")

    def get_joke(self):
        self._response = requests.get(
            self._url,
            headers={"Accept": "application/json"},
            params={"term": self._term}
        ).json()

    def print_joke(self):
        total_jokes = self._response["total_jokes"]
        if total_jokes == 0:
            print(f"Sorry, I don't have any jokes about {self._term}! Please try again.")
        elif total_jokes == 1:
            print(f"I've got one joke about {self._term}! Here it is:")
            print(self._response["results"][0]["joke"])
        else:
            print(f"I've got {total_jokes} jokes about {self._term}! Here's one:")
            print(random.choice(self._response["results"])["joke"])

    def run(self):
        Joke.print_game_name()
        self.get_term()
        self.get_joke()
        self.print_joke()


# print(f"Request to {url} came back with status code {response.status_code}")
# print(response.ok)
# print(response.headers)
# print(response.text)


# print(data["joke"])

if __name__ == "__main__":
    joke = Joke()
    joke.run()
