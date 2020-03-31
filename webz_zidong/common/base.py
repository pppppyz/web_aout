from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

import time



class Base():
    def __init__(self,driver):
        self.driver = driver
        self.timeout = 10
        self.t  = 0.5

    def findElement(self,locator):
        '''定位到元素，返回元素对象,没定位到返回超时异常'''
        if not isinstance(locator,tuple):
            print("locator参数类型错误，必须传元祖类型：loc = ('id','value')")
        else:
            print("正在定位元素信息：定位方式%s,value值->%s"%(locator[0],locator[1]))
            ele = WebDriverWait(self.driver,self.timeout,self.t).until(EC.presence_of_element_located(locator))
            return ele

    def findElements(self,locator):
        '''定位到元素，返回元素集合对象,没定位到返回超时异常'''
        if not isinstance(locator,tuple):
            print("locator参数类型错误，必须传元祖类型：loc = ('id','value')")
        else:
            try:
                print("正在定位元素信息：定位方式%s,value值->%s"%(locator[0],locator[1]))
                eles = WebDriverWait(self.driver,self.timeout,self.t).until(EC.presence_of_element_located(locator))
                return eles
            except:
                return []





    # def findElement(self,loctor):
    #     ele = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*loctor))
    #     return  ele

    def sendKeys(self,locator,text):
        ele = self.findElement(locator)
        ele.send_keys(text)


    def click(self,locator):
        ele= self.findElement(locator)
        ele.click()

    def clear(self,locator):
        #情况输入框
        ele= self.findElement(locator)
        ele.clear()

    def isSelected(self,locator):
        """判断元素是否被选中，返回bool"""
        ele= self.findElement(locator)
        r = ele.is_selected()
        return r


    def isElementExist(self,locator):
        """判断元素是否存在"""
        try:
            self.findElement(locator)
            return True
        except:
            return False


    def is_title(self,title):
        """判断title完全一样"""
        try:
            ruslt = WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_is(title))
            return ruslt
        except:
            return False


    def is_title_contains(self,title):
        """判断title包含"""
        try:
            ruslt = WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_contains(title))
            return ruslt
        except:
            return False


    def is_text_in_element(self,locator,text):
        """text文本是否在元素中，返回bool"""
        try:
            ruslt = WebDriverWait(self.driver,self.timeout,self.t).until(EC.text_to_be_present_in_element(locator,text))
            return ruslt
        except:
            return False


    def is_value_in_element(self,locator,value):
        """判断value属性中是否包含预期字符串,value中的值是空，返回False"""
        try:
            ruslt = WebDriverWait(self.driver,self.timeout,self.t).until(EC.text_to_be_present_in_element_value(locator,value))
            return ruslt
        except:
            return False


    def is_alert(self):
        """判断alert是否存在，存在返回alert，可以进行alert操作，不存在返回False"""
        ruslt = WebDriverWait(self.driver,self.timeout,self.t).until(EC.alert_is_present())
        return ruslt


    def move_to_element(self,locator):
        """鼠标悬停操作"""
        ele = self.findElement(locator)
        ActionChains(driver).move_to_element(locator).perform()

    """Select方法
    index
    value
    text"""
    def select_by_index(self,locator,index=0):
        """通过索引，从0开始，默认选第一个"""
        ele = self.findElement(locator)# 先定位select这一栏
        Select(ele).select_by_index(index)

    def select_by_value(self,locator,value):
        """通过value属性"""
        ele = self.findElement(locator)# 先定位select这一栏
        Select(ele).select_by_index(value)

    def select_by_text(self,locator,text):
        """通过文本值定位"""
        ele = self.findElement(locator)# 先定位select这一栏
        Select(ele).select_by_index(text)


    """js操作浏览器滚动条"""

    def js_scroll_end(self):
        """滚动到底部"""
        js= "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)

    def js_scroll_top(self):
        """滚动到顶部"""
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_focus_element(self,locator):
        """聚焦元素"""
        ele = self.findElement(locator)
        self.driver.execute_script("arguments[0].scrollIntoview();",ele)


    def get_text(self,locator):

        try:
            ele= self.findElement(locator).text
            return ele
        except:
            print("获取文本失败")
            return ""



if __name__ == "__main__":
    #调用
    driver = webdriver.Chrome()
    driver.get("http://192.168.0.60/#/login")
    dx= Base(driver)
    loc1 = ("id","username")
    loc2 = ("id","password")
    loc3 = ("xpath",".//*[@id='root']/div/div/div[1]/div/div[2]/form/button")

    dx.sendKeys(loc1,"admin")
    dx.sendKeys(loc2,"123456")
    ss=dx.isSelected(loc3)
    print(ss)
    dx.click(loc3)

    # time.sleep(3)
    # xx=dx.isElementExist(loc2)
    # print(xx)



    time.sleep(2)
    driver.quit()

