from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

@pytest.fixture
def setup():
    s=Service("C:/Users/GS-3294/Documents/chromedriver_win32 (1)/chromedriver.exe")
    driver=webdriver.Chrome(service=s)
    return driver