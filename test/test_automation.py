"""Teszt automatizálás

Todo:
    [?] Regisztráció (5 db negatív és 1 db pozitív)
        [X] TC_001 - Új felhasználó fiók sikertelen létrehozása hiányos felhasználónév megadásával.
        [X] TC_002 - Új felhasználó fiók sikertelen létrehozása hiányos email cím megadásával.
        [X] TC_003 - Új felhasználó fiók sikertelen létrehozása hiányos jelszó megadásával.
        [X] TC_004 - Új felhasználó fiók sikeres létrehozása megfelelő adatok megadásával.
        [X] TC_005 - Új felhasználó fiók sikertelen létrehozása már regisztrált email cím megadásával.
        [?] TC_006 - Új felhasználó fiók sikertelen létrehozása már létező név megadásával.
                    # Manuálisan elbukik a teszt, ezért kihagyhatom az automatikusból?
    [X] Bejelentkezés (4 db negatív és 1 db pozitív)
        [X] TC_008 - Korábban regisztrált felhasznói fiókkal történő sikertelen bejelentkezés
                    jelszó mező üresen hagyása miatt.
        [X] TC_009 - Korábban regisztrált felhasznói fiókkal történő sikertelen bejelentkezés
                    email cím mező üresen hagyása miatt.
        [X] TC_010 - Korábban még nem regisztrált felhasznói fiókkal történő sikertelen bejelentkezés.
        [X] TC_011 - Korábban regisztrált felhasznói fiókkal történő sikertelen bejelentkezés hibás jelszó miatt.
        [X] TC_012 - Korábban regisztrált felhasznói fiókkal történő sikeres bejelentkezés.
    [X] Adatkezelési nyilatkozat használata (0 db negatív és 1 db pozitív) # negatív teszteset?
        [X] TC_007 - Adatkezelési tájékoztató sikeres elfogadása.
    [X] Adatok listázása (0 db negetív és 1 db pozitív) # negatív teszteset?
        [X] ATC_03 - Népszerű címkék sikeres listázása címkefelhőből
    [X] Több oldalas lista bejárása (0 db negetív és 1 db pozitív) # negatív teszteset?
        [X] ATC_04 - Felhasználó saját cikkjeinek sikeres bejárása
    [?] Új adat bevitel (3 db negetív és 2 db pozitív)
        [X] TC_024 - Korábban már regisztrált felhasználói fiókkal új cikk sikeres létrehozása.
        [X] TC_025 - Korábban már regisztrált felhasználói fiókkal új cikk sikertelen létrehozása
                     cikk címének hiánya miatt.
        [?] TC_026 - Korábban már regisztrált felhasználói fiókkal új cikk sikertelen létrehozása
                     már létező cikk cím miatt. # Manuálisan elbukik a teszt, ezért kihagyhatom az automatikusból?
        [?] TC_035 - Korábban létrehozott cikkhez történő sikertelen hozzászólás írása, hiányzó szöveg miatt.
                     # Manuálisan elbukik a teszt, ezért kihagyhatom az automatikusból?
        [ ] TC_036 - Korábban létrehozott cikkhez történő sikeres hozzászólás írása.
    [X] Ismételt és sorozatos adatbevitel adatforrásból (0 db negetív és 2 db pozitív) # negatív teszteset?
        [X] ATC_01 - Sorozatos sikeres regisztráció user_data.csv fájlból
        [X] ATC_02 - Sorozatos sikeres cikk hozzáadása article_data.tsv fájlból
    [ ] Meglévő adat módosítás (7 db negatív és 10 db pozitív)
        [X] TC_014 - Korábban regisztrált felhasználó fiók profilképének sikertelen megváltoztatatása
                     profilkép hivatkozásának nem megadása miatt.
        [X] TC_015 - Korábban regisztrált felhasználó fiók profilképének sikeres megváltoztatatása.
        [X] TC_016 - Korábban regisztrált felhasználó felhasználónevévek sikertelen megváltoztatatása
                     név nem megadása miatt.
        [X] TC_017 - Korábban regisztrált felhasználó felhasználónevének sikeres megváltoztatatása.
        [ ] TC_018 - Korábban regisztrált felhasználó felhasználónevévek sikertelen megváltoztatatása
                     már létező név miatt. # Manuálisan elbukik a teszt, ezért kihagyhatom az automatikusból?
        [X] TC_019 - Korábban regisztrált felhasználó email címének sikertelen megváltoztatatása
                     email cím mező üresen hagyása miatt.
        [X] TC_020 - Korábban regisztrált felhasználó email címének sikertelen megváltoztatatása
                     már létező email cím miatt.
        [ ] TC_021 - Korábban regisztrált felhasználó email címének sikeres megváltoztatatása.
                     # Manuálisan elbukik a teszt, ezért kihagyhatom az automatikusból?
        [X] TC_022 - Korábban regisztrált felhasználói fiók jelszavának sikeres megváltoztatása.
        [X] TC_023 - Korábban már regisztrált felhasználói fiók bemutatkozásának sikeres módosítása.
        [ ] TC_027 - Korábban létrehozott cikk címének sikertelen módosítása cikk címének nem megadása miatt.
                     # Manuálisan elbukik a teszt, ezért kihagyhatom az automatikusból?
        [ ] TC_028 - Korábban létrehozott cikk címének sikertelen módosítása meglévő cikk címére.
                     # Manuálisan elbukik a teszt, ezért kihagyhatom az automatikusból?
        [ ] TC_029 - Korábban létrehozott cikk címének sikeres módosítása.
        [ ] TC_030 - Korábban létrehozott cikk rövid leírásának sikeres módosítása.
        [ ] TC_031 - Korábban létrehozott cikk tartalmának sikeres módosítása.
        [ ] TC_032 - Korábban létrehozott cikk címkéinek sikeres módosítása.
        [ ] TC_033 - Korábban létrehozott cikk sikeres módosítása változatlan adatokkal.
                     # Manuálisan elbukik a teszt, ezért kihagyhatom az automatikusból?
    [ ] Adat vagy adatok törlése (0 db negetív és 2 db pozitív) # negatív teszteset?
        [X] TC_034 - Korábban létrehozott cikk sikeres törlése.
        [ ] TC_037 - Korábban létrehozott cikk alatt szereplő hozzászólás sikeres törlése.
    [X] Adatok lementése felületről (0 db negetív és 1 db pozitív) # negatív teszteset?
        [X] ATC_05 - Globális hírfolyam cikk címeinek mentése saved_data.tsv fájlba
    [X] Kijelentkezés (1 db pozitív 0 db negatív) # negatív teszteset?
        [X] TC_013 - Korábban létrehozott felhasználóval történő bejelentkezés után sikeres kijelentkezés végrehajtása.
"""

