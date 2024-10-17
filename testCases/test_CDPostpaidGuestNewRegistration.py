import time

import pytest

from pageObjects.CDPostpaidGuestNewRegistration import PostPaidNewRegistration
from Utilities.readProperties import ReadConfig


class Test_NewRegistration:
    appURL = ReadConfig.getMassURL()
    idNumber = ReadConfig.getIDNumber()
    fullName = ReadConfig.getFullName()
    line1 = ReadConfig.getLine1()
    line2 = ReadConfig.getLine2()
    postcode = ReadConfig.getPostCode()
    city = ReadConfig.getCity()
    dline1 = ReadConfig.getDLine1()
    dline2 = ReadConfig.getDLine2()
    dPostcode = ReadConfig.getDPostCode()
    dCity = ReadConfig.getDCity()
    mobileNumber = ReadConfig.getMobileNumber()
    email = ReadConfig.getEmail()

    def test_PostPaidNewRegistration(self, setup):
        self.driver = setup
        self.driver.get(self.appURL)
        self.pPNR = PostPaidNewRegistration(self.driver)
        # time.sleep(10)
        self.pPNR.clickBuyNow160Button()
        self.pPNR.clickRadioButton()
        self.pPNR.enterIDNumber(self.idNumber)
        self.pPNR.clickSubmitButton()
        self.pPNR.clickSelectNumber()
        self.pPNR.clickCheckOutButton()
        self.pPNR.clickUploadButton()
        self.pPNR.clickPopupUploadButton1()
        time.sleep(2)
        self.pPNR.clickUploadButton()
        time.sleep(2)
        # self.pPNR.clickUploadSelfieButton()
        self.pPNR.clickPopupUploadButton2()
        self.pPNR.clickSaveButton()
        self.pPNR.enterFullName(self.fullName)
        self.pPNR.enterLine1(self.line1)
        self.pPNR.enterLine2(self.line2)
        self.pPNR.enterPostcode(self.postcode)
        self.pPNR.enterCity(self.city)
        # self.pPNR.selectStateValue()
        self.pPNR.clickSaveButton()
        self.pPNR.clickYouIDDetailsYes()
        self.pPNR.enterEmailID(self.email)
        self.pPNR.enterDLine1(self.dline1)
        self.pPNR.enterDLine2(self.dline2)
        self.pPNR.enterDPostcode(self.dPostcode)
        self.pPNR.enterDCity(self.dCity)
        self.pPNR.enterMobileNumber(self.mobileNumber)
        self.pPNR.clickDSaveButton()
        self.pPNR.clickIAgreeCheckBox()
        self.pPNR.clickPayNow()
