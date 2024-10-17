from selenium import webdriver
from selenium.webdriver.common.by import By


class agentLogin:
    button_teleSales_xpath = "//button[text()=' Telesales ']"
    textBox_userID_id = 'i0116'
    button_Next_id = "idSIButton9"
    textBox_password_id = 'i0118'
    button_SignIn_id = "//input[@value='Sign in']"
    button_Yes_id = "idSIButton9"

    def __init__(self, driver):
        self.driver = driver

    def clickTeleSalesButton(self):
        self.driver.find_element(By.XPATH, self.button_teleSales_xpath).click()

    def enterAgentUsername(self, username):
        self.driver.find_element(By.ID, self.textBox_userID_id).send_keys(username)

    def clickOnNextButton(self):
        self.driver.find_element(By.ID, self.button_Next_id).click()
    def enterAgentPassword(self, password):
        self.driver.find_element(By.ID, self.textBox_password_id).send_keys(password)

    def clickSingIn(self):
        self.driver.find_element(By.XPATH, self.button_SignIn_id).click()

    def clickYesButton(self):
        self.driver.find_element(By.ID, self.button_Yes_id).click()