import csv
import page_object_model as pom
import configuration_chrome_driver as conf_driver
import allure


class TestRegistration:

    def setup_method(self):
        self.page = pom.ConduitSignUpPage(driver_source=conf_driver.ChromeDriver(remote=True))
        self.page.open(url='http://localhost:1667/#/register')
        self.modal = pom.ConduitGeneralModalWindow(driver_source=self.page)

    def teardown_method(self):
        self.page.close()

    @allure.id('TC_001')
    @allure.title('Új felhasználó fiók sikertelen létrehozása hiányos felhasználónév megadásával.')
    def test_register_negative_username(self):
        self.page.sign_up({
            'email': 'piros_cica23@gmail.com',
            'password': 'Piroska23'
        })
        assert self.modal.get_title_div().text == 'Registration failed!'
        assert self.modal.get_text_div().text == 'Username field required.'

    @allure.id('TC_002')
    @allure.title('Új felhasználó fiók sikertelen létrehozása hiányos email cím megadásával.')
    def test_register_negative_email(self):
        self.page.sign_up({
            'username': 'PirosCica23',
            'password': 'Piroska23'
        })
        assert self.modal.get_title_div().text == 'Registration failed!'
        assert self.modal.get_text_div().text == 'Email field required.'

    @allure.id('TC_003')
    @allure.title('Új felhasználó fiók sikertelen létrehozása hiányos jelszó megadásával.')
    def test_register_negative_password(self):
        self.page.sign_up({
            'username': 'PirosCica23',
            'email': 'piros_cica23@gmail.com'
        })
        assert self.modal.get_title_div().text == 'Registration failed!'
        assert self.modal.get_text_div().text == 'Password field required.'

    @allure.id('TC_004')
    @allure.title('Új felhasználó fiók sikeres létrehozása megfelelő adatok megadásával.')
    def test_register_positive(self):
        self.page.sign_up({
            'username': 'PirosCica23',
            'email': 'piros_cica23@gmail.com',
            'password': 'Piroska23'
        })
        assert self.modal.get_title_div().text == 'Welcome!'
        assert self.modal.get_text_div().text == 'Your registration was successful!'
        self.modal.click_ok_button()
        page = pom.ConduitHomePageWithLogin(driver_source=self.page)
        assert page.get_username_link().text == 'PirosCica23'

    @allure.id('TC_005')
    @allure.title('Új felhasználó fiók sikertelen létrehozása már regisztrált email cím megadásával.')
    def test_register_negative_exists(self):
        self.page.sign_up({
            'username': 'PirosCica23',
            'email': 'piros_cica23@gmail.com',
            'password': 'Piroska23'
        })
        assert self.modal.get_title_div().text == 'Registration failed!'
        assert self.modal.get_text_div().text == 'Email already taken.'


