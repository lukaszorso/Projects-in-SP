import unittest
from urllib import request
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import pytest
import allure

class TestAddingOrders(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(r"")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        #before_failed = request.session.testfailed
        #yield
        #if request.session.testfailed != before_failed:
         #   allure.attach(self.driver.get_screenshot_as_png(), name="Test failed ", attachment_type=AttachmentType.PNG)


    @allure.step("Adding first order")
    def test_one(self):
        #authentication to SP and login
        driver = self.driver
        driver.get("https...")
        driver.find_element_by_name("loginfmt").send_keys("...")
        driver.find_element_by_name("loginfmt").send_keys(Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_id("i0118").send_keys("...")
        driver.execute_script("arguments[0].click();", driver.find_element_by_id("idSIButton9"))
        time.sleep(2)
        checkbox = driver.find_element_by_xpath("//*[@id='KmsiCheckboxField']")
        if checkbox.is_selected():
            print("Value checked, tick!")
            checkbox.click()
        else:
            print("Check value")
            checkbox.click()
        time.sleep(2)
        driver.find_element_by_id("idSIButton9").click()
        time.sleep(2)

        new_order = driver.find_element_by_name("Create new order")
        webdriver.ActionChains(driver).move_to_element(new_order).click(new_order).perform()
        time.sleep(10)
        #iframe
        driver.switch_to.frame(driver.find_element_by_id("SPAppIFrame1"))
        print(driver.title)
        time.sleep(5)
        #filling out form
        department = driver.find_element_by_xpath('//*[@formcontrolid="026903c7-0de4-4ef8-baf5-edd0ad95a78e"]')
        webdriver.ActionChains(driver).move_to_element(department).click(department)
        driver.find_element_by_xpath('//*[@value="Marketing"]').click()
        driver.find_element_by_xpath('//*[@title="Contact address"]').send_keys("test")
        driver.find_element_by_xpath('//*[@title="Contact name"]').send_keys("LN")
        driver.find_element_by_xpath('//*[@title="Contact number"]').send_keys("666")
        address = "55"
        driver.execute_script("arguments[0].setAttribute('value', '" + address + "')", driver.find_element_by_xpath(
            "/html/body/form/div[6]/div/div[2]/table/tbody/tr/td/div/div[21]/div/div/div/input"))
        contact_city = "Berlin"
        driver.execute_script("arguments[0].setAttribute('value', '" + contact_city + "')",
                              driver.find_element_by_xpath(
                                  "/html/body/form/div[6]/div/div[2]/table/tbody/tr/td/div/div[23]/div/div/div/input"))
        post_code = "21500"
        driver.execute_script("arguments[0].setAttribute('value', '" + post_code + "')", driver.find_element_by_xpath(
            "/html/body/form/div[6]/div/div[2]/table/tbody/tr/td/div/div[28]/div/div/div/input"))
        reason_for_sample = driver.find_element_by_xpath('//*[@formcontrolid="50af3271-7f7b-4e23-86d2-f1a4269d9b31"]')
        option5 = driver.find_element_by_xpath('//option[@title="In-store Sampling"]')
        webdriver.ActionChains(driver).move_to_element(reason_for_sample).click(reason_for_sample)
        option5.click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/form/div[6]/div/div[2]/table/tbody/tr/td/div/div[33]/div/div/div/textarea").send_keys("reason1")
        #adding Brands
        driver.find_element_by_xpath("//span[text()='Select SKU']").click()
        #driver.find_element_by_xpath("/html/body/form/div[6]/div/div[2]/table/tbody/tr/td/div/div[40]/div/div/div/div[2]/div[3]/div/div/div/div/span/span[1]/span").click()
        driver.find_element_by_xpath("//span[@class='select2-search select2-search--dropdown']//input").send_keys(
            '2033086')
        driver.find_element_by_xpath("//li[text()='2033086']").click()
        time.sleep(2)
        qty = "31"
        #driver.execute_script("arguments[0].setAttribute('value', '" + qty + "')", driver.find_element_by_xpath("/html/body/form/div[6]/div/div[2]/table/tbody/tr/td/div/div[42]/div/div/div/div[2]/div[4]/div/div/div/input"))
        driver.find_element_by_xpath(
            "/html/body/form/div[6]/div/div[2]/table/tbody/tr/td/div/div[43]/div/div/div/div[2]/div[5]/div/div/div/input").send_keys(qty)
        submit = driver.find_element_by_xpath("//*[@value='SUBMIT']")
        webdriver.ActionChains(driver).move_to_element(submit).click(submit).perform()
        time.sleep(2)
        #alert
        driver.switch_to.alert.accept()
        time.sleep(1)
        driver.switch_to.default_content()
        #screenshot
        allure.attach(driver.get_screenshot_as_png(), name="submit_order", attachment_type=AttachmentType.PNG)
        driver.quit()

    def test_two(self):
        driver = self.driver
        driver.get("https")
        driver.find_element_by_name("loginfmt").send_keys("...")
        driver.find_element_by_name("loginfmt").send_keys(Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_id("i0118").send_keys("...")
        time.sleep(2)
        driver.execute_script("arguments[0].click();", driver.find_element_by_id("idSIButton9"))
        time.sleep(2)
        checkbox = driver.find_element_by_xpath("//*[@id='KmsiCheckboxField']")
        if checkbox.is_selected():
            print("Value checked, tick!")
            checkbox.click()
        else:
            print("Value checked")
            checkbox.click()
        time.sleep(2)
        driver.find_element_by_id("idSIButton9").click()
        time.sleep(3)
        new_order = driver.find_element_by_name("Create new order")
        webdriver.ActionChains(driver).move_to_element(new_order).click(new_order).perform()
        time.sleep(10)
        driver.switch_to.frame(driver.find_element_by_id("SPAppIFrame1"))
        print(driver.title)
        department = driver.find_element_by_xpath('//*[@formcontrolid="026903c7-0de4-4ef8-baf5-edd0ad95a78e"]')
        webdriver.ActionChains(driver).move_to_element(department).click(department)
        driver.find_element_by_xpath('//*[@value="Marketing"]').click()
        driver.find_element_by_xpath('//*[@title="Contact address"]').send_keys("test")
        driver.find_element_by_xpath('//*[@title="Contact name"]').send_keys("LN")
        driver.find_element_by_xpath('//*[@title="Contact number"]').send_keys("333")
        address = "55"
        driver.execute_script("arguments[0].setAttribute('value', '" + address + "')", driver.find_element_by_xpath(
            "/html/body/form/div[6]/div/div[2]/table/tbody/tr/td/div/div[21]/div/div/div/input"))
        contact_city = "Warsaw"
        driver.execute_script("arguments[0].setAttribute('value', '" + contact_city + "')",
                              driver.find_element_by_xpath(
                                  "/html/body/form/div[6]/div/div[2]/table/tbody/tr/td/div/div[23]/div/div/div/input"))
        post_code = "45000"
        driver.execute_script("arguments[0].setAttribute('value', '" + post_code + "')", driver.find_element_by_xpath(
            "/html/body/form/div[6]/div/div[2]/table/tbody/tr/td/div/div[28]/div/div/div/input"))
        reason_for_sample = driver.find_element_by_xpath('//*[@formcontrolid="50af3271-7f7b-4e23-86d2-f1a4269d9b31"]')
        option5 = driver.find_element_by_xpath('//option[@title="In-store Sampling"]')
        webdriver.ActionChains(driver).move_to_element(reason_for_sample).click(reason_for_sample)
        option5.click()
        time.sleep(2)
        driver.find_element_by_xpath(
            "/html/body/form/div[6]/div/div[2]/table/tbody/tr/td/div/div[33]/div/div/div/textarea").send_keys("reason2")
        driver.find_element_by_xpath("//span[text()='Select SKU']").click()
        #driver.find_element_by_xpath(
         #   "/html/body/form/div[6]/div/div[2]/table/tbody/tr/td/div/div[40]/div/div/div/div[2]/div[3]/div/div/div/div/span/span[1]/span").click()
        driver.find_element_by_xpath("//span[@class='select2-search select2-search--dropdown']//input").send_keys(
            '2033086')
        driver.find_element_by_xpath("//li[text()='2033086']").click()
        time.sleep(4)
        qty = "32"
        #driver.execute_script("arguments[0].setAttribute('value', '" + qty + "')", driver.find_element_by_xpath(
         #   "/html/body/form/div[6]/div/div[2]/table/tbody/tr/td/div/div[42]/div/div/div/div[2]/div[4]/div/div/div/input"))
        driver.find_element_by_xpath(
            "/html/body/form/div[6]/div/div[2]/table/tbody/tr/td/div/div[43]/div/div/div/div[2]/div[5]/div/div/div/input").send_keys(qty)
        submit = driver.find_element_by_xpath("//*[@value='SUBMIT']")
        webdriver.ActionChains(driver).move_to_element(submit).click(submit).perform()
        time.sleep(3)
        driver.switch_to.alert.accept()
        time.sleep(3)
        driver.switch_to.default_content()
        #screenshot
        allure.attach(driver.get_screenshot_as_png(), name="submit_order", attachment_type=AttachmentType.PNG)
        driver.quit()

    def test_three(self):
        driver = self.driver
        driver.get("https")
        driver.find_element_by_name("loginfmt").send_keys("...")
        driver.find_element_by_name("loginfmt").send_keys(Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_id("i0118").send_keys("...")
        time.sleep(2)
        driver.execute_script("arguments[0].click();", driver.find_element_by_id("idSIButton9"))
        time.sleep(2)
        checkbox = driver.find_element_by_xpath("//*[@id='KmsiCheckboxField']")
        if checkbox.is_selected():
            print("Value checked, tick!")
            checkbox.click()
        else:
            print("Value checked")
            checkbox.click()
        time.sleep(3)
        driver.find_element_by_id("idSIButton9").click()
        time.sleep(3)
        new_order = driver.find_element_by_name("Create new order")
        webdriver.ActionChains(driver).move_to_element(new_order).click(new_order).perform()
        time.sleep(10)
        driver.switch_to.frame(driver.find_element_by_id("SPAppIFrame1"))
        print(driver.title)
        department = driver.find_element_by_xpath('//*[@formcontrolid="026903c7-0de4-4ef8-baf5-edd0ad95a78e"]')
        webdriver.ActionChains(driver).move_to_element(department).click(department)
        driver.find_element_by_xpath('//*[@value="Marketing"]').click()
        driver.find_element_by_xpath('//*[@title="Contact address"]').send_keys("test")
        driver.find_element_by_xpath('//*[@title="Contact name"]').send_keys("LN")
        driver.find_element_by_xpath('//*[@title="Contact number"]').send_keys("222")
        address = "43"
        driver.execute_script("arguments[0].setAttribute('value', '" + address + "')", driver.find_element_by_xpath(
            "/html/body/form/div[6]/div/div[2]/table/tbody/tr/td/div/div[21]/div/div/div/input"))
        contact_city = "Oslo"
        driver.execute_script("arguments[0].setAttribute('value', '" + contact_city + "')",
                              driver.find_element_by_xpath(
                                  "/html/body/form/div[6]/div/div[2]/table/tbody/tr/td/div/div[23]/div/div/div/input"))
        post_code = "34000"
        driver.execute_script("arguments[0].setAttribute('value', '" + post_code + "')", driver.find_element_by_xpath(
            "/html/body/form/div[6]/div/div[2]/table/tbody/tr/td/div/div[28]/div/div/div/input"))
        reason_for_sample = driver.find_element_by_xpath('//*[@formcontrolid="50af3271-7f7b-4e23-86d2-f1a4269d9b31"]')
        option5 = driver.find_element_by_xpath('//option[@title="In-store Sampling"]')
        webdriver.ActionChains(driver).move_to_element(reason_for_sample).click(reason_for_sample)
        option5.click()
        time.sleep(2)
        driver.find_element_by_xpath(
            "/html/body/form/div[6]/div/div[2]/table/tbody/tr/td/div/div[33]/div/div/div/textarea").send_keys("reason3")
        driver.find_element_by_xpath("//span[text()='Select SKU']").click()
        #driver.find_element_by_xpath(
         #   "/html/body/form/div[6]/div/div[2]/table/tbody/tr/td/div/div[40]/div/div/div/div[2]/div[3]/div/div/div/div/span/span[1]/span").click()
        driver.find_element_by_xpath("//span[@class='select2-search select2-search--dropdown']//input").send_keys(
            '0233308')
        driver.find_element_by_xpath("//li[text()='0233308']").click()
        time.sleep(4)
        qty = "22"
        #driver.execute_script("arguments[0].setAttribute('value', '" + qty + "')", driver.find_element_by_xpath(
         #   "/html/body/form/div[6]/div/div[2]/table/tbody/tr/td/div/div[42]/div/div/div/div[2]/div[4]/div/div/div/input"))
        driver.find_element_by_xpath(
            "/html/body/form/div[6]/div/div[2]/table/tbody/tr/td/div/div[43]/div/div/div/div[2]/div[5]/div/div/div/input").send_keys(qty)
        submit = driver.find_element_by_xpath("//*[@value='SUBMIT']")
        webdriver.ActionChains(driver).move_to_element(submit).click(submit).perform()
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(2)
        driver.switch_to.default_content()
        allure.attach(driver.get_screenshot_as_png(), name="submit_order", attachment_type=AttachmentType.PNG)
        driver.quit()

    def test_four(self):
        driver = self.driver
        driver.get("https")
        driver.find_element_by_name("loginfmt").send_keys("...")
        driver.find_element_by_name("loginfmt").send_keys(Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_id("i0118").send_keys("...")
        time.sleep(2)
        driver.execute_script("arguments[0].click();", driver.find_element_by_id("idSIButton9"))
        time.sleep(2)
        checkbox = driver.find_element_by_xpath("//*[@id='KmsiCheckboxField']")
        if checkbox.is_selected():
            print("Value checked, tick!")
            checkbox.click()
        else:
            print("Value checked")
            checkbox.click()
        time.sleep(2)
        driver.find_element_by_id("idSIButton9").click()
        time.sleep(3)
        new_order = driver.find_element_by_name("Create new order")
        webdriver.ActionChains(driver).move_to_element(new_order).click(new_order).perform()
        time.sleep(10)
        driver.switch_to.frame(driver.find_element_by_id("SPAppIFrame1"))
        print(driver.title)
        department = driver.find_element_by_xpath('//*[@formcontrolid="026903c7-0de4-4ef8-baf5-edd0ad95a78e"]')
        webdriver.ActionChains(driver).move_to_element(department).click(department)
        driver.find_element_by_xpath('//*[@value="Marketing"]').click()
        driver.find_element_by_xpath('//*[@title="Contact address"]').send_keys("test")
        driver.find_element_by_xpath('//*[@title="Contact name"]').send_keys("LN")
        driver.find_element_by_xpath('//*[@title="Contact number"]').send_keys("999")
        address = "88"
        driver.execute_script("arguments[0].setAttribute('value', '" + address + "')", driver.find_element_by_xpath(
            "/html/body/form/div[6]/div/div[2]/table/tbody/tr/td/div/div[21]/div/div/div/input"))
        contact_city = "London"
        driver.execute_script("arguments[0].setAttribute('value', '" + contact_city + "')",
                              driver.find_element_by_xpath(
                                  "/html/body/form/div[6]/div/div[2]/table/tbody/tr/td/div/div[23]/div/div/div/input"))
        post_code = "33422"
        driver.execute_script("arguments[0].setAttribute('value', '" + post_code + "')", driver.find_element_by_xpath(
            "/html/body/form/div[6]/div/div[2]/table/tbody/tr/td/div/div[28]/div/div/div/input"))
        reason_for_sample = driver.find_element_by_xpath('//*[@formcontrolid="50af3271-7f7b-4e23-86d2-f1a4269d9b31"]')
        option5 = driver.find_element_by_xpath('//option[@title="In-store Sampling"]')
        webdriver.ActionChains(driver).move_to_element(reason_for_sample).click(reason_for_sample)
        option5.click()
        time.sleep(2)
        driver.find_element_by_xpath(
            "/html/body/form/div[6]/div/div[2]/table/tbody/tr/td/div/div[33]/div/div/div/textarea").send_keys("reason4")
        driver.find_element_by_xpath("//span[text()='Select SKU']").click()
        #driver.find_element_by_xpath(
            #"/html/body/form/div[6]/div/div[2]/table/tbody/tr/td/div/div[40]/div/div/div/div[2]/div[3]/div/div/div/div/span/span[1]/span").click()
        driver.find_element_by_xpath("//span[@class='select2-search select2-search--dropdown']//input").send_keys(
            '3003129')
        driver.find_element_by_xpath("//li[text()='3003129']").click()
        time.sleep(4)
        qty = "56"
        #driver.execute_script("arguments[0].setAttribute('value', '" + qty + "')", driver.find_element_by_xpath(
         #   "/html/body/form/div[6]/div/div[2]/table/tbody/tr/td/div/div[42]/div/div/div/div[2]/div[4]/div/div/div/input"))
        driver.find_element_by_xpath(
            "/html/body/form/div[6]/div/div[2]/table/tbody/tr/td/div/div[43]/div/div/div/div[2]/div[5]/div/div/div/input").send_keys(qty)
        submit = driver.find_element_by_xpath("//*[@value='SUBMIT']")
        webdriver.ActionChains(driver).move_to_element(submit).click(submit).perform()
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(2)
        driver.switch_to.default_content()
        allure.attach(driver.get_screenshot_as_png(), name="submit_order", attachment_type=AttachmentType.PNG)
        driver.quit()

    def test_five(self):
        driver = self.driver
        driver.get("https")
        driver.find_element_by_name("loginfmt").send_keys("...")
        driver.find_element_by_name("loginfmt").send_keys(Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_id("i0118").send_keys("...")
        time.sleep(2)
        driver.execute_script("arguments[0].click();", driver.find_element_by_id("idSIButton9"))
        time.sleep(2)
        checkbox = driver.find_element_by_xpath("//*[@id='KmsiCheckboxField']")
        if checkbox.is_selected():
            print("Wartosc zaznaczona, odznaczam!")
            checkbox.click()
        else:
            print("Zaznaczam wartosc")
            checkbox.click()
        time.sleep(2)
        driver.find_element_by_id("idSIButton9").click()
        time.sleep(2)
        new_order = driver.find_element_by_name("Create new order")
        webdriver.ActionChains(driver).move_to_element(new_order).click(new_order).perform()
        time.sleep(10)
        driver.switch_to.frame(driver.find_element_by_id("SPAppIFrame1"))
        print(driver.title)
        department = driver.find_element_by_xpath('//*[@formcontrolid="026903c7-0de4-4ef8-baf5-edd0ad95a78e"]')
        webdriver.ActionChains(driver).move_to_element(department).click(department)
        driver.find_element_by_xpath('//*[@value="Marketing"]').click()
        driver.find_element_by_xpath('//*[@title="Contact address"]').send_keys("test")
        driver.find_element_by_xpath('//*[@title="Contact name"]').send_keys("LN")
        driver.find_element_by_xpath('//*[@title="Contact number"]').send_keys("454")
        address = "23"
        driver.execute_script("arguments[0].setAttribute('value', '" + address + "')", driver.find_element_by_xpath(
            "/html/body/form/div[6]/div/div[2]/table/tbody/tr/td/div/div[21]/div/div/div/input"))
        contact_city = "Berlin"
        driver.execute_script("arguments[0].setAttribute('value', '" + contact_city + "')",
                              driver.find_element_by_xpath(
                                  "/html/body/form/div[6]/div/div[2]/table/tbody/tr/td/div/div[23]/div/div/div/input"))
        post_code = "65242"
        driver.execute_script("arguments[0].setAttribute('value', '" + post_code + "')", driver.find_element_by_xpath(
            "/html/body/form/div[6]/div/div[2]/table/tbody/tr/td/div/div[28]/div/div/div/input"))
        reason_for_sample = driver.find_element_by_xpath('//*[@formcontrolid="50af3271-7f7b-4e23-86d2-f1a4269d9b31"]')
        option5 = driver.find_element_by_xpath('//option[@title="In-store Sampling"]')
        webdriver.ActionChains(driver).move_to_element(reason_for_sample).click(reason_for_sample)
        option5.click()
        time.sleep(1)
        driver.find_element_by_xpath(
            "/html/body/form/div[6]/div/div[2]/table/tbody/tr/td/div/div[33]/div/div/div/textarea").send_keys("reason5")
        driver.find_element_by_xpath("//span[text()='Select SKU']").click()
        #driver.find_element_by_xpath(
         #   "/html/body/form/div[6]/div/div[2]/table/tbody/tr/td/div/div[40]/div/div/div/div[2]/div[3]/div/div/div/div/span/span[1]/span").click()
        driver.find_element_by_xpath("//span[@class='select2-search select2-search--dropdown']//input").send_keys(
            '3003129')
        driver.find_element_by_xpath("//li[text()='3003129']").click()
        time.sleep(2)
        qty = "77"
        #driver.execute_script("arguments[0].setAttribute('value', '" + qty + "')", driver.find_element_by_xpath(
         #   "/html/body/form/div[6]/div/div[2]/table/tbody/tr/td/div/div[42]/div/div/div/div[2]/div[4]/div/div/div/input"))
        driver.find_element_by_xpath("/html/body/form/div[6]/div/div[2]/table/tbody/tr/td/div/div[43]/div/div/div/div[2]/div[5]/div/div/div/input").send_keys(qty)
        submit = driver.find_element_by_xpath("//*[@value='SUBMIT']")
        webdriver.ActionChains(driver).move_to_element(submit).click(submit).perform()
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(2)
        driver.switch_to.default_content()
        allure.attach(driver.get_screenshot_as_png(), name="submit_order", attachment_type=AttachmentType.PNG)
        driver.quit()

    def tear_down(self):
        self.driver.close()
