import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver=webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://telranedu.web.app/home")

    yield driver

    driver.quit()


