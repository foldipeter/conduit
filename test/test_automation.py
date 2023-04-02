import page_object_model as pom
import configuration_chrome_driver as conf_driver
import allure


class TestSignUpPage:

    def setup_method(self):
        self.page = pom.ConduitSignUpPage(conf_driver.get_chrome_driver(remote=True))
        self.page.open()

    def teardown_method(self):
        self.page.close()

    @allure.id('TC001')
    @allure.title('Új felhasználó fiók sikertelen létrehozása hiányos felhasználónév megadásával.')
    def test_register_negative_username(self):
        self.page.email_input().send_keys('piros_cica23@gmail.com')
        self.page.password_input().send_keys('Piroska23')
        self.page.sign_up().click()
        assert self.page.modal_title().text == 'Registration failed!'
        assert self.page.modal_text().text == 'Username field required.'

    @allure.id('TC002')
    @allure.title('Új felhasználó fiók sikertelen létrehozása hiányos email cím megadásával.')
    def test_register_negative_email(self):
        self.page.username_input().send_keys('PirosCica23')
        self.page.password_input().send_keys('Piroska23')
        self.page.sign_up().click()
        assert self.page.modal_title().text == 'Registration failed!'
        assert self.page.modal_text().text == 'Email field required.'

    @allure.id('TC003')
    @allure.title('Új felhasználó fiók sikertelen létrehozása hiányos jelszó megadásával.')
    def test_register_negative_password(self):
        self.page.username_input().send_keys('PirosCica23')
        self.page.email_input().send_keys('piros_cica23@gmail.com')
        self.page.sign_up().click()
        assert self.page.modal_title().text == 'Registration failed!'
        assert self.page.modal_text().text == 'Password field required.'

    @allure.id('TC004')
    @allure.title('Új felhasználó fiók sikeres létrehozása megfelelő adatok megadásával.')
    def test_register_positive(self):
        self.page.username_input().send_keys('PirosCica23')
        self.page.email_input().send_keys('piros_cica23@gmail.com')
        self.page.password_input().send_keys('Piroska23')
        self.page.sign_up().click()
        assert self.page.modal_title().text == 'Welcome!'
        assert self.page.modal_text().text == 'Your registration was successful!'
        self.page.modal_ok().click()
        self.page = pom.ConduitHomePage(self.page.driver)
        assert self.page.username_link().text == 'PirosCica23'

    @allure.id('TC005')
    @allure.title('Új felhasználó fiók sikertelen létrehozása már regisztrált email cím megadásával.')
    def test_register_negative_exists(self):
        self.page.username_input().send_keys('PirosCica23')
        self.page.email_input().send_keys('piros_cica23@gmail.com')
        self.page.password_input().send_keys('Piroska23')
        self.page.sign_up().click()
        assert self.page.modal_title().text == 'Registration failed!'
        assert self.page.modal_text().text == 'Email already taken.'


class TestHomePage:

    def setup_method(self):
        self.page = pom.ConduitHomePage(conf_driver.get_chrome_driver(remote=True))
        self.page.open()

    def teardown_method(self):
        self.page.close()

    @allure.id('TC006')
    @allure.title('Adatkezelési tájékoztató sikeres elfogadása.')
    def test_accept_cookie(self):
        self.page.accept_cookie().click()
        assert len(self.page.accept_cookie(in_list=True)) == 0


class TestSignInPage:
    def setup_method(self):
        self.page = pom.ConduitSignInPage(conf_driver.get_chrome_driver(remote=True))
        self.page.open()

    def teardown_method(self):
        self.page.close()

    @allure.id('TC007')
    @allure.title('Korábban regisztrált felhasznói fiókkal történő sikertelen bejelentkezés jelszó mező üresen hagyása miatt.')
    def test_login_negative_password(self):
        self.page.email_input().send_keys('piros_cica23@gmail.com')
        self.page.sign_in().click()
        assert self.page.modal_title().text == 'Login failed!'
        assert self.page.modal_text().text == 'Password field required.'

    @allure.id('TC008')
    @allure.title('Korábban regisztrált felhasznói fiókkal történő sikertelen bejelentkezés email cím mező üresen hagyása miatt.')
    def test_login_negative_email(self):
        self.page.password_input().send_keys('Piroska23')
        self.page.sign_in().click()
        assert self.page.modal_title().text == 'Login failed!'
        assert self.page.modal_text().text == 'Email field required.'

    @allure.id('TC009')
    @allure.title('Korábban még nem regisztrált felhasznói fiókkal történő sikertelen bejelentkezés.')
    def test_login_negative_registered(self):
        self.page.email_input().send_keys('piros_cica24@gmail.com')
        self.page.password_input().send_keys('Piroska24')
        self.page.sign_in().click()
        assert self.page.modal_title().text == 'Login failed!'
        assert self.page.modal_text().text == 'Invalid user credentials.'

    @allure.id('TC010')
    @allure.title('Korábban regisztrált felhasznói fiókkal történő sikertelen bejelentkezés hibás jelszó miatt.')
    def test_login_negative_wrong(self):
        self.page.email_input().send_keys('piros_cica23@gmail.com')
        self.page.password_input().send_keys('Piroska24')
        self.page.sign_in().click()
        assert self.page.modal_title().text == 'Login failed!'
        assert self.page.modal_text().text == 'Invalid user credentials.'

    @allure.id('TC011')
    @allure.title('Korábban regisztrált felhasznói fiókkal történő sikeres bejelentkezés.')
    def test_login_positive(self):
        self.page.email_input().send_keys('piros_cica23@gmail.com')
        self.page.password_input().send_keys('Piroska23')
        self.page.sign_in().click()
        self.page = pom.ConduitHomePage(self.page.driver)
        assert self.page.username_link().text == 'PirosCica23'
