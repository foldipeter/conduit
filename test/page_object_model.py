"""Page Object Model for Conduit testing project

This module contains the objects that represent the fronted of Conduit.

Todo:
    [X] General page object model
        [X] open
        [X] close
        [X] refresh
        [X] find_element
        [X] find_elements
        [X] fill_input_element
        [X] clear_input_element
    [X] Conduit home page model
        [X] get_accept_cookie_button
        [X] click_accept_cookie_button
        [X] get_popular_tag_links
        [X] click_popular_tag_link
        [X] get_global_feed_link
        [X] click_global_feed_link
        [X] Without login
            [X] get_sign_in_link
            [X] click_sign_in_link
            [X] get_sign_up_link
            [X] click_sign_up_link
        [X] With login
            [X] get_username_link
            [X] click_username_link
            [X] get_log_out_link
            [X] click_log_out_link
            [X] get_settings_link
            [X] click_settings_link
            [X] get_new_article_link
            [X] click_new_article_link
            [X] get_your_feed_link
            [X] click_your_feed_link
    [x] Conduit sign in page model
        [X] get_email_input
        [X] fill_email_input
        [X] get_password_input
        [X] fill_password_input
        [X] get_sign_in_button
        [X] click_sign_in_button
        [X] sign_in
    [x] Conduit sign up page model
        [X] get_username_input
        [X] fill_username_input
        [X] get_email_input
        [X] fill_email_input
        [X] get_password_input
        [X] fill_password_input
        [X] get_sign_up_button
        [X] click_sign_up_button
        [X] sign_up
    [X] General modal window model
        [X] get_title_div
        [X] get_text_div
        [X] get_ok_button
        [X] click_ok_button
    [x] Conduit settings page model
        [X] get_title_header
        [X] get_profile_picture_input
        [X] fill_profile_picture_input
        [X] get_username_input
        [X] fill_username_input
        [X] get_bio_textarea
        [X] fill_bio_textarea
        [X] get_email_input
        [X] fill_email_input
        [X] get_password_input
        [X] fill_password_input
        [X] get_update_settings_button
        [X] click_update_settings_button
        [X] update_settings
    [ ] Conduit profile page model
        [X] get_profile_picture_img
        [X] get_profile_name_header
        [X] get_profile_bio_paragraph
        [ ] ... my articles, favorite articles
    [X] Conduit new article page model
        [X] get_title_input
        [X] fill_title_input
        [X] get_about_input
        [X] fill_about_input
        [X] get_article_textarea
        [X] fill_article_textarea
        [X] get_tags_input
        [X] add_tags
        [X] get_publish_article_button
        [X] click_publish_article_button
        [X] new_article
    [ ] Conduit article page model
        [X] get_title_header
        [X] get_author_link
        [X] get_date_element
        [X] get_edit_article_link
        [X] click_edit_article_link
        [X] get_delete_article_button
        [X] click_delete_article_button
        [X] get_tag_list
        [X] get_article_div
        [ ] ... comment stuff, follow, favorite etc...
    [ ] General pagination
        [X] get_active_page_number_link
        [X] get_pagination_link
        [X] get_pagination_links
        [X] click_pagination_link
        [X] click_next_pagination_link
    [ ] General feed
        [X] articles_header
        [X] get_last_article_header
        [X] get_specific_article_header
        [X] click_specific_article_header
        [ ] ... username, date, tags, read more, about, favorite
    [ ] etc more model...
"""

from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


