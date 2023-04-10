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
from selenium.webdriver.common.keys import Keys


class TestRegistration:

    def setup_method(self):
        driver = conf_driver.get_chrome_driver(remote=True)
        self.page = pom.ConduitSignUpPage(driver=driver)
        self.page.open(url='http://localhost:1667/#/register')
        self.modal = pom.ConduitGeneralModalWindow(driver=driver)

    def teardown_method(self):
        self.page.close()

    @allure.id('TC_001')
    @allure.title('Új felhasználó fiók sikertelen létrehozása hiányos felhasználónév megadásával.')
    def test_register_negative_username(self):
        self.page.email_input().send_keys('piros_cica23@gmail.com')
        self.page.password_input().send_keys('Piroska23')
        self.page.sign_up().click()
        assert self.modal.title().text == 'Registration failed!'
        assert self.modal.text().text == 'Username field required.'

    @allure.id('TC_002')
    @allure.title('Új felhasználó fiók sikertelen létrehozása hiányos email cím megadásával.')
    def test_register_negative_email(self):
        self.page.username_input().send_keys('PirosCica23')
        self.page.password_input().send_keys('Piroska23')
        self.page.sign_up().click()
        assert self.modal.title().text == 'Registration failed!'
        assert self.modal.text().text == 'Email field required.'

    @allure.id('TC_003')
    @allure.title('Új felhasználó fiók sikertelen létrehozása hiányos jelszó megadásával.')
    def test_register_negative_password(self):
        self.page.username_input().send_keys('PirosCica23')
        self.page.email_input().send_keys('piros_cica23@gmail.com')
        self.page.sign_up().click()
        assert self.modal.title().text == 'Registration failed!'
        assert self.modal.text().text == 'Password field required.'

    @allure.id('TC_004')
    @allure.title('Új felhasználó fiók sikeres létrehozása megfelelő adatok megadásával.')
    def test_register_positive(self):
        self.page.username_input().send_keys('PirosCica23')
        self.page.email_input().send_keys('piros_cica23@gmail.com')
        self.page.password_input().send_keys('Piroska23')
        self.page.sign_up().click()
        assert self.modal.title().text == 'Welcome!'
        assert self.modal.text().text == 'Your registration was successful!'
        self.modal.ok().click()
        page = pom.ConduitHomePageWithLogin(self.page.driver)
        assert page.username_link().text == 'PirosCica23'

    @allure.id('TC_005')
    @allure.title('Új felhasználó fiók sikertelen létrehozása már regisztrált email cím megadásával.')
    def test_register_negative_exists(self):
        self.page.username_input().send_keys('PirosCica23')
        self.page.email_input().send_keys('piros_cica23@gmail.com')
        self.page.password_input().send_keys('Piroska23')
        self.page.sign_up().click()
        assert self.modal.title().text == 'Registration failed!'
        assert self.modal.text().text == 'Email already taken.'


class TestPrivacyPolicy:

    def setup_method(self):
        self.page = pom.ConduitHomePageWithoutLogin(driver=conf_driver.get_chrome_driver(remote=True))
        self.page.open(url='http://localhost:1667/#/')

    def teardown_method(self):
        self.page.close()

    @allure.id('TC_007')
    @allure.title('Adatkezelési tájékoztató sikeres elfogadása.')
    def test_accept_cookie(self):
        self.page.accept_cookie(in_list=False).click()
        self.page.refresh()
        assert len(self.page.accept_cookie(in_list=True)) == 0


