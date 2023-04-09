"""Page Object Model for Conduit testing project

This module contains the objects that represent the fronted of Conduit.

Todo:
    [x] General page object model
    [ ] Conduit home page model
        [ ] Without login
        [ ] With login
    [X] General modal window model
    [x] Conduit sign in page model
    [x] Conduit sign up page model
    [x] Conduit settings page model
    [ ] Conduit new article page model
    [ ] Conduit profil page model
    [ ] Conduit article page model
    ...
"""

from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class GeneralPage:
    """General Page Object for Page Object Model

    Simple model for testing process.

    Arguments:
        driver (Chrome):Selenium Chrome webdriver

    Attributes:
        driver (Chrome): Selenium Chrome webdriver
        driverWait (WebDriverWait): Selenium Chrome webdriver wait
        url (str): URL
    """
    driver: Chrome
    driverWait: WebDriverWait

    def __init__(self, driver: Chrome):
        self.driver = driver
        self.driverWait = WebDriverWait(driver=driver, timeout=5)

    def open(self, url: str) -> None:
        """Open URL with driver.get method

        Arguments:
        url (str): URL
        """
        self.driver.get(url)
        self.driver.maximize_window()

    def close(self) -> None:
        """Close with driver.close method"""
        self.driver.close()

    def refresh(self) -> None:
        """Refresh with driver.refresh method"""
        self.driver.refresh()


class ConduitHomePageWithoutLogin(GeneralPage):
    """Conduit home page (without login) modell

    Conduit home page (without login) model from general page model.

    Arguments:
        driver (Chrome): Selenium Chrome webdriver
    """

    def __init__(self, driver: Chrome):
        super().__init__(driver=driver)

    def sign_in_link(self) -> WebElement:
        """Get sing in link from Conduit home page

        Returns:
             WebElement: sign in link
        """
        return self.driverWait.until(expected_conditions.element_to_be_clickable(
            (By.XPATH, '//li[@class="nav-item"]/a[contains(text(), "Sign in")]')))

    def sign_up_link(self) -> WebElement:
        """Get sing up link from Conduit home page

        Returns:
            WebElement: sign up link
        """
        return self.driverWait.until(expected_conditions.element_to_be_clickable(
            (By.XPATH, '//li[@class="nav-item"]/a[contains(text(), "Sign up")]')))

    def accept_cookie(self, in_list=False) -> WebElement | list[WebElement]:
        """Get accept cookie button from Conduit home page.

        The list format is useful when the existence of the element is also important for the test case.

        Arguments:
            in_list(bool): if True return to list format

        Returns:
            WebElement | list[WebElement]: accept cookie button in a list
        """
        return self.driver.find_elements(By.CLASS_NAME,
                                         'cookie__bar__buttons__button--accept') if in_list else self.driver.find_element(
            By.CLASS_NAME, 'cookie__bar__buttons__button--accept')


class ConduitHomePageWithLogin(GeneralPage):
    """Conduit home page (with login) modell

    Conduit home page (with login) model from general page model.

    Arguments:
        driver (Chrome): Selenium Chrome webdriver
    """

    def __init__(self, driver: Chrome):
        super().__init__(driver=driver)

    def username_link(self) -> WebElement:
        """Get username link from Conduit home page

        Returns:
            WebElement: username link
        """

        return self.driverWait.until(expected_conditions.element_to_be_clickable(
            (By.XPATH, '//li[@class="nav-item"]/a[contains(@href, "#/@")]')))

    def log_out_link(self) -> WebElement:
        """Get log out link from Conduit home page

        Returns:
            WebElement: log out link
        """
        return self.driverWait.until(expected_conditions.element_to_be_clickable(
            (By.XPATH, '//li[@class="nav-item"]/a[contains(text(), "Log out")]')))

    def settings_link(self) -> WebElement:
        """Get settings link from Conduit home page

        Returns:
            WebElement: log out link
        """
        return self.driverWait.until(expected_conditions.element_to_be_clickable(
            (By.XPATH, '//li[@class="nav-item"]/a[contains(text(), "Settings")]')))


class ConduitSignInPage(GeneralPage):
    """Conduit sign in page model

    Conduit sign in page model from general page model.

    Arguments:
        driver (Chrome): Selenium Chrome webdriver
    """

    def __init__(self, driver: Chrome):
        super().__init__(driver=driver)

    def email_input(self) -> WebElement:
        """Get email input from Conduit sign in page

        Returns:
            WebElement: email input
        """
        return self.driver.find_element(By.XPATH, '//input[contains(@placeholder,"Email")]')

    def password_input(self) -> WebElement:
        """Get password input from Conduit sign in page

        Returns:
            WebElement: password input
        """
        return self.driver.find_element(By.XPATH, '//input[contains(@placeholder,"Password")]')

    def sign_in(self) -> WebElement:
        """Get sign in button from Conduit sign in page

        Returns:
            WebElement: sign in button
        """
        return self.driver.find_element(By.XPATH, '//button[contains(text(), "Sign in")]')


