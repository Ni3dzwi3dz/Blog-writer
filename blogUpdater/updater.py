import config
import os
from httplib2 import Http
from oauth2client.file import Storage
from oauth2client import tools
from oauth2client.client import flow_from_clientsecrets, OAuth2Credentials
from googleapiclient.discovery import build
from googleapiclient.http import HttpRequest


class BlogUpdater:

    def __init__(self) -> None:
        self.http = Http()
        self.credentials = self.authorize()
        self.service = self.build_service()


    def authorize(self) -> OAuth2Credentials:

        credential_dir = os.path.join(os.path.dirname(__file__), 'cached_oauth_credentials')

        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir, 'googleapis.json')

        store = Storage(credential_path)
        credentials = store.get()

        if not credentials:
            flow = flow_from_clientsecrets(config.CREDENTIALS, scope=config.SCOPES)
            flow.user_agent = config.USER_AGENT
            credentials = tools.run_flow(
                flow,
                store,
                tools.argparser.parse_args(args=['--noauth_local_webserver']))
            store.put(credentials)
        else:
            credentials.refresh(self.http)

        return credentials

    def build_service(self):

        if not self.credentials:
            self.authorize()

        service = build('blogger', 'v3', credentials=self.credentials)
        
        return service

    def get_blog_id(self) -> str:
        blogs = self.service.blogs()
        response = blogs.get(blogId=config.BLOG_ID, maxPosts=3, view='ADMIN').execute()
        print(response.headers)
        print(response.body)



    def post_to_blog(self,list_of_posts: list) -> None:

        posts = self.service.posts()
        for post in list_of_posts:
            response = posts.insert(blogId=config.BLOG_ID, body=post, isDraft=True).execute()
            print(response.headers)
            print(response.body)