class TestLogin:
    def setup_method(self):
        driver = conf_driver.get_chrome_driver(remote=True)
        self.page = pom.ConduitSignInPage(driver=driver)
        self.page.open(url='http://localhost:1667/#/login')
        self.modal = pom.ConduitGeneralModalWindow(driver=driver)

    def teardown_method(self):
        self.page.close()

    @allure.id('TC_008')
    @allure.title(
        'Korábban regisztrált felhasznói fiókkal történő sikertelen bejelentkezés jelszó mező üresen hagyása miatt.')
    def test_login_negative_password(self):
        self.page.email_input().send_keys('piros_cica23@gmail.com')
        self.page.sign_in().click()
        assert self.modal.title().text == 'Login failed!'
        assert self.modal.text().text == 'Password field required.'

    @allure.id('TC_009')
    @allure.title(
        'Korábban regisztrált felhasznói fiókkal történő sikertelen bejelentkezés email cím mező üresen hagyása miatt.')
    def test_login_negative_email(self):
        self.page.password_input().send_keys('Piroska23')
        self.page.sign_in().click()
        assert self.modal.title().text == 'Login failed!'
        assert self.modal.text().text == 'Email field required.'

    @allure.id('TC_010')
    @allure.title('Korábban még nem regisztrált felhasznói fiókkal történő sikertelen bejelentkezés.')
    def test_login_negative_registered(self):
        self.page.email_input().send_keys('piros_cica24@gmail.com')
        self.page.password_input().send_keys('Piroska24')
        self.page.sign_in().click()
        assert self.modal.title().text == 'Login failed!'
        assert self.modal.text().text == 'Invalid user credentials.'

    @allure.id('TC_011')
    @allure.title('Korábban regisztrált felhasznói fiókkal történő sikertelen bejelentkezés hibás jelszó miatt.')
    def test_login_negative_wrong(self):
        self.page.email_input().send_keys('piros_cica23@gmail.com')
        self.page.password_input().send_keys('Piroska24')
        self.page.sign_in().click()
        assert self.modal.title().text == 'Login failed!'
        assert self.modal.text().text == 'Invalid user credentials.'

    @allure.id('TC_012')
    @allure.title('Korábban regisztrált felhasznói fiókkal történő sikeres bejelentkezés.')
    def test_login_positive(self):
        self.page.email_input().send_keys('piros_cica23@gmail.com')
        self.page.password_input().send_keys('Piroska23')
        self.page.sign_in().click()
        page = pom.ConduitHomePageWithLogin(self.page.driver)
        assert page.username_link().text == 'PirosCica23'


class TestLogout:

    def setup_method(self):
        driver = conf_driver.get_chrome_driver(remote=True)
        page = pom.ConduitSignInPage(driver=driver)
        page.open(url='http://localhost:1667/#/login')
        page.email_input().send_keys('piros_cica23@gmail.com')
        page.password_input().send_keys('Piroska23')
        page.sign_in().click()
        self.page = pom.ConduitHomePageWithLogin(driver)

    def teardown_method(self):
        self.page.close()

    @allure.id('TC_013')
    @allure.title('Korábban létrehozott felhasználóval történő bejelentkezés után sikeres kijelentkezés végrehajtása.')
    def test_logout_positive(self):
        self.page.log_out_link().click()
        self.page = pom.ConduitHomePageWithoutLogin(self.page.driver)
        assert self.page.sign_in_link().is_displayed()


