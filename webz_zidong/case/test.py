from selenium import webdriver
import time
import unittest




class LoginFail(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://192.168.0.60/#/login")

    def tearDown(sef):
        sef.driver.delete_all_cookies() #情况cookis
        sef.driver.refresh() #刷新浏览器

    def is_login_sucess(self):
        try:
            hh=self.driver.find_element_by_xpath("html/body/div[2]/div/span/div/div/div/span")   .text
        except:
            return ""


    def test_01(self):
        '''测试登录失败'''

        time.sleep(3)
        self.driver.find_element_by_id("username").send_keys("admin")
        self.driver.find_element_by_id("password").send_keys("1723456")
        self.driver.find_element_by_xpath(".//*[@id='root']/div/div/div[1]/div/div[2]/form/button").click()
        time.sleep(1)
        hh=self.driver.find_element_by_xpath("html/body/div[2]/div/span/div/div/div/span")   .text
        print(hh)
        self.assertTrue(hh=="用户名或密码错误")
    def test_02(self):
        '''测试登录成功'''
        # if self.isElementPresent("id", 'username'):
        #   fromCity = self.driver.find_element_by_xpath("//span[@id='form:PORLocation0']").text
        #   print("元素存在啊")
        # else:
        #   print("元素值不存在")


        self.driver.find_element_by_id("username").send_keys("admin")
        self.driver.find_element_by_id("password").send_keys("123456")
        self.driver.find_element_by_xpath(".//*[@id='root']/div/div/div[1]/div/div[2]/form/button").click()
        #判断是否登录成功
        time.sleep(5)
        t1 = self.driver.find_element_by_xpath(".//*[@id='root']/div/div/section/section/header/ul/li/div/div/span").text
        self.assertTrue(t1=="超级管1理员")


