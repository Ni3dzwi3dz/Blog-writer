import requests
from bs4 import BeautifulSoup as bs

class BoulderingScraper:

    def __init__(self,list_of_terms: list, already_processed: list = []):

        self.url = 'http://bouldering.pl'
        self.terms_to_look_for = list_of_terms
        self.already_processed = already_processed


    def get_articles_list(self) -> list:

        results = []
        site = requests.get(self.url)
        soup = bs(site.text, 'html.parser')


        links = soup.findAll('div', {'class': 'tytul'})

        for link in links:
            print(f'Checking {link}')
            link = bs(link.decode_contents(),'html.parser')
            results.append(link.find('a')['href'])

        return results

    def parse_article(self,article: str) -> dict:

        result = {}
        site = requests.get(article)
        soup = bs(site.text,'html.parser')

        body = soup.find('div', {'class': 'tresc'})
        title = soup.find('div', {'class': 'tytul'})

        if body and title:
            for term in self.terms_to_look_for:
                if term in body.text:
                    result['title'] = title.text
                    result['body'] = str(body)
                    break

        return result

    def parse(self) -> list:

        results = []
        articles = self.get_articles_list()

        for article in articles:

            if article not in self.already_processed:
                result = self.parse_article(article)

                if result:
                    results.append(result)

            self.already_processed.append(article)

        return results
