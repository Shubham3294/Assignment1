import pytest
from selenium import webdriver 
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("login_input,password_input",[("standard_user","secret_sauce")])
def test_login(login_input,password_input):
    driver=webdriver.Chrome(executable_path="C:/Users/GS-3294/Documents/chromedriver_win32 (1)/chromedriver.exe")
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.find_element(By.ID,value="user-name").send_keys(login_input)
    driver.find_element(By.ID,value="password").send_keys(password_input)
    
    driver.find_element(By.ID,value="login-button").click()
    

 