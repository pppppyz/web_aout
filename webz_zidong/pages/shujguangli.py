from selenium import webdriver
from common.base import Base
from selenium.webdriver.support import expected_conditions






class  DataGl(Base):
    #登录页面
    loc1 = ("id","username")
    loc2 = ("id","password")
    loc3 = ("xpath",".//*[@id='root']/div/div/div[1]/div/div[2]/form/button")

    #数据管理
    loc_sj = ("xpath",".//*[@id='root']/div/div/section/aside/div[1]/div/div[1]/ul/li[3]/div")
    loc_jb =("xpath",".//*[@id='data$Menu']/li[1]/a")
    loc_hm=("xpath",".//*[@id='reportedTelcode']")
    loc_select = ("xpath",".//*[@id='content']/form/div/div[1]/div[3]/button")
    locss= ("xpath",".//*[@id='content']/form/div/div[2]/div/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[3]")




    def login(self,user= "admin",pws="123456"):
        self.driver.get("http://192.168.0.60/#/login")
        self.sendKeys(self.loc1,user)
        self.sendKeys(self.loc2,pws)
        self.click(self.loc3)


    def ju_bao(self):
        self.click(self.loc_sj)
        self.click(self.loc_jb)
        self.sendKeys(self.loc_hm,"106943792557570077")
        self.click(self.loc_select)
        ss=self.text(self.locss)
        return ss
        print(ss)

     # def text_L(self):
     #     is





if __name__=="__main__":
    driver=webdriver.Chrome()
    #
    data= DataGl(driver)
    data.login()
    # data.ju_bao()
    # if 106943792557570077==ss:




    driver.quit()