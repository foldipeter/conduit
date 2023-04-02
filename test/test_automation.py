import page_object_model as pom
import configuration_chrome_driver as conf_driver
import allure


class TestSignUpPage:

    def setup_method(self):
        self.page = pom.ConduitSignUpPage(conf_driver.get_chrome_driver())
        self.page.open()

    def teardown_method(self):
        self.page.close()

    @allure.id('TC1')
    @allure.title('Új felhasználó fiók sikertelen létrehozása hiányos felhasználónév megadásával.')
    def test_register_negative_username(self):
        self.page.email_input().send_keys('piros_cica23@gmail.com')
        self.page.password_input().send_keys('Piroska23')
        self.page.sign_up().click()
        assert self.page.modal_title().text == 'Registration failed!'
        assert self.page.modal_text().text == 'Username field required.'

    @allure.id('TC2')
    @allure.title('Új felhasználó fiók sikertelen létrehozása hiányos email cím megadásával.')
    def test_register_negative_email(self):
        self.page.username_input().send_keys('PirosCica23')
        self.page.password_input().send_keys('Piroska23')
        self.page.sign_up().click()
        assert self.page.modal_title().text == 'Registration failed!'
        assert self.page.modal_text().text == 'Email field required.'

    @allure.id('TC3')
    @allure.title('Új felhasználó fiók sikertelen létrehozása hiányos jelszó megadásával.')
    def test_register_negative_password(self):
        self.page.username_input().send_keys('PirosCica23')
        self.page.email_input().send_keys('piros_cica23@gmail.com')
        self.page.sign_up().click()
        assert self.page.modal_title().text == 'Registration failed!'
        assert self.page.modal_text().text == 'Password field required.'

    @allure.id('TC4')
    @allure.title('Új felhasználó fiók sikeres létrehozása megfelelő adatok megadásával.')
    def test_register_positive(self):
        self.page.username_input().send_keys('PirosCica23')
        self.page.email_input().send_keys('piros_cica23@gmail.com')
        self.page.password_input().send_keys('Piroska23')
        self.page.sign_up().click()
        assert self.page.modal_title().text == 'Welcome!'
        assert self.page.modal_text().text == 'Your registration was successful!'