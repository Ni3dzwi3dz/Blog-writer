from blogUpdater.updater import BlogUpdater
from scraper import main
import config

if __name__ == '__main__':

    scrapper = main.GeneralScraper(config.TERMS_TO_LOOK_FOR)
    updater = BlogUpdater()

    scrapper.load_already_checked()
    results = scrapper.check_sites()

    updater.post_to_blog(results)


    scrapper.save_already_checked()