class GeneralPage:
    """General page object for page object model extend user interaction

    Model for testing process.

    Arguments:
        driver_source ({'driver': Chrome}): Object what contains Selenium Chrome webdriver

    Attributes:
        driver (Chrome): Selenium Chrome webdriver
    """

    def __init__(self, driver_source: {'driver': Chrome}):
        self.driver = driver_source.driver

    def find_element(self, by: str, value: str, timeout=10) -> WebElement | None:
        """Find element with waiting

        Arguments:
            by (str): By.ID
            value (str): selector
            timeout (int): time out in seconds default is 10s

        Returns:
            WebElement | None: element or None if not found
        """
        try:
            return WebDriverWait(driver=self.driver, timeout=timeout).until(
                expected_conditions.element_to_be_clickable((by, value)))
        except TimeoutException:
            return None

    def find_elements(self, by: str, value: str, timeout=10) -> list[WebElement]:
        """Find elements with waiting

        Arguments:
            by (str): By.ID
            value (str): selector
            timeout (int): time out in seconds default is 10s

        Returns:
            list[WebElement]: elements in list if element not found return empty list
        """
        try:
            return WebDriverWait(driver=self.driver, timeout=timeout).until(
                lambda driver: driver.find_elements(by, value))
        except TimeoutException:
            return []

    def open(self, url: str) -> None:
        """Open URL with driver get method

        Arguments:
        url (str): URL
        """
        self.driver.get(url)
        self.driver.maximize_window()

    def refresh(self) -> None:
        """Refresh with driver refresh method"""
        self.driver.refresh()

    def close(self) -> None:
        """Close with driver close method"""
        self.driver.close()

    @staticmethod
    def fill_input_element(element: WebElement, value: str) -> None:
        """Fill the input element with given value

        If len of value zero this method clears the input element value with simulate backspace key press

        Arguments:
            element (WebElement): the input element
            value (str): given text

        Returns:
            None
        """

        if len(value) == 0:
            GeneralPage.clear_input_element(element=element)
        else:
            element.click()
            element.clear()
            element.send_keys(value)

    @staticmethod
    def clear_input_element(element: WebElement) -> None:
        """Clear the input element value with simulate backspace key press

        Arguments:
            element (WebElement): input element

        Returns:
            None
        """

        while len(element.get_attribute('value')) > 0:
            element.send_keys(Keys.BACKSPACE)


class ConduitHomePage(GeneralPage):
    """Page object model for Conduit home page

    Conduit home page general model

    Arguments:
        driver_source ({'driver': Chrome}): Object what contains Selenium Chrome webdriver
    """

    def __init__(self, driver_source: {'driver': Chrome}):
        super().__init__(driver_source=driver_source)

    def get_accept_cookie_button(self) -> WebElement | None:
        """Get accept cookie button from Conduit home page.

        If button doesn't exist return None.

        Returns:
            WebElement | None: accept cookie button
        """

        return self.find_element(By.CLASS_NAME, 'cookie__bar__buttons__button--accept')

    def click_accept_cookie_button(self) -> None:
        """Click accept cookie button on Conduit home page.

        Returns:
            None
        """

        self.get_accept_cookie_button().click()

    def get_popular_tag_links(self) -> list[WebElement]:
        """Get popular tag links from Conduit home page

        Returns:
            list[WebElement]: popular tag links in list
        """

        return self.find_elements(By.XPATH, '//*[@class="sidebar"]//*[@class="tag-list"]/a')

    def click_popular_tag_link(self, tag_name: str) -> None:
        """Click the given popular tag link from Conduit home page

        Arguments:
            tag_name (str): tag name

        Returns:
            None
        """

        next(tag_link for tag_link in self.get_popular_tag_links() if tag_link.text == tag_name).click()

    def get_global_feed_link(self) -> WebElement | None:
        """Get global feed link from Conduit home page.

        If link doesn't exist return None.

        Returns:
            WebElement | None: global feed link
        """

        return self.find_element(By.CLASS_NAME, '//li[@class="nav-item"]/a[contains(text(), "Global Feed")]')

    def click_global_feed_link(self) -> None:
        """Click global feed link on Conduit home page.

        Returns:
            None
        """

        self.get_global_feed_link().click()


