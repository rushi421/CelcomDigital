from selenium.webdriver.common.by import By


class PostPaidExistingNewRegistration:
    toggle_ExistingCelComSubscriber_xpath = "//span[@class='toggle']"

    def __init__(self, driver):
        self.driver = driver

    def clickToggleButton(self):
        self.driver.find_element(By.XPATH, self.toggle_ExistingCelComSubscriber_xpath).click()