class TestPrivacyPolicy:

    def setup_method(self):
        self.page = pom.ConduitHomePage(driver_source=conf_driver.ChromeDriver(remote=True))
        self.page.open(url='http://localhost:1667/#/')

    def teardown_method(self):
        self.page.close()

    @allure.id('TC_007')
    @allure.title('Adatkezelési tájékoztató sikeres elfogadása.')
    def test_accept_cookie(self):
        self.page.click_accept_cookie_button()
        self.page.refresh()
        assert self.page.get_accept_cookie_button() is None


class TestLogin:
    def setup_method(self):
        self.page = pom.ConduitSignInPage(driver_source=conf_driver.ChromeDriver(remote=True))
        self.page.open(url='http://localhost:1667/#/login')
        self.modal = pom.ConduitGeneralModalWindow(driver_source=self.page)

    def teardown_method(self):
        self.page.close()

    @allure.id('TC_008')
    @allure.title(
        'Korábban regisztrált felhasznói fiókkal történő sikertelen bejelentkezés jelszó mező üresen hagyása miatt.')
    def test_login_negative_password(self):
        self.page.sign_in({
            'email': 'piros_cica23@gmail.com'
        })
        assert self.modal.get_title_div().text == 'Login failed!'
        assert self.modal.get_text_div().text == 'Password field required.'

    @allure.id('TC_009')
    @allure.title(
        'Korábban regisztrált felhasznói fiókkal történő sikertelen bejelentkezés email cím mező üresen hagyása miatt.')
    def test_login_negative_email(self):
        self.page.sign_in({
            'password': 'Piroska23'
        })
        assert self.modal.get_title_div().text == 'Login failed!'
        assert self.modal.get_text_div().text == 'Email field required.'

    @allure.id('TC_010')
    @allure.title('Korábban még nem regisztrált felhasznói fiókkal történő sikertelen bejelentkezés.')
    def test_login_negative_registered(self):
        self.page.sign_in({
            'email': 'piros_cica24@gmail.com',
            'password': 'Piroska24'
        })
        assert self.modal.get_title_div().text == 'Login failed!'
        assert self.modal.get_text_div().text == 'Invalid user credentials.'

    @allure.id('TC_011')
    @allure.title('Korábban regisztrált felhasznói fiókkal történő sikertelen bejelentkezés hibás jelszó miatt.')
    def test_login_negative_wrong(self):
        self.page.sign_in({
            'email': 'piros_cica23@gmail.com',
            'password': 'Piroska24'
        })
        assert self.modal.get_title_div().text == 'Login failed!'
        assert self.modal.get_text_div().text == 'Invalid user credentials.'

    @allure.id('TC_012')
    @allure.title('Korábban regisztrált felhasznói fiókkal történő sikeres bejelentkezés.')
    def test_login_positive(self):
        self.page.sign_in({
            'email': 'piros_cica23@gmail.com',
            'password': 'Piroska23'
        })
        page = pom.ConduitHomePageWithLogin(driver_source=self.page)
        assert page.get_username_link().text == 'PirosCica23'


class TestLogout:

    def setup_method(self):
        page = pom.ConduitSignInPage(driver_source=conf_driver.ChromeDriver(remote=True))
        page.open(url='http://localhost:1667/#/login')
        page.sign_in({
            'email': 'piros_cica23@gmail.com',
            'password': 'Piroska23'
        })
        self.page = pom.ConduitHomePageWithLogin(driver_source=page)

    def teardown_method(self):
        self.page.close()

    @allure.id('TC_013')
    @allure.title('Korábban létrehozott felhasználóval történő bejelentkezés után sikeres kijelentkezés végrehajtása.')
    def test_logout_positive(self):
        self.page.click_log_out_link()
        page = pom.ConduitHomePageWithoutLogin(driver_source=self.page)
        assert page.get_sign_in_link().is_displayed()


