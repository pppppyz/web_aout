import unittest
from common.HTMLTestRunner import HTMLTestRunner

casePath = "F:\webz_zidong\\case"
rule = "test*.py"
discover = unittest.defaultTestLoader.discover(start_dir=casePath, pattern=rule)
print(discover)

reportPath = "F:\webz_zidong\\report\\" + "report.html"
fp = open(reportPath, "wb")

runner = HTMLTestRunner(stream=fp,
                        title="报告的title",
                        description="描述你的报告干什么用:",
                        retry = 1)
runner.run(discover)
fp.close()
