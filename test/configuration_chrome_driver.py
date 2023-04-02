"""Configuration Chrome webdriver for Selenium

This module helps the testing process by configuring Selenium Chrome webdriver separately.

Todo:
    [x] Creating a configuration that works locally
    [x] Creating a configuration that works on the GitHub Actions remote machine
"""

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def get_chrome_driver() -> Chrome:
    """Function that performs the configuration

    It currently makes Chrome webdriver twith speciel arguments.

    Returns:
        Chrome: configurated Selenium Chrome webdriver
    """
    options = Options()
    options.add_experimental_option('detach', True)
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    return Chrome(service=Service(executable_path=ChromeDriverManager().install()), options=options)