class TestEditProfile:

    def setup_method(self):
        page = pom.ConduitSignInPage(driver_source=conf_driver.ChromeDriver(remote=True))
        page.open(url='http://localhost:1667/#/login')
        page.sign_in({
            'email': 'piros_cica23@gmail.com',
            'password': 'Piroska23'
        })
        page = pom.ConduitHomePageWithLogin(driver_source=page)
        page.click_settings_link()
        self.page = pom.ConduitSettingsPage(driver_source=page)
        self.page.get_title_header()
        self.modal = pom.ConduitGeneralModalWindow(driver_source=page)

    def teardown_method(self):
        self.page.close()

    @allure.id('TC_014')
    @allure.title('Korábban regisztrált felhasználó fiók profilképének sikertelen megváltoztatatása' +
                  ' profilkép hivatkozásának nem megadása miatt.')
    def test_profile_picture_negative(self):
        self.page.update_settings({
            'profile_picture': ''
        })
        assert self.modal.get_title_div().text == 'Update failed!'
        assert self.modal.get_text_div().text == 'Image field required.'

    @allure.id('TC_015')
    @allure.title('Korábban regisztrált felhasználó fiók profilképének sikeres megváltoztatatása.')
    def test_profile_picture_positive(self):
        self.page.update_settings({
            'profile_picture': 'https://cdn-icons-png.flaticon.com/512/9327/9327067.png'
        })
        assert self.modal.get_title_div().text == 'Update successful!'
        self.modal.click_ok_button()
        page = pom.ConduitHomePageWithLogin(driver_source=self.page)
        page.click_username_link()
        page = pom.ConduitProfilePage(driver_source=page)
        assert page.get_profile_picture_img().get_attribute(
            'src') == 'https://cdn-icons-png.flaticon.com/512/9327/9327067.png'

    @allure.id('TC_016')
    @allure.title(
        'Korábban regisztrált felhasználó felhasználónevévek sikertelen megváltoztatatása név nem megadása miatt.')
    def test_profile_username_negative(self):
        self.page.update_settings({
            'username': ''
        })
        assert self.modal.get_title_div().text == 'Update failed!'
        assert self.modal.get_text_div().text == 'Username field required.'

    @allure.id('TC_017')
    @allure.title('Korábban regisztrált felhasználó felhasználónevének sikeres megváltoztatatása.')
    def test_profile_username_positive(self):
        self.page.update_settings({
            'username': 'VorosMacska23'
        })
        assert self.modal.get_title_div().text == 'Update successful!'
        self.modal.click_ok_button()
        page = pom.ConduitHomePageWithLogin(driver_source=self.page)
        page.click_username_link()
        page = pom.ConduitProfilePage(driver_source=page)
        assert page.get_profile_name_header().text == "VorosMacska23"

    @allure.id('TC_019')
    @allure.title('Korábban regisztrált felhasználó email címének sikertelen megváltoztatatása' +
                  'email cím mező üresen hagyása miatt.')
    def test_profile_email_negative_empty(self):
        self.page.update_settings({
            'email': ''
        })
        assert self.modal.get_title_div().text == 'Update failed!'
        assert self.modal.get_text_div().text == 'Email field required.'

    @allure.id('TC_020')
    @allure.title(
        'Korábban regisztrált felhasználó email címének sikertelen megváltoztatatása már létező email cím miatt.')
    def test_profile_email_negative_exists(self):
        self.page.update_settings({
            'email': 'testuser1@example.com'
        })
        assert self.modal.get_title_div().text == 'Update failed!'
        assert self.modal.get_text_div().text == 'Email already taken.'

    @allure.id('TC_023')
    @allure.title('Korábban már regisztrált felhasználói fiók bemutatkozásának sikeres módosítása.')
    def test_profile_bio_positive(self):
        self.page.update_settings({
            'bio': 'Szeretem a piros gombolyagokat.'
        })
        assert self.modal.get_title_div().text == 'Update successful!'
        self.modal.click_ok_button()
        page = pom.ConduitHomePageWithLogin(driver_source=self.page)
        page.click_username_link()
        page = pom.ConduitProfilePage(driver_source=page)
        assert page.get_profile_bio_paragraph().text == "Szeretem a piros gombolyagokat."

    @allure.id('TC_022')
    @allure.title('Korábban regisztrált felhasználói fiók jelszavának sikeres megváltoztatása.')
    def test_profile_password_positive(self):
        self.page.update_settings({
            'password': 'PirosCica23'
        })
        assert self.modal.get_title_div().text == 'Update successful!'
        self.modal.click_ok_button()
        page = pom.ConduitHomePageWithLogin(driver_source=self.page)
        page.click_log_out_link()
        page = pom.ConduitHomePageWithoutLogin(driver_source=page)
        page.click_sign_in_link()
        page = pom.ConduitSignInPage(driver_source=page)
        page.sign_in({
            'email': 'piros_cica23@gmail.com',
            'password': 'PirosCica23'
        })
        page = pom.ConduitHomePageWithLogin(driver_source=page)
        assert page.get_username_link().text == 'VorosMacska23'


