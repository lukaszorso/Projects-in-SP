import unittest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import pytest
import allure
from utils.driver_factory import DriverFactory
from datetime import date

class TestBookingVisit(unittest.TestCase):
    #@pytest.fixture()
    def setUp(self):
        self.driver = DriverFactory.get_driver("chrome")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    @allure.step("Desk booking")
    def test_chrome(self):
        driver = self.driver
        driver.get(
            "https")
        driver.find_element_by_name("loginfmt").send_keys("...")
        driver.find_element_by_name("loginfmt").send_keys(Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_id("i0118").send_keys("...")
        driver.execute_script("arguments[0].click();", driver.find_element_by_id("idSIButton9"))
        checkbox = driver.find_element_by_xpath("//*[@id='KmsiCheckboxField']")
        if checkbox.is_selected():
            print("Wartosc zaznaczona, odznaczam!")
            checkbox.click()
        else:
            print("Zaznaczam wartosc")
            checkbox.click()
        driver.find_element_by_id("idSIButton9").click()
        time.sleep(3)
        print(driver.title)
        driver.switch_to.frame(driver.find_element_by_xpath("//*[@class='publishedAppIframe']"))
        print(driver.title)
        time.sleep(3)
        #adding request
        driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div[2]/div/div/div[5]/div/div/div/div/button/div").click()
        driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div[3]/div/div/div[5]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/div/div/div[1]").click()
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/ul/li[2]").click()
        driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div[3]/div/div/div[5]/div/div/div/div/div/div/div/div/div[3]/div/div/div/div[3]/div/div/div/div[1]/div[2]").click()
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/ul/li[4]").click()
        # time.sleep(5)
        driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div[3]/div/div/div[5]/div/div/div/div/div/div/div/div/div[4]/div/div/div/div[4]/div/div/div/div[1]/div[2]").click()
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/ul/li[3]").click()
        calendar = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div[3]/div[1]/div/div[5]/div/div/div/div/div/div/div/div/div[6]/div/div/div/div[3]/div/div/div/div/input")
        calendar.clear()

        # setting current day
        #today = date.today()
        calendar.send_keys("31/08/2020")
        time.sleep(2)
        checkbox2 = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div[3]/div/div/div[12]/div/div/div/div/label/input")

        webdriver.ActionChains(driver).move_to_element(checkbox2).click(checkbox2).perform()
        if checkbox2.is_selected():
            print("Checkbox marked, button should be active")
        else:
            print("Checkbox not marked, button should be disabled")
        time.sleep(4)

        button = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div[3]/div/div/div[15]/div/div/div/div/button/div")
        if button.is_enabled():
            print("Button active")
            webdriver.ActionChains(driver).move_to_element(button).click(button).perform()
            #button.click()
            #time.sleep(4)
         # print(button.get_attribute("textContent"))
        else:
            print("Button not active")

        wait = WebDriverWait(driver, 20, 0.2, NoSuchElementException)
        wait.until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, 'appmagic-label-text'), 'You have successfully booked a visit'))
        print(driver.find_element_by_class_name("appmagic-label-text").text)

        #Adding request for the same day - unable
        driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div[2]/div/div/div[5]/div/div/div/div/button/div").click()
        driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div[3]/div/div/div[5]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/div/div/div[1]").click()
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/ul/li[2]").click()
        driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div[3]/div/div/div[5]/div/div/div/div/div/div/div/div/div[3]/div/div/div/div[3]/div/div/div/div[1]/div[2]").click()
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/ul/li[4]").click()
        driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div[3]/div/div/div[5]/div/div/div/div/div/div/div/div/div[4]/div/div/div/div[4]/div/div/div/div[1]/div[2]").click()
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/ul/li[3]").click()
        calendar = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div[3]/div[1]/div/div[5]/div/div/div/div/div/div/div/div/div[6]/div/div/div/div[3]/div/div/div/div/input")
        calendar.clear()
        calendar.send_keys("31/08/2020")
        time.sleep(4)
        checkbox2 = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div[3]/div/div/div[12]/div/div/div/div/label/input")

        webdriver.ActionChains(driver).move_to_element(checkbox2).click(checkbox2).perform()
        if checkbox2.is_selected():
            print("Checkbox marked, button should be active")
        else:
            print("Checkbox not marked, button should be disabled")
        time.sleep(4)

        button = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div[3]/div/div/div[15]/div/div/div/div/button/div")
        if button.is_enabled():
            print("Button active")
            button.click()
            time.sleep(4)
        # print(button.get_attribute("textContent"))
        else:
            print("Button not active")

        driver.switch_to.default_content()

        wait = WebDriverWait(driver, 30, 0.2, NoSuchElementException)
        wait.until(expected_conditions.visibility_of_element_located((By.ID, 'toast-container')))
        driver.save_screenshot("Screenshots_already_booked/first.png")
        print(driver.find_element_by_id("toast-container").text)
        driver.quit()

