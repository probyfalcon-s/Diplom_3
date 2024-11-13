from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
import pytest

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        chrome_service = ChromeService(executable_path="path/to/chromedriver")
        driver = webdriver.Chrome(service=chrome_service)
    elif request.param == "firefox":
        firefox_service = FirefoxService(executable_path="path/to/geckodriver")
        driver = webdriver.Firefox(service=firefox_service)
    yield driver
    driver.quit()


