import requests
from bs4 import BeautifulSoup as bs


class GoryScraper:

    def __init__(self, list_of_terms: list, already_processed: list = []) -> None:
        self.url = 'http://goryonline.com'
        self.terms_to_look_for = list_of_terms
        self.already_processed = already_processed

    def get_articles_list(self, appendix: str = '/') -> list:

        results = []
        site = requests.get(self.url + appendix)
        soup = bs(site.text, 'html.parser')

        links = soup.findAll('div', {'class': 'title'})

        for link in links:

            link = bs(link.decode_contents(), 'html.parser')
            results.append(self.url + link.find('a')['href'])

        return results

    def parse_article(self, article: str) -> dict:

        print(f'Checking {article}')
        try:
            site = requests.get(article)
        except:
            print('Site loading error. Good bye!')
            return {}

        soup = bs(site.text, 'html.parser')

        title = soup.find('h1', {'class': 'pl10'})
        header = soup.find('div', {'class': 'pl10 mt10'})
        body = soup.find('div', {'class': 'mt20 pl20'})

        if title and header and body:
            for term in self.terms_to_look_for:
                if term in body.text:
                    result = {'title': title.text, 'content': str(header) + str(body)}
                    return result

        return {}

    def parse(self) -> list:

        articles = self.get_articles_list()
        results = []

        for article in articles:

            if article not in self.already_processed:
                result = self.parse_article(article)

                if result:
                    results.append(result)

                self.already_processed.append(article)

        return results