class ConduitHomePageWithoutLogin(ConduitHomePage):
    """Page object model for Conduit home page before login

    Conduit home page before login

    Arguments:
        driver_source ({'driver': Chrome}): Object what contains Selenium Chrome webdriver
    """

    def __init__(self, driver_source: {'driver': Chrome}):
        super().__init__(driver_source=driver_source)

    def get_sign_in_link(self) -> WebElement | None:
        """Get sing in link from Conduit home page

        If link doesn't exist return None.

        Returns:
             WebElement | None: sign in link
        """

        return self.find_element(By.XPATH, '//li[@class="nav-item"]/a[contains(text(), "Sign in")]')

    def click_sign_in_link(self) -> None:
        """Click sing in link on Conduit home page

        Returns:
             None
        """

        self.get_sign_in_link().click()

    def get_sign_up_link(self) -> WebElement | None:
        """Get sing up link from Conduit home page

        If link doesn't exist return None.

        Returns:
            WebElement | None: sign up link
        """

        return self.find_element(By.XPATH, '//li[@class="nav-item"]/a[contains(text(), "Sign up")]')

    def click_sign_up_link(self) -> None:
        """Click sing up link on Conduit home page

        Returns:
             None
        """

        self.get_sign_up_link().click()


class ConduitHomePageWithLogin(ConduitHomePage):
    """Page object model for Conduit home page after login

    Conduit home page after login

    Arguments:
        driver_source ({'driver': Chrome}): Object what contains Selenium Chrome webdriver
    """

    def __init__(self, driver_source: {'driver': Chrome}):
        super().__init__(driver_source=driver_source)

    def get_username_link(self) -> WebElement | None:
        """Get username link from Conduit home page

        If link doesn't exist return None.

        Returns:
            WebElement | None: username link
        """

        return self.find_element(By.XPATH, '//li[@class="nav-item"]/a[contains(@href, "#/@")]')

    def click_username_link(self) -> None:
        """Click username link on Conduit home page

        Returns:
             None
        """

        self.get_username_link().click()

    def get_log_out_link(self) -> WebElement | None:
        """Get log out link from Conduit home page

        If link doesn't exist return None.

        Returns:
            WebElement | None: log out link
        """

        return self.find_element(By.XPATH, '//li[@class="nav-item"]/a[contains(text(), "Log out")]')

    def click_log_out_link(self) -> None:
        """Click log out link on Conduit home page

        Returns:
            None
        """

        self.get_log_out_link().click()

    def get_settings_link(self) -> WebElement | None:
        """Get settings link from Conduit home page

        If link doesn't exist return None.

        Returns:
            WebElement | None: settings link
        """

        return self.find_element(By.XPATH, '//li[@class="nav-item"]/a[contains(text(), "Settings")]')

    def click_settings_link(self) -> None:
        """Click settings link on Conduit home page

        Returns:
            None
        """

        self.get_settings_link().click()

    def get_new_article_link(self) -> WebElement | None:
        """Get new article link from Conduit home page

        If link doesn't exist return None.

        Returns:
            WebElement | None: new article link
        """

        return self.find_element(By.XPATH, '//li[@class="nav-item"]/a[contains(text(), "New Article")]')

    def click_new_article_link(self) -> None:
        """Click new article link on Conduit home page

        Returns:
            None
        """

        self.get_new_article_link().click()

    def get_your_feed_link(self) -> WebElement | None:
        """Get your feed link from Conduit home page.

        If link doesn't exist return None.

        Returns:
            WebElement | None: your feed link
        """

        return self.find_element(By.CLASS_NAME, '//li[@class="nav-item"]/a[contains(text(), "Your Feed")]')

    def click_your_feed_link(self) -> None:
        """Click your feed link on Conduit home page.

        Returns:
            None
        """

        self.get_your_feed_link().click()


