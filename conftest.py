import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver=webdriver.Chrome()
    driver.get("https://telranedu.web.app/home")

    yield driver

    driver.quit()


