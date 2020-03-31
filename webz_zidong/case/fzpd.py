from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

##元素判断类EC

driver = webdriver.Chrome()
driver.get("http://192.168.0.60/#/login")
r1 = EC.title_is("4G110")(driver)
print(r1
      )




driver.quit()