class ConduitSignInPage(GeneralPage):
    """Conduit sign in page model

    Conduit sign in page model from general page model.

    Arguments:
        driver_source ({'driver': Chrome}): Object what contains Selenium Chrome webdriver
    """

    def __init__(self, driver_source: {'driver': Chrome}):
        super().__init__(driver_source=driver_source)

    def get_email_input(self) -> WebElement | None:
        """Get email input from Conduit sign in page

        If doesn't exist return None.

        Returns:
            WebElement | None: email input
        """

        return self.find_element(By.XPATH, '//input[contains(@placeholder,"Email")]')

    def fill_email_input(self, email: str) -> None:
        """Fill email input on Conduit sign in page with the given email

        Returns:
            None
        """

        GeneralPage.fill_input_element(element=self.get_email_input(), value=email)

    def get_password_input(self) -> WebElement | None:
        """Get password input from Conduit sign in page

        If it doesn't exist return None.

        Returns:
            WebElement | None: password input
        """

        return self.find_element(By.XPATH, '//input[contains(@placeholder,"Password")]')

    def fill_password_input(self, password: str) -> None:
        """Fill password input on Conduit sign in page with given password

        Returns:
            None
        """

        GeneralPage.fill_input_element(element=self.get_password_input(), value=password)

    def get_sign_in_button(self) -> WebElement | None:
        """Get sign in button from Conduit sign in page

        If it doesn't exist return None.

        Returns:
            WebElement | None: sign in button
        """
        return self.find_element(By.XPATH, '//button[contains(text(), "Sign in")]')

    def click_sign_in_button(self) -> None:
        """Click sign in button on Conduit sign in page

        Returns:
            None
        """

        self.get_sign_in_button().click()

    def sign_in(self, data: {'email': str, 'password': str}) -> None:
        """Modeling sign in process with given email and password

        Arguments:
            data ({'email': str, 'password': str}): email and password

        Returns:
            None
        """

        if 'email' in data:
            self.fill_email_input(email=data['email'])
        if 'password' in data:
            self.fill_password_input(password=data['password'])
        self.click_sign_in_button()


class ConduitGeneralModalWindow(GeneralPage):
    """Conduit general modal window model

    Conduit general modal window model from general page model for pop up messages.

    Arguments:
        driver_source ({'driver': Chrome}): Object what contains Selenium Chrome webdriver
    """

    def __init__(self, driver_source: {'driver': Chrome}):
        super().__init__(driver_source=driver_source)

    def get_title_div(self) -> WebElement | None:
        """Get title from Conduit modal pop up

        If it doesn't exist return None.

        Returns:
            WebElement | None: modal title div
        """

        return self.find_element(By.CLASS_NAME, 'swal-title')

    def get_text_div(self) -> WebElement | None:
        """Get text from Conduit modal pop up

        Returns:
            WebElement | None: modal text div
        """

        return self.find_element(By.CLASS_NAME, 'swal-text')

    def get_ok_button(self) -> WebElement | None:
        """Get ok button from Conduit modal pop up

        If it doesn't exist return None.

        Returns:
            WebElement | None: ok button
        """

        return self.find_element(By.CLASS_NAME, 'swal-button')

    def click_ok_button(self) -> None:
        """Click ok button on Conduit modal pop up

        Returns:
            None
        """

        self.get_ok_button().click()


class ConduitSignUpPage(GeneralPage):
    """Conduit sign up page model

    Conduit sign up page model from general page model.

    Arguments:
        driver_source ({'driver': Chrome}): Object what contains Selenium Chrome webdriver
    """

    def __init__(self, driver_source: {'driver': Chrome}):
        super().__init__(driver_source=driver_source)

    def get_username_input(self) -> WebElement | None:
        """Get username input from Conduit sign up page

        If it doesn't exist return None.

        Returns:
            WebElement | None: email input
        """

        return self.find_element(By.XPATH, '//input[contains(@placeholder,"Username")]')

    def fill_username_input(self, username: str) -> None:
        """Fill username input on Conduit sign up page with given username

        Arguments:
            username (str): username

        Returns:
            WebElement | None: email input
        """

        GeneralPage.fill_input_element(element=self.get_username_input(), value=username)

    def get_email_input(self) -> WebElement | None:
        """Get email input from Conduit sign up page

        If it doesn't exist return None.

        Returns:
            WebElement: email input
        """

        return self.find_element(By.XPATH, '//input[contains(@placeholder,"Email")]')

    def fill_email_input(self, email: str) -> None:
        """Fill email input on Conduit sign up page

        Arguments:
            email (str): given email

        Returns:
            None
        """

        GeneralPage.fill_input_element(element=self.get_email_input(), value=email)

    def get_password_input(self) -> WebElement | None:
        """Get password input from Conduit sign up page

        If it doesn't exist return None.

        Returns:
            WebElement | None: password input
        """

        return self.find_element(By.XPATH, '//input[contains(@placeholder,"Password")]')

    def fill_password_input(self, password: str) -> None:
        """Fill password input on Conduit sign up page

        Arguments:
            password (str): given password

        Returns:
            None
        """

        GeneralPage.fill_input_element(element=self.get_password_input(), value=password)

    def get_sign_up_button(self) -> WebElement | None:
        """Get sign up button from Conduit sign up page

        If it doesn't exist return None.

        Returns:
            WebElement | None: sign in button
        """

        return self.find_element(By.XPATH, '//button[contains(text(), "Sign up")]')

    def click_sign_up_button(self) -> None:
        """Click sign up button on Conduit sign up page

        Returns:
            None
        """

        self.get_sign_up_button().click()

    def sign_up(self, data: {'username': str, 'email': str, 'password': str}):
        """Modeling sign in process with given email and password

            Arguments:
                data (data:{'username': str, 'email': str, 'password': str}): username, email, password

            Returns:
                None
        """

        if 'username' in data:
            self.fill_username_input(data['username'])
        if 'email' in data:
            self.fill_email_input(data['email'])
        if 'password' in data:
            self.fill_password_input(data['password'])
        self.click_sign_up_button()


