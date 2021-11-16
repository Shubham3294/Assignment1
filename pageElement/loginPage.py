from selenium.webdriver.common.by import By
class Login:
    username_id="user-name"
    password_id="password"
    loginbutton_xpath="//*[@id='login-button']"

    def __init__(self,driver):
        self.driver=driver

    def setusername(self,username):
        self.driver.find_element(By.ID,value=self.username_id).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element(By.ID,value=self.password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,value=self.loginbutton_xpath).click()