class TestRepeatedInputFromSource:

    def setup_method(self):
        self.registration = pom.ConduitSignUpPage(driver_source=conf_driver.ChromeDriver(remote=True))
        self.modal = pom.ConduitGeneralModalWindow(driver_source=self.registration)
        self.home_with_login = pom.ConduitHomePageWithLogin(driver_source=self.registration)
        self.home_without_login = pom.ConduitHomePageWithoutLogin(driver_source=self.registration)
        self.home_without_login.open(url='http://localhost:1667/#/')
        self.new_article = pom.ConduitNewArticle(driver_source=self.registration)
        self.article = pom.ConduitArticle(driver_source=self.registration)

    def teardown_method(self):
        self.registration.close()

    @allure.id('ATC_01')
    @allure.title('Sorozatos sikeres regisztráció user_data.csv fájlból')
    def test_register_positive(self):
        with open('./test/user_data.csv', mode='r') as user_data_csv:
            csv_reader = csv.DictReader(user_data_csv)
            for record in csv_reader:
                self.home_without_login.click_sign_up_link()
                self.registration.sign_up(record)
                assert self.modal.get_title_div().text == 'Welcome!'
                assert self.modal.get_text_div().text == 'Your registration was successful!'
                self.modal.click_ok_button()
                assert self.home_with_login.get_username_link().text == record['username']
                self.home_with_login.click_log_out_link()

    @allure.id('ATC_02')
    @allure.title('Sorozatos sikeres cikk hozzáadása article_data.tsv fájlból')
    def test_new_article_positive(self):
        self.home_without_login.click_sign_in_link()
        page = pom.ConduitSignInPage(driver_source=self.modal)
        page.sign_in({
            'email': 'foltos_cica23@gmail.com',
            'password': 'FoltosCica23'
        })
        assert self.home_with_login.get_username_link().text == 'FoltosCica23'
        with open('./test/article_data.tsv', mode='r', encoding='utf-8-sig') as user_data_csv:
            csv_reader = csv.DictReader(user_data_csv, delimiter="\t")
            for record in csv_reader:
                self.home_with_login.click_new_article_link()
                self.new_article.new_article({
                    'title': record['title'],
                    'about': record['about'],
                    'article': f'# Napi idézet\n\n> {record["article"]}\n\n*{record["author"]}*',
                    'tags': record['tags']
                })
                assert self.article.get_title_header().text == record['title']
                for element, tag in zip(self.article.get_tag_list(), record['tags'].split(',')):
                    assert element.text == tag