class TestEditProfile:

    def setup_method(self):
        driver = conf_driver.get_chrome_driver(remote=True)
        page = pom.ConduitSignInPage(driver=driver)
        page.open(url='http://localhost:1667/#/login')
        page.email_input().send_keys('piros_cica23@gmail.com')
        page.password_input().send_keys('Piroska23')
        page.sign_in().click()
        page = pom.ConduitHomePageWithLogin(driver=driver)
        page.settings_link().click()
        self.page = pom.ConduitSettingsPage(driver=driver)
        self.page.title()
        self.modal = pom.ConduitGeneralModalWindow(driver=driver)

    def teardown_method(self):
        self.page.close()

    @allure.id('TC_014')
    @allure.title('Korábban regisztrált felhasználó fiók profilképének sikertelen megváltoztatatása' +
                  ' profilkép hivatkozásánaknem megadása miatt.')
    def test_profile_picture_negative(self):
        while len(self.page.profile_picture_input().get_attribute('value')) > 0:
            self.page.profile_picture_input().send_keys(Keys.BACKSPACE)
        self.page.update_settings().click()
        assert self.modal.title().text == 'Update failed!'
        assert self.modal.text().text == 'Image field required.'

    @allure.id('TC_015')
    @allure.title('Korábban regisztrált felhasználó fiók profilképének sikeres megváltoztatatása.')
    def test_profile_picture_positive(self):
        self.page.profile_picture_input().clear()
        self.page.profile_picture_input().send_keys('https://cdn-icons-png.flaticon.com/512/9327/9327067.png')
        self.page.update_settings().click()
        assert self.modal.title().text == 'Update successful!'
        self.modal.ok().click()
        page = pom.ConduitHomePageWithLogin(driver=self.page.driver)
        page.username_link().click()
        page = pom.ConduitProfilePage(driver=page.driver)
        assert page.profile_picture().get_attribute('src') == 'https://cdn-icons-png.flaticon.com/512/9327/9327067.png'

    @allure.id('TC_016')
    @allure.title(
        'Korábban regisztrált felhasználó felhasználónevévek sikertelen megváltoztatatása név nem megadása miatt.')
    def test_profile_username_negative(self):
        while len(self.page.username_input().get_attribute('value')) > 0:
            self.page.username_input().send_keys(Keys.BACKSPACE)
        self.page.update_settings().click()
        assert self.modal.title().text == 'Update failed!'
        assert self.modal.text().text == 'Username field required.'

    @allure.id('TC_017')
    @allure.title('Korábban regisztrált felhasználó felhasználónevének sikeres megváltoztatatása.')
    def test_profile_username_positive(self):
        self.page.username_input().clear()
        self.page.username_input().send_keys('VorosMacska23')
        self.page.update_settings().click()
        assert self.modal.title().text == 'Update successful!'
        self.modal.ok().click()
        page = pom.ConduitHomePageWithLogin(driver=self.page.driver)
        page.username_link().click()
        page = pom.ConduitProfilePage(driver=page.driver)
        assert page.profile_name().text == "VorosMacska23"

    @allure.id('TC_019')
    @allure.title('Korábban regisztrált felhasználó email címének sikertelen megváltoztatatása' +
                  'email cím mező üresen hagyása miatt.')
    def test_profile_email_negative_empty(self):
        while len(self.page.email_input().get_attribute('value')) > 0:
            self.page.email_input().send_keys(Keys.BACKSPACE)
        self.page.update_settings().click()
        assert self.modal.title().text == 'Update failed!'
        assert self.modal.text().text == 'Email field required.'

    @allure.id('TC_020')
    @allure.title(
        'Korábban regisztrált felhasználó email címének sikertelen megváltoztatatása már létező email cím miatt.')
    def test_profile_email_negative_exists(self):
        self.page.email_input().clear()
        self.page.email_input().send_keys('testuser1@example.com')
        self.page.update_settings().click()
        assert self.modal.title().text == 'Update failed!'
        assert self.modal.text().text == 'Email already taken.'

    @allure.id('TC_023')
    @allure.title('Korábban már regisztrált felhasználói fiók bemutatkozásának sikeres módosítása.')
    def test_profile_bio_positive(self):
        self.page.bio_textarea().clear()
        self.page.bio_textarea().send_keys('Szeretem a piros gombolyagokat.')
        self.page.update_settings().click()
        assert self.modal.title().text == 'Update successful!'
        self.modal.ok().click()
        page = pom.ConduitHomePageWithLogin(driver=self.page.driver)
        page.username_link().click()
        page = pom.ConduitProfilePage(driver=page.driver)
        assert page.profile_bio().text == "Szeretem a piros gombolyagokat."

    @allure.id('TC_022')
    @allure.title('Korábban regisztrált felhasználói fiók jelszavának sikeres megváltoztatása.')
    def test_profile_password_positive(self):
        self.page.password_input().send_keys('PirosCica23')
        self.page.update_settings().click()
        assert self.modal.title().text == 'Update successful!'
        self.modal.ok().click()
        page = pom.ConduitHomePageWithLogin(driver=self.page.driver)
        page.log_out_link().click()
        page = pom.ConduitHomePageWithoutLogin(self.page.driver)
        page.sign_in_link().click()
        page = pom.ConduitSignInPage(self.page.driver)
        page.email_input().send_keys('piros_cica23@gmail.com')
        page.password_input().send_keys('PirosCica23')
        page.sign_in().click()
        page = pom.ConduitHomePageWithLogin(self.page.driver)
        assert page.username_link().text == 'VorosMacska23'