class ConduitGeneralModalWindow(GeneralPage):
    """Conduit general modal window model

        Conduit general modal window model from general page model for pop up messages.

        Arguments:
            driver (Chrome): Selenium Chrome webdriver
    """

    def __init__(self, driver: Chrome):
        super().__init__(driver=driver)

    def title(self) -> WebElement:
        """Get title from Conduit modal pop up

        Returns:
            WebElement: modal title
        """
        return self.driverWait.until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'swal-title')))

    def text(self) -> WebElement:
        """Get text from Conduit modal pop up

        Returns:
            WebElement: modal text
        """
        return self.driverWait.until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'swal-text')))

    def ok(self) -> WebElement:
        """Get ok button from Conduit modal pop up

        Returns:
            WebElement: ok button
        """
        return self.driverWait.until(
            expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'swal-button')))


class ConduitSignUpPage(GeneralPage):
    """Conduit sign up page modell

    Conduit sign up page model from general page model.

    Arguments:
        driver (Chrome): Selenium Chrome webdriver
    """

    def __init__(self, driver: Chrome):
        super().__init__(driver=driver)

    def username_input(self) -> WebElement:
        """Get username input from Conduit sign up page

        Returns:
            WebElement: email input
        """
        return self.driver.find_element(By.XPATH, '//input[contains(@placeholder,"Username")]')

    def email_input(self) -> WebElement:
        """Get email input from Conduit sign up page

        Returns:
            WebElement: email input
        """
        return self.driver.find_element(By.XPATH, '//input[contains(@placeholder,"Email")]')

    def password_input(self) -> WebElement:
        """Get password input from Conduit sign up page

        Returns:
            WebElement: password input
        """
        return self.driver.find_element(By.XPATH, '//input[contains(@placeholder,"Password")]')

    def sign_up(self) -> WebElement:
        """Get sign up button from Conduit sign up page

        Returns:
            WebElement: sign in button
        """
        return self.driver.find_element(By.XPATH, '//button[contains(text(), "Sign up")]')


class ConduitSettingsPage(GeneralPage):
    """Conduit settings page model

        Conduit settings page model from general page model.

        Arguments:
            driver (Chrome): Selenium Chrome webdriver
    """

    def __init__(self, driver: Chrome):
        super().__init__(driver=driver)

    def title(self):
        """Get title from Conduit home page
        Use for waiting loaded page

        Returns:
            WebElement: title
        """
        return self.driverWait.until(expected_conditions.element_to_be_clickable(
            (By.XPATH, '//h1[contains(text(), "Settings")]')))

    def profile_picture_input(self) -> WebElement:
        """Get profil picture input from Conduit settings page

        Returns:
            WebElement: profile picture input
        """
        return self.driver.find_element(By.XPATH, '//input[@type="text"][contains(@placeholder, "profile picture")]')

    def username_input(self) -> WebElement:
        """Get username input from Conduit settings page

        Returns:
            WebElement: username input
        """
        return self.driver.find_element(By.XPATH, '//input[@type="text"][contains(@placeholder, "username")]')

    def bio_textarea(self) -> WebElement:
        """Get bio textarea from Conduit settings page

        Returns:
            WebElement: textarea input
        """
        return self.driver.find_element(By.XPATH, '//textarea[contains(@placeholder, "bio")]')

    def email_input(self) -> WebElement:
        """Get email input from Conduit settings page

        Returns:
            WebElement: email input
        """
        return self.driver.find_element(By.XPATH, '//input[@type="text"][contains(@placeholder, "Email")]')

    def password_input(self) -> WebElement:
        """Get password input from Conduit settings page

        Returns:
            WebElement: password input
        """
        return self.driver.find_element(By.XPATH, '//input[@type="password"][contains(@placeholder, "Password")]')

    def update_settings(self) -> WebElement:
        """Get update settings button from Conduit sign up page

        Returns:
            WebElement: update settings button
        """
        return self.driver.find_element(By.XPATH, '//button[contains(text(), "Update Settings")]')


class ConduitProfilePage(GeneralPage):
    """Conduit profile page model

    Conduit profile page model from general page model.

    Arguments:
        driver (Chrome): Selenium Chrome webdriver
        """

    def __init__(self, driver: Chrome):
        super().__init__(driver=driver)

    def profile_picture(self):
        """Get profil picture img from Conduit home page

        Returns:
            WebElement: profile picture img
        """
        return self.driverWait.until(expected_conditions.element_to_be_clickable(
            (By.CLASS_NAME, 'user-img')))

    def profile_name(self):
        """Get profil name header from Conduit home page

        Returns:
            WebElement: profile name header
        """
        return self.driverWait.until(expected_conditions.element_to_be_clickable(
            (By.XPATH, '//*[@class="user-info"]//h4')))
    def profile_bio(self):
        """Get profile bio paragraph from Conduit home page

        Returns:
            WebElement: profile bio paragraph
        """
        return self.driverWait.until(expected_conditions.element_to_be_clickable(
            (By.XPATH, '//*[@class="user-info"]//p')))
