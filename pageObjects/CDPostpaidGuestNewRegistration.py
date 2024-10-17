import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import pyautogui


class PostPaidNewRegistration:
    button_CDPBuyNow160_xpath = "(//button[text()=' Buy Now '])[2]"
    rdButton_newNumber_xpath = "//span[text()='New Number']"
    textBox_IDNumber_xpath = "//input[@placeholder='888888888888']"
    button_submit_xpath = "//button[text()=' Submit ']"
    button_selectNumber_xpath = "(//div[@class='number-card ng-star-inserted'])[1]"
    button_checkOut_xpath = "//button[text()=' Check Out ']"
    button_uploadID_xpath = "(//button[text()='Upload'])[1]"
    # button_uploadSelfie_xpath = "(//button[text()='Upload'])[2]"
    button_uploadIDSelfiePopUp_xpath = "//span[text()='Upload Now']"
    button_UploadEmailSave_xpath = "//button[text()=' Save ']"
    textBox_fullName_xpath = "(//input[contains(@class, 'mat-input-element')])[1]"
    textBox_Line1_xpath = "(//input[contains(@class, 'mat-input-element')])[3]"
    textBox_Line2_xpath = "(//input[contains(@class, 'mat-input-element')])[4]"
    textBox_postCode_xpath = "(//input[contains(@class, 'mat-input-element')])[6]"
    textBox_city_xpath = "(//input[contains(@class, 'mat-input-element')])[7]"
    dropDown_state_xpath = "(//span[contains(@class, 'mat-select-placeholder')])[1]"
    button_yourIDDetailsYes_xpath = "//button[text()=' Yes ']"
    textBox_email_xpath = "//input[@inputmode='email']"
    textBox_DLine1_xpath = "(//input[contains(@class, 'mat-input-element')])[1]"
    textBox_Dline2_xpath = "(//input[contains(@class, 'mat-input-element')])[2]"
    textBox_DPostCode_xpath = "(//input[contains(@class, 'mat-input-element')])[4]"
    textBox_DCity_xpath = "(//input[contains(@class, 'mat-input-element')])[5]"
    textBox_mobileNumber_xpath = "(//input[contains(@class, 'mat-input-element')])[6]"
    button_deliveryAddressSave_xpath = "//button[text()='Save']"
    checkBox_IAgree_xpath = "//strong[contains(.,'I agree to')]"
    button_PayNow_xpath = "//button[text()=' Pay Now ']"

    def __init__(self, driver):
        self.driver = driver

    def clickBuyNow160Button(self):
        element = self.driver.find_element(By.XPATH, self.button_CDPBuyNow160_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView()", element)  # By Location the element
        element.send_keys(Keys.PAGE_DOWN)
        element.send_keys(Keys.PAGE_DOWN)
        self.driver.find_element(By.XPATH, self.button_CDPBuyNow160_xpath).click()

    def clickRadioButton(self):
        self.driver.find_element(By.XPATH, self.rdButton_newNumber_xpath).click()

    def enterIDNumber(self, idnumber):
        self.driver.find_element(By.XPATH, self.textBox_IDNumber_xpath).send_keys(idnumber)

    def clickSubmitButton(self):
        element = self.driver.find_element(By.XPATH, self.button_submit_xpath)
        element.send_keys(Keys.PAGE_DOWN)
        element.send_keys(Keys.PAGE_DOWN)
        element.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.button_submit_xpath).click()

    def clickSelectNumber(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.button_selectNumber_xpath).click()

    def clickCheckOutButton(self):
        element = self.driver.find_element(By.XPATH, self.button_checkOut_xpath)
        element.send_keys(Keys.PAGE_DOWN)
        element.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.button_checkOut_xpath).click()

    def clickUploadButton(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.button_uploadID_xpath).click()

    def clickPopupUploadButton1(self):
        time.sleep(2)
        elementpresent = EC.presence_of_element_located((By.XPATH, self.button_uploadIDSelfiePopUp_xpath))
        WebDriverWait(self.driver, 10).until(elementpresent).click()
        time.sleep(3)
        pyautogui.write(r"C:\Users\Hello\PycharmProjects\CelcomDigital\TestData\Img1.png")
        pyautogui.press('enter') 

    """def clickUploadSelfieButton(self):
        time.sleep(4)
        self.driver.find_element(By.XPATH, self.button_uploadSelfie_xpath).click()"""

    def clickPopupUploadButton2(self):
        elementpresent = EC.presence_of_element_located((By.XPATH, self.button_uploadIDSelfiePopUp_xpath))
        WebDriverWait(self.driver, 10).until(elementpresent).click()
        time.sleep(3)
        pyautogui.write(r"C:\Users\Hello\PycharmProjects\CelcomDigital\TestData\Img2.png")
        pyautogui.press('enter')

    def clickSaveButton(self):
        self.driver.find_element(By.XPATH, self.button_UploadEmailSave_xpath).click()

    def enterFullName(self, fullname):
        self.driver.find_element(By.XPATH, self.textBox_fullName_xpath).clear()
        self.driver.find_element(By.XPATH, self.textBox_fullName_xpath).send_keys(fullname)

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

    def selectStateValue(self):
        self.driver.find_element(By.XPATH, self.dropDown_state_xpath)

    def clickYouIDDetailsYes(self):
        self.driver.find_element(By.XPATH, self.button_yourIDDetailsYes_xpath).click()

    def enterEmailID(self, email):
        self.driver.find_element(By.XPATH, self.textBox_email_xpath).send_keys(email)

    def enterDLine1(self, dline1):
        self.driver.find_element(By.XPATH, self.textBox_DLine1_xpath).send_keys(dline1)

    def enterDLine2(self, dline2):
        self.driver.find_element(By.XPATH, self.textBox_Dline2_xpath).send_keys(dline2)

    def enterDPostcode(self, dpostcode):
        self.driver.find_element(By.XPATH, self.textBox_DPostCode_xpath).send_keys(dpostcode)

    def enterDCity(self, dcity):
        self.driver.find_element(By.XPATH, self.textBox_DCity_xpath).send_keys(dcity)

    def enterMobileNumber(self, mobilenumber):
        self.driver.find_element(By.XPATH, self.textBox_mobileNumber_xpath).send_keys(mobilenumber)

    def clickDSaveButton(self):
        self.driver.find_element(By.XPATH, self.button_deliveryAddressSave_xpath).click()

    def clickIAgreeCheckBox(self):
        self.driver.find_element(By.XPATH, self.checkBox_IAgree_xpath).click()

    def clickPayNow(self):
        self.driver.find_element(By.XPATH, self.button_PayNow_xpath).click()
