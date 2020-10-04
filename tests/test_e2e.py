import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()
        log.info("Getting all the card titles")
        # self.driver.find_element_by_css_selector("a[href*='shop']").click()
        # checkoutPage = CheckoutPage(self.driver)
        # products = checkoutPage.getCardTitles()
        # products = self.driver.find_elements_by_css_selector("div.card")
        cards = checkoutPage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutPage.getCardFooter()[i].click()

        self.driver.find_element_by_css_selector(".btn-primary").click()
        # self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        confirmPage = checkoutPage.checkOutItems()
        log.info("Entering country name Ind")
        self.driver.find_element_by_id("country").send_keys("Ind")
        self.verifyLinkPresence("India")
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector(".btn-success").click()
        message = self.driver.find_element_by_class_name("alert-success").text
        log.info("Text received from application is " + message)
        assert "Success" in message
        self.driver.get_screenshot_as_file("D://ss.png")
