import requests
from bs4 import BeautifulSoup as bs


class WspinanieScraper:

    def __init__(self, list_of_terms: list, already_processed: list = []) -> None:
        self.url = 'wspinanie.pl'
        self.terms_to_look_for = list_of_terms
        self.already_processed = already_processed

    def open_site(self, site: str = 'http://wspinanie.pl') -> requests.models.Response:

        # TODO : blok try-catch
        site = requests.get(site)

        return site

    def get_articles_list(self) -> list:

        site = self.open_site()
        soup = bs(site.text, 'html.parser')

        articles_list = [item['href'] for item in soup.find_all('a', {'rel': 'bookmark'})]

        return articles_list

    def parse_article(self, article_link: str) -> dict:
        print(f'Parsing {article_link}')

        soup = bs(self.open_site(article_link).text, 'html.parser')

        body = soup.find('div', {'class': 'entry'})
        title = soup.find('h1', {'class': 'posttitle'})

        if title and body:
            for term in self.terms_to_look_for:
                if term in body.text:
                    result = {'content': str(body), 'title': title.text}
                    print(f'Returning {title.text}')
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
