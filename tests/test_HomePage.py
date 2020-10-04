import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_formSubmission(self, getData):
        log = self.getLogger()
        # driver.find_element_by_name("name").send_keys("Ravi Kant")
        homePage = HomePage(self.driver)
        log.info("First name is "+getData["Name"])
        homePage.getName().send_keys(getData["Name"])
        # driver.find_element_by_css_selector("input[name='name']").send_keys("Ravi")
        homePage.getEmail().send_keys(getData["Email"])
        # driver.find_element_by_name("email").send_keys("kant.dos@gmail.com")
        homePage.getPassword().send_keys("Asdf123")
        homePage.getCheckBox().click()
        # select class provide the methods to handle the options in dropdown
        # dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
        # dropdown.select_by_visible_text("Female")
        # dropdown.select_by_index(0)
        # dropdown.select_by_value("Female")
        self.selectOptionByText(homePage.getGender(), getData["Gender"])
        homePage.submitForm().click()
        self.driver.get_screenshot_as_file("D:\\ss.png")
        # print(driver.find_element_by_class_name("alert-success").text)
        message = homePage.getMessage().text
        # message = driver.find_element_by_css_selector("[class*='alert-success']").text  # /*[contains(@class,
        # 'alert-success')] - xpath
        assert "Success" in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePageData)
    def getData(self, request):
        return request.param