class ConduitSettingsPage(GeneralPage):
    """Conduit settings page model

    Conduit settings page model from general page model.

    Arguments:
        driver_source ({'driver': Chrome}): Object what contains Selenium Chrome webdriver
    """

    def __init__(self, driver_source: {'driver': Chrome}):
        super().__init__(driver_source=driver_source)

    def get_title_header(self) -> WebElement | None:
        """Get title header from Conduit home page

        If it doesn't exist return None.

        Returns:
            WebElement | None: title
        """

        return self.find_element(By.XPATH, '//h1[contains(text(), "Settings")]')

    def get_profile_picture_input(self) -> WebElement | None:
        """Get profile picture input from Conduit settings page

        If it doesn't exist return None.

        Returns:
            WebElement | None: profile picture input
        """

        return self.find_element(By.XPATH, '//input[@type="text"][contains(@placeholder, "profile picture")]')

    def fill_profile_picture_input(self, url: str) -> None:
        """Fill profile picture input on Conduit settings page with given url

        Arguments:
            url (str): given url of profile picture

        Returns:
            None
        """

        GeneralPage.fill_input_element(element=self.get_profile_picture_input(), value=url)

    def get_username_input(self) -> WebElement | None:
        """Get username input from Conduit settings page

        If it doesn't exist return None.

        Returns:
            WebElement | None: username input
        """

        return self.find_element(By.XPATH, '//input[@type="text"][contains(@placeholder, "username")]')

    def fill_username_input(self, username: str) -> None:
        """Fill username input on Conduit settings page with given username

        Arguments:
            username (str): given username

        Returns:
            None
        """

        GeneralPage.fill_input_element(element=self.get_username_input(), value=username)

    def get_bio_textarea(self) -> WebElement | None:
        """Get bio textarea from Conduit settings page

        If it doesn't exist return None.

        Returns:
            WebElement | None: textarea input
        """

        return self.find_element(By.XPATH, '//textarea[contains(@placeholder, "bio")]')

    def fill_bio_textarea(self, bio: str) -> None:
        """Fill bio textarea from Conduit settings page

        Arguments:
            bio (str): profile bio

        Returns:
            None
        """

        GeneralPage.fill_input_element(element=self.get_bio_textarea(), value=bio)

    def get_email_input(self) -> WebElement | None:
        """Get email input from Conduit settings page

        If it doesn't exist return None.

        Returns:
            WebElement | None: email input
        """

        return self.find_element(By.XPATH, '//input[@type="text"][contains(@placeholder, "Email")]')

    def fill_email_input(self, email: str) -> None:
        """Fill email input on Conduit settings page

        Arguments:
            email (str): given email

        Returns:
            None
        """

        GeneralPage.fill_input_element(element=self.get_email_input(), value=email)

    def get_password_input(self) -> WebElement | None:
        """Get password input from Conduit settings page

        If it doesn't exist return None.

        Returns:
            WebElement | None: password input
        """

        return self.find_element(By.XPATH, '//input[@type="password"][contains(@placeholder, "Password")]')

    def fill_password_input(self, password: str) -> None:
        """FIll password input on Conduit settings page

        Parameters:
            password (str): given password

        Returns:
            None
        """

        GeneralPage.fill_input_element(element=self.get_password_input(), value=password)

    def get_update_settings_button(self) -> WebElement | None:
        """Get update settings button from Conduit settings page

        If it doesn't exist return None.

        Returns:
            WebElement | None: update settings button
        """
        return self.find_element(By.XPATH, '//button[contains(text(), "Update Settings")]')

    def click_update_settings_button(self) -> None:
        """Click update settings button on Conduit settings page

        Returns:
            None
        """

        self.get_update_settings_button().click()

    def update_settings(self, data: {'profile_picture': str, 'username': str, 'bio': str, 'email': str,
                                     'password': str}) -> None:
        """Modeling update settings process with given datas

        Arguments:
            data ({'profile_picture': str, 'username': str, 'bio': str, 'email': str,
                                     'password': str}): user data to be changed

        Returns:
            None
        """

        if 'profile_picture' in data:
            self.fill_profile_picture_input(url=data['profile_picture'])
        if 'username' in data:
            self.fill_username_input(username=data['username'])
        if 'bio' in data:
            self.fill_bio_textarea(bio=data['bio'])
        if 'email' in data:
            self.fill_email_input(email=data['email'])
        if 'password' in data:
            self.fill_password_input(password=data['password'])
        self.click_update_settings_button()


