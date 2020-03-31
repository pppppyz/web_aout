#coding = utf-8
import xlrd

class ExcelUtil():
    def __init__(self,excelPath,sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        #获取第一行作为key值
        self.keys = self.table.row_values(0)
        #h获取总行数
        self.rolNum =  self.table.nrows
        #获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rolNum<=1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in range(self.rolNum-1):
                s = {}
                #从第二行取对应的values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j+=1
        return r



if __name__ =="__main__":
    # import os
    # propath =os.path.dirname(os.path.dirname(os.path.relpath(__file__)))
    # filepath =os.path.join(propath,"commomm","datas.xls")
    # print(filepath)
    filepath = "F:\\webz_zidong\\common\\datas.xls"
    sheetName= "Sheet1"
    data = ExcelUtil(filepath,sheetName)
    testdates=data.dict_data()
    print(testdates)