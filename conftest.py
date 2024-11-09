import pytest
from selenium import webdriver

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome(executable_path="path/to/chromedriver")
    elif request.param == "firefox":
        driver = webdriver.Firefox(executable_path="path/to/geckodriver")
    driver.get(BASE_URL)
    yield driver
    driver.quit()