class ConduitGeneralPagination(GeneralPage):
    """Conduit general pagination page model

    Conduit general pagination page model from general page model.

    Arguments:
        driver_source ({'driver': Chrome}): Object what contains Selenium Chrome webdriver
    """

    def __init__(self, driver_source: {'driver': Chrome}):
        super().__init__(driver_source=driver_source)

    def get_active_page_number_link(self) -> WebElement | None:
        """Get active page number link from Conduit general pagination

        If it doesn't exist return None.

        Returns:
            WebElement | None: active page number link
        """

        return self.find_element(By.XPATH, '//li[@class="page-item active"]/a')

    def get_pagination_links(self) -> list[WebElement]:
        """Get pagination links from Conduit general pagination in list

        Returns:
            list[WebElement]: pagination links in list
        """

        return self.find_elements(By.CLASS_NAME, 'page-link')

    def get_pagination_link(self, page_number: int | str) -> WebElement | None:
        """Get pagination link what contain the given page number from Conduit page.

        If it doesn't exist return None.

        Attributes:
            page_number (int | str): the given page number

        Returns:
            WebElement | None: pagination links in list
        """

        return self.find_element(By.XPATH, f'//a[@class="page-link"][contains(text(), "{page_number}")]')

    def click_pagination_link(self, page_number: int | str) -> None:
        """Click pagination link what contain the given page number on Conduit page

        Arguments:
            page_number (str | int): page number

        Returns:
            None
        """

        self.get_pagination_link(page_number=page_number).click()

    def click_next_pagination_link(self) -> bool:
        """Click the next pagination link on Conduit page

        If there is a next link return True, if there isn't next link then return False.

        Returns:
            bool: Has next link?
        """

        current_page_number = int(self.get_active_page_number_link().text)
        next_pagination_link = self.get_pagination_link(page_number=current_page_number + 1)
        if next_pagination_link is not None:
            next_pagination_link.click()
        else:
            return False
        return True


