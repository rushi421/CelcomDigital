import time

import pytest
from selenium import webdriver
from pageObjects.loginPageDealer import dealerLogin
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getDealerURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logInfo = LogGen.loggen()

    @pytest.mark.lalitha
    def test_homePageTitle(self, setup):
        self.logInfo.info("****************Test case has been started***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == 'Celcom':
            assert True
        else:
            assert False

    @pytest.mark.parametrize("username, password",
                             [("ENT01", "Powa5841"),
                              ("ENT02", "Duda7822"),
                              ("ENT03", "Mekq2575"),
                              ("ENT04", "Soxu4057")])
    def test_Login(self, setup, username, password):
        self.logInfo.info("****************Test case has been started***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.DL = dealerLogin(self.driver)
        self.DL.clickDealerButton()
        self.DL.enterDealerUsername(username)
        self.DL.enterDealerPassword(password)
        time.sleep(1)
        self.DL.clickSingIn()