if __name__ == '__main__':
    updater = BlogUpdater()
    updater.get_blog_id()
    #updater.post_to_blog([{'body': '<div class="entry">\n<p>Przez ostatnie dwa dni miałem przyjemność powspinać się z <strong>Wadimem Jabłońskim</strong>. Dzięki zebranym przez Wadima informacjom cel na ostatnie dni został dobrany wyśmienicie, a była nim południowa ściana Kieżmarskiego Szczytu.<span id="more-246859"></span></p>\n<p style="text-align: center"><strong>***</strong></p>\n<p style="text-align: left">Ściana ta z uwagi na południową wystawę kojarzy się głównie z letnim wspinaniem, jednak ostatnie dni były wyjątkowe. Po ostatnich odwilżach, a następnie utrzymujących się mrozach, na ścianie pojawiło się sporo lodu. W dniach, kiedy my wspinaliśmy się w ścianie, tj. 11 i 12 stycznia, lodu było już mniej w porównaniu do dni poprzednich. Generalnie odcinki wycenione przez nas za WI4 na obu pokonanych drogach, pomimo niewygórowanych trudności, z uwagi na cienki lód były nieasekurowane. Dodatkowo w wielu miejscach, w szczególności drogi Prawego Puskasa (robocza nazwa Puskasowy Mikst), lód był mocno odspojony od skały i loteryjny. W związku z tym niektóre odcinki zamiast z pozoru łatwym lodem woleliśmy pokonać trudniejszą technicznie, ale dającą możliwość asekuracji skałą.</p>\n<p>Z uwagi (na ile nam wiadomo) brak przejść tych linii w taki sposób, jak my to zrobiliśmy, pozwoliliśmy sobie na nadanie im nazw roboczych.</p>\n<p><strong>Wielkie Zacięcie Integrale</strong></p>\n<p>Jest to kombinacja formacji Depresja i Płyty Kellego (w naszym odczuciu tworzą razem ewidentne dolne wielkie zacięcie) oraz góra Wielkiego Zacięcia. Dolną część, aż do startu z Rampy w Wielkie Zacięcie, z uwagi na niewielkie trudności pokonujemy bez asekuracji. Reszta drogi, poza czysto drytoolowym wyciągiem za M7 (latem VI+), to cudny mikst. W tych warunkach droga petarda.</p>\n<div class="wp-caption aligncenter" id="attachment_246860" style="width: 630px"><a data-rel="lightbox-gallery-bKUZkGOf" data-rl_caption="" data-rl_title=\'Start w wyciąg M7 na "Wielkim Zacięciu Integrale" (fot. J. Kuczera, W. Jabłoński)\' href="https://wspinanie.pl/wp-content/uploads/2022/01/wielkie-zaciecie-integrale-wyciag-M7.jpg" title=\'Start w wyciąg M7 na "Wielkim Zacięciu Integrale" (fot. J. Kuczera, W. Jabłoński)\'><img alt=\'Start w wyciąg M7 na "Wielkim Zacięciu Integrale" (fot. J. Kuczera, W. Jabłoński)\' aria-describedby="caption-attachment-246860" class="size-large wp-image-246860" height="286" loading="lazy" sizes="(max-width: 620px) 100vw, 620px" src="https://wspinanie.pl/wp-content/uploads/2022/01/wielkie-zaciecie-integrale-wyciag-M7-620x286.jpg" srcset="https://wspinanie.pl/wp-content/uploads/2022/01/wielkie-zaciecie-integrale-wyciag-M7-620x286.jpg 620w, https://wspinanie.pl/wp-content/uploads/2022/01/wielkie-zaciecie-integrale-wyciag-M7-400x184.jpg 400w, https://wspinanie.pl/wp-content/uploads/2022/01/wielkie-zaciecie-integrale-wyciag-M7-768x354.jpg 768w, https://wspinanie.pl/wp-content/uploads/2022/01/wielkie-zaciecie-integrale-wyciag-M7-1536x708.jpg 1536w, https://wspinanie.pl/wp-content/uploads/2022/01/wielkie-zaciecie-integrale-wyciag-M7.jpg 2040w" width="620"/></a><p class="wp-caption-text" id="caption-attachment-246860">Start w wyciąg M7 na „Wielkim Zacięciu Integrale” (fot. J. Kuczera, W. Jabłoński)</p></div>\n<p>Co do samego stylu to ani ja ani Wadim nie byliśmy ani razu na Wielkim Zacięciu, jednak dla przyzwoitości należy wspomnieć, że dzień przed wspinaniem widziałem krótki kadr z filmu na którym ktoś wspina się na pierwszym trudnym wyciągu. Także styl przejścia to 1. wyciąg mocny Flash , a tak reszta OS. Droga oferuje świetną asekurację i stałe stanowiska, co sprawia, że powaga drogi maleje.</p>\n<div class="wp-caption aligncenter" id="attachment_246861" style="width: 630px"><a data-rel="lightbox-gallery-bKUZkGOf" data-rl_caption="" data-rl_title="Spojrzenie w dół na wyc. M7-" href="https://wspinanie.pl/wp-content/uploads/2022/01/wielkie-zaciecie-integrale-wyciag-M7-.jpg" title="Spojrzenie w dół na wyc. M7-"><img alt=\'Spojrzenie w dół na wyciąg M7- na "Wielkim Zacięciu Integrale" (fot. J. Kuczera, W. Jabłoński)\' aria-describedby="caption-attachment-246861" class="wp-image-246861 size-large" height="465" loading="lazy" sizes="(max-width: 620px) 100vw, 620px" src="https://wspinanie.pl/wp-content/uploads/2022/01/wielkie-zaciecie-integrale-wyciag-M7--620x465.jpg" srcset="https://wspinanie.pl/wp-content/uploads/2022/01/wielkie-zaciecie-integrale-wyciag-M7--620x465.jpg 620w, https://wspinanie.pl/wp-content/uploads/2022/01/wielkie-zaciecie-integrale-wyciag-M7--400x300.jpg 400w, https://wspinanie.pl/wp-content/uploads/2022/01/wielkie-zaciecie-integrale-wyciag-M7--768x576.jpg 768w, https://wspinanie.pl/wp-content/uploads/2022/01/wielkie-zaciecie-integrale-wyciag-M7--1536x1152.jpg 1536w, https://wspinanie.pl/wp-content/uploads/2022/01/wielkie-zaciecie-integrale-wyciag-M7-.jpg 2000w" width="620"/></a><p class="wp-caption-text" id="caption-attachment-246861">Spojrzenie w dół na wyciąg M7- na „Wielkim Zacięciu Integrale” (fot. J. Kuczera, W. Jabłoński)</p></div>\n<p>Trudności drogi to M7, WI4, 550 m przewyższenia, 5h 50min – czas przejścia do szczytu.</p>\n<p><strong>Puskasowy Mikst</strong></p>\n<p>W około 85% droga biegnie Prawym Puskasem, jednakże pierwszy trudny wyciąg za M7, tak jak i częściowo drugi wyciąg, biegnie niezależnym terenem. Podobnie sprawa wygląda na ostatnim wyciągu i prawdopodobnie częściowo na wyciągu za M6/M6+, ale tutaj działa to w drugą stronę – nędzny lód wypełniał formację, którą przypuszczalnie biegnie oryginalna linia. W związku z tym my poszliśmy od prawej, gorszą jakościowo skałą, ale dającą możliwość asekuracji.</p>\n<div class="wp-caption aligncenter" id="attachment_246863" style="width: 560px"><a data-rel="lightbox-gallery-bKUZkGOf" data-rl_caption="" data-rl_title=\'Końcówka dolnego wyciągu M7 na drodze "Puskasowy Mikst" (fot. J. Kuczera, W. Jabłoński)\' href="https://wspinanie.pl/wp-content/uploads/2022/01/puskasowy-mikst-wyciag-M7.jpg" title=\'Końcówka dolnego wyciągu M7 na drodze "Puskasowy Mikst" (fot. J. Kuczera, W. Jabłoński)\'><img alt=\'Końcówka dolnego wyciągu M7 na drodze "Puskasowy Mikst" (fot. J. Kuczera, W. Jabłoński)\' aria-describedby="caption-attachment-246863" class="wp-image-246863" height="739" loading="lazy" sizes="(max-width: 550px) 100vw, 550px" src="https://wspinanie.pl/wp-content/uploads/2022/01/puskasowy-mikst-wyciag-M7-620x833.jpg" srcset="https://wspinanie.pl/wp-content/uploads/2022/01/puskasowy-mikst-wyciag-M7-620x833.jpg 620w, https://wspinanie.pl/wp-content/uploads/2022/01/puskasowy-mikst-wyciag-M7-400x538.jpg 400w, https://wspinanie.pl/wp-content/uploads/2022/01/puskasowy-mikst-wyciag-M7-768x1032.jpg 768w, https://wspinanie.pl/wp-content/uploads/2022/01/puskasowy-mikst-wyciag-M7-1143x1536.jpg 1143w, https://wspinanie.pl/wp-content/uploads/2022/01/puskasowy-mikst-wyciag-M7.jpg 1488w" width="550"/></a><p class="wp-caption-text" id="caption-attachment-246863">Końcówka dolnego wyciągu M7 na drodze „Puskasowy Mikst” (fot. J. Kuczera, W. Jabłoński)</p></div>\n<p>W naszej ocenie droga ta zdecydowanie jest poważniejsza od Wielkiego Zacięcia Integrale z uwagi na brak stałej asekuracji (w sumie napotkaliśmy tylko 2 stare haki) i ilość wspinaczkowego terenu. Asekuracja generalnie jest dobra. Co do urody drogi – to absolutna piękność. Zdecydowanie najlepsza skalno-lodowa droga, po której wspinałem się w Tatrach.</p>\n<div class="wp-caption aligncenter" id="attachment_246864" style="width: 630px"><a data-rel="lightbox-gallery-bKUZkGOf" data-rl_caption="" data-rl_title=\'Wyciąg M6/6+ na drodze "Puskasowy Mikst" (fot. J. Kuczera, W. Jabłoński)\' href="https://wspinanie.pl/wp-content/uploads/2022/01/puskasowy-mikst-wyciag-M6.jpg" title=\'Wyciąg M6/6+ na drodze "Puskasowy Mikst" (fot. J. Kuczera, W. Jabłoński)\'><img alt=\'Wyciąg M6/6+ na drodze "Puskasowy Mikst" (fot. J. Kuczera, W. Jabłoński)\' aria-describedby="caption-attachment-246864" class="size-large wp-image-246864" height="465" loading="lazy" sizes="(max-width: 620px) 100vw, 620px" src="https://wspinanie.pl/wp-content/uploads/2022/01/puskasowy-mikst-wyciag-M6-620x465.jpg" srcset="https://wspinanie.pl/wp-content/uploads/2022/01/puskasowy-mikst-wyciag-M6-620x465.jpg 620w, https://wspinanie.pl/wp-content/uploads/2022/01/puskasowy-mikst-wyciag-M6-400x300.jpg 400w, https://wspinanie.pl/wp-content/uploads/2022/01/puskasowy-mikst-wyciag-M6-768x576.jpg 768w, https://wspinanie.pl/wp-content/uploads/2022/01/puskasowy-mikst-wyciag-M6-1536x1152.jpg 1536w, https://wspinanie.pl/wp-content/uploads/2022/01/puskasowy-mikst-wyciag-M6.jpg 2000w" width="620"/></a><p class="wp-caption-text" id="caption-attachment-246864">Wyciąg M6/6+ na drodze „Puskasowy Mikst” (fot. J. Kuczera, W. Jabłoński)</p></div>\n<p>Styl przejścia OS.</p>\n<p>Trudności drogi to M7, WI4, 550 m przewyższenia, 7h – czas przejścia do szczytu.</p>\n<div class="wp-caption aligncenter" id="attachment_246867" style="width: 630px"><a data-rel="lightbox-gallery-bKUZkGOf" data-rl_caption="" data-rl_title=\'Topo dróg "Wielkie Zacięcie Integrale" i "Puskasowy Mikst" (fot. J. Kuczera, W. Jabłoński)\' href="https://wspinanie.pl/wp-content/uploads/2022/01/kiezmarski-kuczera-jablonski-topo-scaled.jpg" title=\'Topo dróg "Wielkie Zacięcie Integrale" i "Puskasowy Mikst" (fot. J. Kuczera, W. Jabłoński)\'><img alt="" aria-describedby="caption-attachment-246867" class="size-large wp-image-246867" height="465" loading="lazy" sizes="(max-width: 620px) 100vw, 620px" src="https://wspinanie.pl/wp-content/uploads/2022/01/kiezmarski-kuczera-jablonski-topo-620x465.jpg" srcset="https://wspinanie.pl/wp-content/uploads/2022/01/kiezmarski-kuczera-jablonski-topo-620x465.jpg 620w, https://wspinanie.pl/wp-content/uploads/2022/01/kiezmarski-kuczera-jablonski-topo-400x300.jpg 400w, https://wspinanie.pl/wp-content/uploads/2022/01/kiezmarski-kuczera-jablonski-topo-768x576.jpg 768w, https://wspinanie.pl/wp-content/uploads/2022/01/kiezmarski-kuczera-jablonski-topo-1536x1152.jpg 1536w, https://wspinanie.pl/wp-content/uploads/2022/01/kiezmarski-kuczera-jablonski-topo-2048x1536.jpg 2048w" width="620"/></a><p class="wp-caption-text" id="caption-attachment-246867">Topo dróg „Wielkie Zacięcie Integrale” i „Puskasowy Mikst” (fot. J. Kuczera, W. Jabłoński)</p></div>\n<p><strong>Kilka uwag na koniec</strong></p>\n<ol>\n<li>M7 to trochę więcej jak zimowo-klasyczne 7. Według mnie tatrzańska wycena zimowo-klasyczna jest świetna do wyceniania bardziej parchatych dróg okraszonych trawą. Natomiast użycie skali mikstowej na pokonanych przez nas drogach, gdzie jest bardzo lito, trawy niemalże brak, a lodu sporo wydaje się bardziej akuratne.</li>\n<li>Jeśli ktoś ma jakieś informacje na temat tak przebytych dróg, to proszę o informacje.</li>\n<li>Dla osób chcących wspinać się co najmniej 2 dni, dobrą opcją jest nocleg w schronisku znajdującym się 5 min drogi poniżej Skalnatego Plesa. My z tej opcji skorzystaliśmy i to był strzał w dziesiątkę.</li>\n</ol>\n<p style="text-align: right"><strong>Jan Kuczera<br/>\n</strong>Instruktor PZA, TOPR, KW Kraków, KS Korona, HardRock-wspinanie.pl, blackdiamondequipment, cragstore, PHS<strong><br/>\n</strong></p>\n<p>O wspinaniu na Kieżmarskim <a href="https://www.facebook.com/wadim.j">pisze na swoim profilu</a> także Wadim Jabłoński.</p>\n<div style="width:300px; height:250px; margin:10px auto; text-align:center"><ins data-revive-id="b0d79768e9f3c66600fc233d58dc9beb" data-revive-zoneid="75"></ins>\n</div>\n<script async="" src="//ads.wspinanie.pl/delivery/asyncjs.php"></script>\n<div style="clear:both;"></div>\n</div>', 'title': '  Paradne wspinanie na Kieżmarskim: Jasiek Kuczera i Wadim Jabłoński'}])
