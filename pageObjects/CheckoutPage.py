from selenium.webdriver.common.by import By

from pageObjects.ConfirmationPage import ConfirmPage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, "div.card")  # driver.find_elements_by_css_selector("")
    checkFooter = (By.CSS_SELECTOR, "div button")
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckoutPage.checkFooter)

    def checkOutItems(self):  # driver.find_element_by_xpath("//button[@class='btn btn-success']")
        self.driver.find_element(*CheckoutPage.checkOut).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
