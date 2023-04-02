"""Configuration Chrome webdriver for Selenium

This module helps the testing process by configuring Selenium Chrome webdriver separately.

Todo:
    [x] Creating a configuration that works locally
    [ ] Creating a configuration that works on the GitHub Actions remote machine
"""

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def get_chrome_driver() -> Chrome:
    """Function that performs the configuration

    It currently only makes Chrome webdriver that works locally.

    Returns:
        Chrome: configurated Selenium Chrome webdriver
    """
    options = Options()
    options.add_experimental_option('detach', True)
    return Chrome(service=Service(executable_path=ChromeDriverManager().install()), options=options)
