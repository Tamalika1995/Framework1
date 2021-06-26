import allure
import pytest
from pages.login_page import *
from pages.home_page import *
from utils import Utils as util
import moment
@pytest.mark.usefixtures("test_setup")
class Test_login():
    def test_login(self,test_setup):
        driver=self.driver
        login=login_Page(driver)
        global current_time
        global s_name
        global testname
        current_time = moment.now().strftime('%d-%m-%y_%H:%M:%S')
        testname=util.whoami()
        s_name = testname+'_' + current_time
        allure.attach(driver.get_screenshot_as_png(), name=s_name, attachment_type=allure.attachment_type.PNG)
        driver.save_screenshot(r'C:/Users/614785.old/PycharmProjects/Framework1/screenshots/'+s_name+".png")
        login.enter_username(util.USERNAME)
        login.enter_password(util.PASSWORD)
        allure.attach(driver.get_screenshot_as_png(), name=s_name, attachment_type=allure.attachment_type.PNG)
        driver.save_screenshot(r'C:/Users/614785.old/PycharmProjects/Framework1/screenshots/' + s_name + ".png")
        login.click_login()
        allure.attach(driver.get_screenshot_as_png(),name=s_name,attachment_type=allure.attachment_type.PNG)
        driver.save_screenshot(r'C:/Users/614785.old/PycharmProjects/Framework1/screenshots/' + s_name + ".png")

    def test_logout(self,test_setup):
        driver = self.driver
        hm_pg=home_page(driver)
        hm_pg.click_welcome()
        current_time = moment.now().strftime('%d-%m-%y_%H:%M:%S')
        testname = util.whoami()
        s_name = testname + '_' + current_time
        allure.attach(driver.get_screenshot_as_png(), name=s_name, attachment_type=allure.attachment_type.PNG)
        driver.get_screenshot_as_file(r"C:\Users\614785.old\PycharmProjects\Framework1\screenshots\ss.png")
        hm_pg.click_logout()
        allure.attach(driver.get_screenshot_as_png(), name=s_name, attachment_type=allure.attachment_type.PNG)
