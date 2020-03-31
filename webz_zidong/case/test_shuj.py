from selenium import webdriver
from pages.shujguangli import DataGl
import unittest
from common.base import Base
from common.base import Base

class Sj(unittest.TestCase):
    def setUp(self):
        self.driver= webdriver.Chrome()
        self.driver.get("http://192.168.0.60/#/login")
    def tearDown(self):
        self.driver.quit()

    def test_login1(self):
        loc_sj = ("xpath",".//*[@id='root']/div/div/section/aside/div[1]/div/div[1]/ul/li[3]/div")
        loc_jb =("xpath",".//*[@id='data$Menu']/li[1]/a")
        loc_hm=("xpath",".//*[@id='reportedTelcode']")
        loc_select = ("xpath",".//*[@id='content']/form/div/div[1]/div[3]/button")
        locss= ("xpath",".//*[@id='content']/form/div/div[2]/div/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[3]")

        data=DataGl(self.driver)
        data.login()
        data.click(loc_sj)
        data.click(loc_jb)
        data.sendKeys(loc_hm,"106943792557570077")
        data.click(loc_select)
        data.click(loc_sj)
        ss=data.get_text(locss)
        print(ss)
        print(type(ss))





        self.assertTrue("106943792557570077"==ss)

