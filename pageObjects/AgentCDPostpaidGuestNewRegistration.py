import time

import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AgentPostPaidNewRegistration:
    button_PostPaidPlansBuy_xpath = "(//button[text()=' Buy '])[3]"
    ddClick_SelectPlan_xpath = "(//div[contains(@class, 'mat-select-arrow-wrapper')])[1]"
    ddValue_CDPostPaidPlans_xpath = "//span[text()='CelcomDigi Postpaid Plans']"
    ddClick_SelectPlanOption_xpath = "(//div[contains(@class, 'mat-select-trigger')])[2]"
    ddValue_plan_xpath = "//span[text()='CelcomDigi Postpaid 5G 160']"
    button_Next_xpath = "//button[contains(.,'Next')]"
    textBox_Line1_xpath = "(//input[contains(@class, 'mat-input-element')])[1]"
    textBox_Line2_xpath = "(//input[contains(@class, 'mat-input-element')])[2]"
    textBox_postCode_xpath = "(//input[contains(@class, 'mat-input-element')])[4]"
    textBox_city_xpath = "(//input[contains(@class, 'mat-input-element')])[5]"
    button_Submit_xpath = "//button[text()=' Submit ']"

    def __init__(self, driver):
        self.driver = driver

    def clickBuyButton(self):
        self.driver.find_element(By.XPATH, self.button_PostPaidPlansBuy_xpath).click()

    """def clickSelectPlanDropDown(self):
        self.driver.find_element(By.XPATH, self.ddClick_SelectPlan_xpath).click()
        time.sleep(5)
        element = self.driver.find_element(By.XPATH, self.ddClick_SelectPlan_xpath)
        element.send_keys(Keys.PAGE_DOWN)"""

    def selectCDPostPaidPlan(self):
        self.driver.find_element(By.XPATH, self.ddValue_CDPostPaidPlans_xpath).click()
        pyautogui.press('enter')
        time.sleep(2)

    def clickPlanOptionDropDown(self):
        self.driver.find_element(By.XPATH, self.ddClick_SelectPlanOption_xpath).click()

    def selectPlanValue(self):
        self.driver.find_element(By.XPATH, self.ddValue_plan_xpath).click()
        pyautogui.press('enter')

    def clickNextButton(self):
        parent = self.driver.current_window_handle
        print('parent window is:', parent)
        self.driver.find_element(By.XPATH, self.button_Next_xpath).click()
        child = self.driver.window_handles
        print('All Windows:', child)
        for tab in child:
            print(tab)
            if parent != tab:
                self.driver.switch_to.window(tab)
                self.driver.execute_script("window.scrollTo(0, 2000)", "")
                self.driver.find_element(By.XPATH, "//span[text()='New Number']").click()

    def enterLine1(self, line1):
        self.driver.find_element(By.XPATH, self.textBox_Line1_xpath).clear()
        self.driver.find_element(By.XPATH, self.textBox_Line1_xpath).send_keys(line1)

    def enterLine2(self, line2):
        self.driver.find_element(By.XPATH, self.textBox_Line2_xpath).clear()
        self.driver.find_element(By.XPATH, self.textBox_Line2_xpath).send_keys(line2)

    def enterPostcode(self, postcode):
        self.driver.find_element(By.XPATH, self.textBox_postCode_xpath).clear()
        self.driver.find_element(By.XPATH, self.textBox_postCode_xpath).send_keys(postcode)

    def enterCity(self, city):
        self.driver.find_element(By.XPATH, self.textBox_city_xpath).clear()
        self.driver.find_element(By.XPATH, self.textBox_city_xpath).send_keys(city)

    def clickSubmitButton(self):
        self.driver.find_element(By.XPATH, self.button_Submit_xpath).clear()
