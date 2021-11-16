import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import logging

class TestUI:

    @pytest.mark.parametrize("login_input,password_input",[("standard_user","secret_sauce"),("gs@gmail.com","secret_sauce")])
    def test_login(self,login_input,password_input):
        
        s=Service("C:/Users/GS-3294/Documents/chromedriver_win32 (1)/chromedriver.exe")
        self.driver=webdriver.Chrome(service=s)
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.ID,value="user-name").send_keys(login_input)
        self.driver.find_element(By.ID,value="password").send_keys(password_input)
        self.driver.find_element(By.XPATH,value="//*[@id='login-button']").click()
        
        time.sleep(3)
        self.driver.close()
        
    

 