from selenium import webdriver
from selenium.webdriver.common.by import By


class dealerLogin:
    button_dealer_xpath = "//button[text()=' Dealer ']"
    textBox_userID_id = 'signInName'
    textBox_password_id = 'password'
    button_SignIn_id = "//button[text()='Sign in']"

    def __init__(self, driver):
        self.driver = driver

    def clickDealerButton(self):
        self.driver.find_element(By.XPATH, self.button_dealer_xpath).click()

    def enterDealerUsername(self, username):
        self.driver.find_element(By.ID, self.textBox_userID_id).send_keys(username)

    def enterDealerPassword(self, password):
        self.driver.find_element(By.ID, self.textBox_password_id).send_keys(password)

    def clickSingIn(self):
        self.driver.find_element(By.XPATH, self.button_SignIn_id).click()
