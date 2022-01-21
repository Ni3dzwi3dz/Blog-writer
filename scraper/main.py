from scraper.bouldering import BoulderingScraper
from scraper.gory import GoryScraper
from scraper.wspinanie import WspinanieScraper


class GeneralScraper:

    def __init__(self, terms_to_look_for: list) -> None:
        self.scrapped_articles = []
        self.already_checked = []
        self.terms_too_look_for = terms_to_look_for

    def check_sites(self) -> list:

        result = self.parse_wspinanie() + self.parse_bouldering() + self.parse_goryonline()

        return result

    def load_already_checked(self, filename: str = 'alreday_checked.txt') -> None:
        try:
            with open(filename, 'r') as f:
                self.already_checked = [line.strip() for line in f]
        except FileNotFoundError:
            print('File not found. Nothing loaded')

    def save_already_checked(self, filename: str = 'already_checked.txt') -> None:

        with open(filename, 'w') as f:
            for item in self.already_checked:
                f.write(item)

    def parse_wspinanie(self) -> list:

        scrapper = WspinanieScraper(self.terms_too_look_for, self.already_checked)
        result = scrapper.parse()
        self.already_checked += scrapper.already_processed

        return result

    def parse_goryonline(self) -> list:

        scrapper = GoryScraper(self.terms_too_look_for, self.already_checked)
        result = scrapper.parse()
        self.already_checked += scrapper.already_processed

        return result

    def parse_bouldering(self) -> list:

        scrapper = BoulderingScraper(self.terms_too_look_for, self.already_checked)
        result = scrapper.parse()
        self.already_checked += scrapper.already_processed

        return result
