import time
import unittest

from selenium import webdriver

from pages.login_page import login


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver= webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()


    def test_01(self):
        login(self.driver)
        time.sleep(3)
        t1 = self.driver.find_element_by_xpath(".//*[@id='root']/div/div/section/section/header/ul/li/div/div/span").text
        self.assertTrue(t1=="超级管理员")

    def test_02(self):
        login(self.driver,"admin","524")
        time.sleep(3)
        hh=self.driver.find_element_by_xpath("html/body/div[2]/div/span/div/div/div/span")   .text
        print(hh)
        self.assertTrue(hh=="用户名或密码错误")
