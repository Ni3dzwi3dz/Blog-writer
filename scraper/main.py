import requests
import json
# import config

class GeneralScraper:

    def __init__(self)-> None:
        self.scrapped_articles = []
        self.already_checked = []

    def check_sites(self) -> list:

        #for site in config.LIST_OF_SITES.keys:
            # i co tu się będzie działo?
            pass

    def load_already_checked(self, filename: str = 'alreday_checked.txt') -> None:
        try:
            with open (filename, 'r') as f:
                self.already_checked = [line.strip() for line in f]
        except FileNotFoundError:
            print('File not found. Nothing loaded')

if __name__ == '__main__':
    scrappy = GeneralScraper()
    
    scrappy.load_already_checked()