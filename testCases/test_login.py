import pytest
from selenium import webdriver
from pageElement.loginPage import Login
import time


class Test_login:
    SaucedemoUrl= "https://www.saucedemo.com/"
    parameterList=[("standard_user","secret_sauce"),("locked_out_user","secret_sauce"),
                    ("gs@gmail.com","secret_sauce"),("problem_user","secret_sauce")]
                    
    @pytest.mark.parametrize("login_input,password_input",parameterList)
    def test_login(self,setup,login_input,password_input):
        self.driver=setup
        self.driver.get(self.SaucedemoUrl)
        self.driver.maximize_window()
        self.loginPage=Login(self.driver)
        
        self.loginPage.setusername(login_input)
        self.loginPage.setpassword(password_input)
        self.loginPage.clickLogin()
        time.sleep(3)   
        current_url= self.driver.current_url
        self.driver.close()

        assert current_url == "https://www.saucedemo.com/inventory.html"
        
        