class TestRepeatedInputFromSource:

    def setup_method(self):
        driver = conf_driver.get_chrome_driver(remote=True)
        self.registration = pom.ConduitSignUpPage(driver=driver)
        self.modal = pom.ConduitGeneralModalWindow(driver=driver)
        self.home_with_login = pom.ConduitHomePageWithLogin(driver=driver)
        self.home_without_login = pom.ConduitHomePageWithoutLogin(driver=driver)
        self.home_without_login.open(url='http://localhost:1667/#/')
        self.new_article = pom.ConduitNewArticle(driver=driver)
        self.article = pom.ConduitArticle(driver=driver)

    def teardown_method(self):
        self.registration.close()

    @allure.id('ATC_01')
    @allure.title('Sorozatos sikeres regisztráció user_data.csv fájlból')
    def test_register_positive(self):
        with open('./test/user_data.csv', mode='r') as user_data_csv:
            csv_reader = csv.DictReader(user_data_csv)
            for record in csv_reader:
                self.home_without_login.sign_up_link().click()
                self.registration.username_input().send_keys(record['username'])
                self.registration.email_input().send_keys(record['email'])
                self.registration.password_input().send_keys(record['password'])
                self.registration.sign_up().click()
                assert self.modal.title().text == 'Welcome!'
                assert self.modal.text().text == 'Your registration was successful!'
                self.modal.ok().click()
                assert self.home_with_login.username_link().text == record['username']
                self.home_with_login.log_out_link().click()

    @allure.id('ATC_02')
    @allure.title('Sorozatos sikeres cikk hozzáadása article_data.tsv fájlból')
    def test_new_article_positive(self):
        self.home_without_login.sign_in_link().click()
        page = pom.ConduitSignInPage(driver=self.modal.driver)
        page.email_input().send_keys('foltos_cica23@gmail.com')
        page.password_input().send_keys('FoltosCica23')
        page.sign_in().click()
        assert self.home_with_login.username_link().text == 'FoltosCica23'
        with open('./test/article_data.tsv', mode='r', encoding='utf-8-sig') as user_data_csv:
            csv_reader = csv.DictReader(user_data_csv, delimiter="\t")
            for record in csv_reader:
                self.home_with_login.new_article_link().click()
                self.new_article.title_input().send_keys(record['title'])
                self.new_article.about_input().send_keys(record['about'])
                self.new_article.article_textarea().send_keys(
                    f'# Napi idézet\n\n> {record["article"]}\n\n*{record["author"]}*')
                tags = record['tags'].split(',')
                for tag in tags:
                    self.new_article.tags_input().send_keys(tag)
                    self.new_article.tags_input().send_keys(Keys.ENTER)
                self.new_article.publish_article().click()
                assert self.article.title().text == record['title']
                for element, tag in zip(self.article.tag_list(), tags):
                    assert element.text == tag


