from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
import time


 # Example:
 #            from selenium.webdriver.support.ui import WebDriverWait \n
 #            element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("someId")) \n
 #            is_disappeared = WebDriverWait(driver, 30, 1, (ElementNotVisibleException)).\ \n
 #                        until_not(lambda x: x.find_element_by_id("someId").is_displayed())
 #

driver = webdriver.Chrome()
driver.get("http://192.168.0.60/#/login")
#返回的是元素对象
# driver.find_element(By.ID,"username")
# driver.find_element(By.ID,"password")


def findElement(driver,loctor,timeout=10,t=0.5):
    ele = WebDriverWait(driver, 10).until(lambda x: x.find_element(*loctor))
    return  ele


loc1 = (By.ID,"username")
loc2 = (By.ID,"password")
loc3 = (By.XPATH,".//*[@id='root']/div/div/div[1]/div/div[2]/form/button")

findElement(driver,loc1).send_keys("admin")

findElement(driver,loc2).send_keys("123456")

findElement(driver,loc3).click()

time.sleep(3)
driver.quit()
# ele1 = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("password"))
# ele2 = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(".//*[@id='root']/div/div/div[1]/div/div[2]/form/button"))
# print(ele)
# ele.send_keys("admin")
# ele1.send_keys("123456")
# ele2.click()
# driver.quit()