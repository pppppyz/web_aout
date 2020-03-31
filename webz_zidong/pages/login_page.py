





def login(driver,usr="admin",pwd="123456"):
    driver.get("http://192.168.0.60/#/login")
    driver.find_element_by_id("username").send_keys(usr)
    driver.find_element_by_id("password").send_keys(pwd)
    driver.find_element_by_xpath(".//*[@id='root']/div/div/div[1]/div/div[2]/form/button").click()



# if __name__ =="__main__":
#     from selenium import webdriver
#     import unittest
#     driver = webdriver.Chrome()
#
#     login(driver)
#     driver.quit()