class TestWriteAndDeleteArticle:

    def setup_method(self):
        driver = conf_driver.get_chrome_driver(remote=True)
        page = pom.ConduitSignInPage(driver=driver)
        page.open(url='http://localhost:1667/#/login')
        page.email_input().send_keys('piros_cica23@gmail.com')
        page.password_input().send_keys('PirosCica23')
        page.sign_in().click()
        self.page = pom.ConduitHomePageWithLogin(driver=driver)
        self.page.new_article_link().click()
        self.new_article = pom.ConduitNewArticle(driver=driver)
        self.article = pom.ConduitArticle(driver=driver)
        self.modal = pom.ConduitGeneralModalWindow(driver=driver)

    def teardown_method(self):
        self.page.close()

    @allure.id('TC_024')
    @allure.title('Korábban már regisztrált felhasználói fiókkal új cikk sikeres létrehozása.')
    def test_new_article_positive(self):
        self.new_article.title_input().send_keys('Te milyen cica vagy?')
        self.new_article.about_input().send_keys('Cicák fajtái')
        self.new_article.article_textarea().send_keys('# Típusok:\n\n- Rövid szőrű fajták\n- Félhosszú szőrű fajták\n' +
                                                      '- Hosszú szőrű fajták\n- Hibrid fajták\n\n' +
                                                      '**Írd meg kommentben a fentiek közül!**')
        tags = ['cica', 'kerdes', 'valasz']
        for tag in tags:
            self.new_article.tags_input().send_keys(tag)
            self.new_article.tags_input().send_keys(Keys.ENTER)
        self.new_article.publish_article().click()
        assert self.article.title().text == 'Te milyen cica vagy?'
        for element, tag in zip(self.article.tag_list(), tags):
            assert element.text == tag

    @allure.id('TC_025')
    @allure.title(
        'Korábban már regisztrált felhasználói fiókkal új cikk sikertelen létrehozása cikk címének hiánya miatt.')
    def test_new_article_negative(self):
        self.new_article.title_input().clear()
        self.new_article.about_input().send_keys('Cicák fajtái')
        self.new_article.article_textarea().send_keys('# Típusok:\n\n- Rövid szőrű fajták\n- Félhosszú szőrű fajták\n' +
                                                      '- Hosszú szőrű fajták\n- Hibrid fajták\n\n' +
                                                      '**Írd meg kommentben a fentiek közül!**')
        titles = ['cica', 'kerdes', 'valasz']
        for title in titles:
            self.new_article.tags_input().send_keys(title)
            self.new_article.tags_input().send_keys(Keys.ENTER)
        self.new_article.publish_article().click()
        assert self.modal.title().text == 'Oops!'

    @allure.id('TC_034')
    @allure.title('Korábban létrehozott cikk sikeres törlése.')
    def test_delete_article_positive(self):
        self.page.username_link().click()
        profile_page = pom.ConduitProfilePage(driver=self.page.driver)
        profile_page.profile_name()
        links = profile_page.preview_links()
        link = list(filter(lambda element: element.text == 'Te milyen cica vagy?', links))
        assert len(link) == 1
        link[0].click()
        self.article.delete_article().click()
        self.page.username_link().click()
        profile_page.profile_name()
        links = profile_page.preview_links()
        if len(links) > 0:
            link = list(filter(lambda element: element.text == 'Te milyen cica vagy?', links))
            assert len(link) == 0
        else:
            assert len(links) == 0


class TestListAndSaveData:
    def setup_method(self):
        driver = conf_driver.get_chrome_driver(remote=True)
        page = pom.ConduitSignInPage(driver=driver)
        page.open(url='http://localhost:1667/#/login')
        page.email_input().send_keys('foltos_cica23@gmail.com')
        page.password_input().send_keys('FoltosCica23')
        page.sign_in().click()
        self.page = pom.ConduitHomePageWithLogin(driver=driver)
        self.profile = pom.ConduitProfilePage(driver=driver)
        self.pagination = pom.ConduitGeneralPagination(driver=driver)
        self.page.username_link()

    def teardown_method(self):
        self.page.close()

    @allure.id('ATC_03')
    @allure.title('Népszerű címkék sikeres listázása címkefelhőből')
    def test_collect_tags_positive(self):
        links = self.page.popular_tags()
        assert len(links) > 0

    @allure.id('ATC_04')
    @allure.title('Felhasználó saját cikkjeinek sikeres bejárása')
    def test_collect_my_articles_positive(self):
        self.page.username_link().click()
        self.profile.profile_name()
        self.pagination.active_page_number()
        page_numbers = self.pagination.pagination_link()
        current_page = 0
        for page in page_numbers:
            page.click()
            current_page += 1
            assert self.pagination.active_page_number().text == str(current_page)
            articles_link = self.profile.preview_links()
            assert len(articles_link) > 0

    @allure.id('ATC_05')
    @allure.title('Globális hírfolyam cikk címeinek mentése saved_data.tsv fájlba')
    def test_save_global_feed_positive(self):
        self.pagination.active_page_number()
        page_numbers = self.pagination.pagination_link()
        assert len(page_numbers) > 0
        with open('./test/saved_data.tsv', mode='w', encoding='utf-8', newline='') as csv_file:
            fieldnames = ['oldalszam', 'cim']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter='\t')
            writer.writeheader()
            for page in page_numbers:
                page.click()
                oldalszam = self.pagination.active_page_number().text
                self.page.username_link()
                headers = self.page.articles_header()
                assert len(headers) > 0
                for header in headers:
                    writer.writerow({'oldalszam': oldalszam, 'cim': header.text})