class ConduitNewArticle(GeneralPage):
    """Conduit new article page model

    Conduit new article page model from general page model.

    Arguments:
        driver_source ({'driver': Chrome}): Object what contains Selenium Chrome webdriver
    """

    def __init__(self, driver_source: {'driver': Chrome}):
        super().__init__(driver_source=driver_source)

    def get_title_input(self) -> WebElement | None:
        """Get article title input from Conduit new article page

        If it doesn't exist return None.

        Returns:
            WebElement | None: article title input
        """

        return self.find_element(By.XPATH, '//input[@type="text"][contains(@placeholder, "Article Title")]')

    def fill_title_input(self, title: str) -> None:
        """Fill article title input on Conduit new article page

        Arguments:
            title (str): article title

        Returns:
            None
        """

        GeneralPage.fill_input_element(element=self.get_title_input(), value=title)

    def get_about_input(self) -> WebElement | None:
        """Get article about input from Conduit new article page

        If it doesn't exist return None.

        Returns:
            WebElement | None: article about input
        """

        return self.find_element(By.XPATH, '//input[@type="text"][contains(@placeholder, "article about")]')

    def fill_about_input(self, about: str) -> None:
        """Get article about input on Conduit new article page

        Arguments::
           about (str): article about

        Returns:
            None
        """

        GeneralPage.fill_input_element(element=self.get_about_input(), value=about)

    def get_article_textarea(self) -> WebElement | None:
        """Get article textarea from Conduit new article page

        If it doesn't exist return None.

        Returns:
            WebElement | None: article textarea input
        """

        return self.find_element(By.XPATH, '//textarea[contains(@placeholder, "Write your article")]')

    def fill_article_textarea(self, article: str) -> None:
        """Get article textarea on Conduit new article page

        Arguments:
            article (str): article body in markdown

        Returns:
            None
        """

        GeneralPage.fill_input_element(element=self.get_article_textarea(), value=article)

    def get_tags_input(self) -> WebElement | None:
        """Get article tags input from Conduit new article page

        If it doesn't exist return None.

        Returns:
            WebElement | None: article tags input
        """

        return self.find_element(By.XPATH, '//input[@type="text"][contains(@placeholder, "Enter tags")]')

    def add_tags(self, tags: str) -> None:
        """Add article tag or tags on Conduit new article page

        Arguments:
            tags (str): tag or tags separated by coma

        Returns:
            None
        """

        tag_list = tags.split(',')
        input_element = self.get_tags_input()
        for tag in tag_list:
            input_element.send_keys(tag)
            input_element.send_keys(Keys.ENTER)

    def get_publish_article_button(self) -> WebElement | None:
        """Get update publish article button from Conduit new article page

        If it doesn't exist return None.

        Returns:
            WebElement | None: publish article button
        """

        return self.find_element(By.XPATH, '//button[contains(text(), "Publish Article")]')

    def click_publish_article_button(self) -> None:
        """Click update publish article button on Conduit new article page

        Returns:
            None
        """

        self.get_publish_article_button().click()

    def new_article(self, data: {'title': str, 'about': str, 'article': str, 'tags': str}) -> None:
        """Modeling update settings process with given datas

        Arguments:
            data ({'title': str, 'about': str, 'article': str, 'tags': str}): represented a new article,
                                                                              tags is coma separated

        Returns:
            None
        """

        if 'title' in data:
            GeneralPage.fill_input_element(element=self.get_title_input(), value=data['title'])
        if 'about' in data:
            GeneralPage.fill_input_element(element=self.get_about_input(), value=data['about'])
        if 'article' in data:
            GeneralPage.fill_input_element(element=self.get_article_textarea(), value=data['article'])
        if 'tags' in data:
            self.add_tags(tags=data['tags'])
        self.click_publish_article_button()