class TestWriteAndDeleteArticle:

    def setup_method(self):
        page = pom.ConduitSignInPage(driver_source=conf_driver.ChromeDriver(remote=True))
        page.open(url='http://localhost:1667/#/login')
        page.sign_in({
            'email': 'piros_cica23@gmail.com',
            'password': 'PirosCica23'
        })
        self.page = pom.ConduitHomePageWithLogin(driver_source=page)
        self.page.click_new_article_link()
        self.new_article = pom.ConduitNewArticle(driver_source=page)
        self.article = pom.ConduitArticle(driver_source=page)
        self.modal = pom.ConduitGeneralModalWindow(driver_source=page)

    def teardown_method(self):
        self.page.close()

    @allure.id('TC_024')
    @allure.title('Korábban már regisztrált felhasználói fiókkal új cikk sikeres létrehozása.')
    def test_new_article_positive(self):
        tags = 'cica,kerdes,valasz'
        self.new_article.new_article({
            'title': 'Te milyen cica vagy?',
            'about': 'Cicák fajtái',
            'article': '# Típusok:\n\n- Rövid szőrű fajták\n- Félhosszú szőrű fajták\n' +
                       '- Hosszú szőrű fajták\n- Hibrid fajták\n\n' +
                       '**Írd meg kommentben a fentiek közül!**',
            'tags': tags
        })
        assert self.article.get_title_header().text == 'Te milyen cica vagy?'
        for element, tag in zip(self.article.get_tag_list(), tags.split(',')):
            assert element.text == tag

    @allure.id('TC_025')
    @allure.title(
        'Korábban már regisztrált felhasználói fiókkal új cikk sikertelen létrehozása cikk címének hiánya miatt.')
    def test_new_article_negative(self):
        self.new_article.new_article({
            'title': '',
            'about': 'Cicák fajtái',
            'article': '# Típusok:\n\n- Rövid szőrű fajták\n- Félhosszú szőrű fajták\n' +
                       '- Hosszú szőrű fajták\n- Hibrid fajták\n\n' +
                       '**Írd meg kommentben a fentiek közül!**',
            'tags': 'cica,kerdes,valasz'
        })
        assert self.modal.get_title_div().text == 'Oops!'

    @allure.id('TC_034')
    @allure.title('Korábban létrehozott cikk sikeres törlése.')
    def test_delete_article_positive(self):
        self.page.click_username_link()
        feed = pom.ConduitGeneralFeed(driver_source=self.page)
        profile_page = pom.ConduitProfilePage(driver_source=feed)
        profile_page.get_profile_name_header()
        articles = feed.get_articles_header()
        articles = list(filter(lambda element: element.text == 'Te milyen cica vagy?', articles))
        assert len(articles) == 1
        articles[0].click()
        self.article.click_delete_article()
        self.page.get_username_link()
        self.page.click_username_link()
        profile_page.get_profile_name_header()
        articles = feed.get_articles_header()
        if len(articles) > 0:
            articles = list(filter(lambda element: element.text == 'Te milyen cica vagy?', articles))
        assert len(articles) == 0


class TestListAndSaveData:
    def setup_method(self):
        page = pom.ConduitSignInPage(driver_source=conf_driver.ChromeDriver(remote=True))
        page.open(url='http://localhost:1667/#/login')
        page.sign_in({
            'email': 'foltos_cica23@gmail.com',
            'password': 'FoltosCica23'
        })
        self.page = pom.ConduitHomePageWithLogin(driver_source=page)
        self.profile = pom.ConduitProfilePage(driver_source=page)
        self.pagination = pom.ConduitGeneralPagination(driver_source=page)
        self.feed = pom.ConduitGeneralFeed(driver_source=page)

    def teardown_method(self):
        self.page.close()

    @allure.id('ATC_03')
    @allure.title('Népszerű címkék sikeres listázása címkefelhőből')
    def test_collect_tags_positive(self):
        links = self.page.get_popular_tag_links()
        self.page.get_username_link()
        assert len(links) > 0

    @allure.id('ATC_04')
    @allure.title('Felhasználó saját cikkjeinek sikeres bejárása')
    def test_collect_my_articles_positive(self):
        self.page.click_username_link()
        self.profile.get_profile_name_header()
        self.pagination.get_active_page_number_link()
        current_page = 0
        while True:
            current_page += 1
            assert self.pagination.get_active_page_number_link().text == str(current_page)
            articles = self.feed.get_articles_header()
            assert len(articles) > 0
            if self.pagination.click_next_pagination_link() is False:
                break

    @allure.id('ATC_05')
    @allure.title('Globális hírfolyam cikk címeinek mentése saved_data.tsv fájlba')
    def test_save_global_feed_positive(self):
        self.pagination.get_active_page_number_link()
        page_numbers = self.pagination.get_pagination_links()
        assert len(page_numbers) > 0
        with open('./test/saved_data.tsv', mode='w', encoding='utf-8', newline='') as csv_file:
            fieldnames = ['oldalszam', 'cim']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter='\t')
            writer.writeheader()
            while True:
                oldalszam = self.pagination.get_active_page_number_link().text
                self.pagination.get_active_page_number_link()
                self.page.get_username_link()
                headers = self.feed.get_articles_header()
                assert len(headers) > 0
                for header in headers:
                    writer.writerow({'oldalszam': oldalszam, 'cim': header.text})
                if self.pagination.click_next_pagination_link() is False:
                    break
