"""Page Object Model for Conduit testing project

This module contains the objects that represent the fronted of Conduit.

Todo:
    [ ] Completing this list
    [x] General page object model
    [x] Conduit home page model
    [x] Conduit sign in page model
    [x] Conduit sign up page model
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
        url (str): URL

    Attributes:
        driver (Chrome): Selenium Chrome webdriver
        driverWait (WebDriverWait): Selenium Chrome webdriver wait
        url (str): URL
    """
    driver: Chrome
    driverWait: WebDriverWait
    url: str

    def __init__(self, driver: Chrome, url: str):
        self.driver = driver
        self.driverWait = WebDriverWait(driver=driver, timeout=5)
        self.url = url

    def open(self) -> None:
        """Open URL with driver.get method"""
        self.driver.get(self.url)
        self.driver.maximize_window()

    def close(self) -> None:
        """Close with driver.close method"""
        self.driver.close()

    def refresh(self) -> None:
        """Refresh with driver.refresh method"""
        self.driver.refresh()


class ConduitHomePage(GeneralPage):
    """Conduit home page modell

    Conduit home page model from general page model.

    Arguments:
        driver (Chrome): Selenium Chrome webdriver
    """

    def __init__(self, driver: Chrome):
        super().__init__(driver=driver, url='http://localhost:1667/#/')

    def sign_in_link(self) -> WebElement:
        """Get sing in link from Conduit home page

        Returns:
             WebElement: sign in link
        """
        return self.driver.find_element(By.XPATH, '//li[@class="nav-item"]/a[contains(text(), "Sign in")]')

    def sign_up_link(self) -> WebElement:
        """Get sing up link from Conduit home page

        Returns:
            WebElement: sign up link
        """
        return self.driver.find_element(By.XPATH, '//li[@class="nav-item"]/a[contains(text(), "Sign up")]')

    def accept_cookie(self, in_list=False) -> list[WebElement] | WebElement:
        """Get accept cookie button from Conduit home page.

        The list format is useful when the existence of the element is also important for the test case.

        Arguments:
            in_list(bool): if True return to list format

        Returns:
            list[WebElement] | WebElement: accept cookie button in a list
        """
        return self.driver.find_elements(By.CLASS_NAME,
                                         'cookie__bar__buttons__button--accept') if in_list else self.driver.find_element(
            By.CLASS_NAME, 'cookie__bar__buttons__button--accept')


class ConduitSignInPage(GeneralPage):
    """Conduit sign in page model

    Conduit sign in page model from general page model.

    Arguments:
        driver (Chrome): Selenium Chrome webdriver
    """

    def __init__(self, driver: Chrome):
        super().__init__(driver=driver, url='http://localhost:1667/#/login')

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

    def modal_title(self) -> WebElement:
        """Get title from Conduit sign in page modal pop up

        Returns:
            WebElement: modal title
        """
        return self.driverWait.until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'swal-title')))

    def modal_text(self) -> WebElement:
        """Get text from Conduit sign in page modal pop up

        Returns:
            WebElement: modal text
        """
        return self.driverWait.until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'swal-text')))

    def modal_ok(self) -> WebElement:
        """Get ok button from Conduit sign in page modal pop up

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
        super().__init__(driver=driver, url='http://localhost:1667/#/register')

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

    def modal_title(self) -> WebElement:
        """Get title from Conduit sign up page modal pop up

        Returns:
            WebElement: modal title
        """
        return self.driverWait.until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'swal-title')))

    def modal_text(self) -> WebElement:
        """Get text from Conduit sign up page modal pop up

        Returns:
            WebElement: modal text
        """
        return self.driverWait.until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'swal-text')))

    def modal_ok(self) -> WebElement:
        """Get ok button from Conduit sign up page modal pop up

        Returns:
            WebElement: ok button
        """
        return self.driverWait.until(
            expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'swal-button')))