class ConduitArticle(GeneralPage):
    """Conduit article page model

    Conduit article page model from general page model.

    Arguments:
        driver_source ({'driver': Chrome}): Object what contains Selenium Chrome webdriver
    """

    def __init__(self, driver_source: {'driver': Chrome}):
        super().__init__(driver_source=driver_source)

    def get_title_header(self) -> WebElement | None:
        """Get article title header from Conduit article page

        If it doesn't exist return None.

        Returns:
            WebElement | None: article title header
        """

        return self.find_element(By.XPATH, '//*[@class="banner"]//h1')

    def get_author_link(self) -> WebElement | None:
        """Get article author link from Conduit article page

        If it doesn't exist return None.

        Returns:
            WebElement | None: article author link
        """

        return self.find_element(By.XPATH, '//*[@class="info"]//a[@class="author"]')

    def get_date_element(self) -> WebElement | None:
        """Get article date element from Conduit article page

        If it doesn't exist return None.

        Returns:
            WebElement | None: article date
        """

        return self.find_element(By.XPATH, '//*[@class="info"]//*[@class="date"]')

    def get_edit_article_link(self) -> WebElement | None:
        """Get edit article link from Conduit article page

        If it doesn't exist return None.

        Returns:
            WebElement | None: edit article
        """

        return self.find_element(By.XPATH, '//a//*[contains(text(), "Edit Article")]')

    def click_edit_article_link(self) -> None:
        """Click edit article link on Conduit article page

        Returns:
            None
        """

        self.get_edit_article_link().click()

    def get_delete_article_button(self) -> WebElement | None:
        """Get delete article button from Conduit article page

        If it doesn't exist return None.

        Returns:
            WebElement | None: delete article button
        """

        return self.find_element(By.XPATH, '//button//*[contains(text(), "Delete Article")]')

    def click_delete_article(self) -> None:
        """Click delete article on Conduit article page

        Returns:
            None
        """

        self.get_delete_article_button().click()

    def get_tag_list(self) -> list[WebElement]:
        """Get tag list from Conduit article page

        Returns:
            list[WebElement]: tag list
        """

        return self.find_elements(By.XPATH, '//*[@class="tag-list"]/*')

    def get_article_div(self) -> WebElement | None:
        """Get article div from Conduit article page

        If it doesn't exist return None.

        Returns:
            WebElement | None: article container div
        """

        return self.find_element(By.XPATH, '//*[@class="tag-list"]/parent::div/div[not(contains(@class, "tag"))]')


class ConduitProfilePage(GeneralPage):
    """Conduit profile page model

    Conduit profile page model from general page model.

    Arguments:
        driver_source ({'driver': Chrome}): Object what contains Selenium Chrome webdriver
    """

    def __init__(self, driver_source: {'driver': Chrome}):
        super().__init__(driver_source=driver_source)

    def get_profile_picture_img(self) -> WebElement | None:
        """Get profile picture img from Conduit profile page

        If it doesn't exist return None.

        Returns:
            WebElement | None: profile picture img
        """

        return self.find_element(By.CLASS_NAME, 'user-img')

    def get_profile_name_header(self) -> WebElement | None:
        """Get profile name header from Conduit profile page

        If it doesn't exist return None.

        Returns:
            WebElement | None: profile name header
        """

        return self.find_element(By.XPATH, '//*[@class="user-info"]//h4')

    def get_profile_bio_paragraph(self) -> WebElement | None:
        """Get profile bio paragraph from Conduit profile page

        Returns:
            WebElement | None: profile bio paragraph
        """

        return self.find_element(By.XPATH, '//*[@class="user-info"]//p')


class ConduitGeneralFeed(GeneralPage):
    """Conduit general feed page model

    Conduit general feed page from general page model.

    Arguments:
        driver_source ({'driver': Chrome}): Object what contains Selenium Chrome webdriver
    """

    def __init__(self, driver_source: {'driver': Chrome}):
        super().__init__(driver_source=driver_source)

    def get_articles_header(self) -> list[WebElement]:
        """Get articles header from Conduit page

        Returns:
            list[WebElement]: articles header in list
        """

        return self.find_elements(By.XPATH, '//*[@class="article-preview"]//h1')

    def get_last_article_header(self) -> WebElement | None:
        """Get last article header from Conduit page

        Returns:
            WebElement | None: last articles header
        """

        return self.find_element(By.XPATH, '//*[@class="article-preview"][last()]//h1')

    def get_specific_article_header(self, text: str) -> WebElement | None:
        """Get the first specific article header witch contains the given text from Conduit page

        Arguments:
            text (str): text what must be contained the header

        Returns:
            WebElement | None: he first specific article header witch contains the given text
        """

        return self.find_element(By.XPATH, f'//*[@class="article-preview"]//h1[contains(text(),"{text}")]')

    def click_specific_article_header(self, text: str) -> None:
        """Click the first specific article header witch contains the given text on Conduit page

        Arguments:
            text (str): text what must be contained the header

        Returns:
            None
        """

        self.get_specific_article_header(text=text).click()
