# coding = utf-8
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_framework.src.utils.config import Config, DRIVER_PATH, DATA_PATH
from Test_framework.src.utils.login import LoGin
from Test_framework.src.utils.log import logger
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import random
# from Test_framework.src.utils.login import login
# from Test_framework.src.utils.file_reader import ExcelReader
# from Test_framework.src.utils.HTMLTestRunner import HTMLTestRunner


class Test_Order(unittest.TestCase):
    # 页面元素定位（获取Config中配置）
    search_goods = Config().get('search_goods')  # 搜索商品
    search = (By.XPATH, Config().get('search'))  # 搜索栏
    add_shop_cat = (By.XPATH, Config().get('add_shop_cat'))  #加入购物车
    search_button = (By.XPATH, Config().get('search_button'))  #搜索按钮
    purchase_quantity = (By.XPATH, Config().get('purchase_quantity'))  #购买数量
    increase = (By.XPATH, Config().get('increase')) #数量箭头

    @classmethod
    def sub_setUp(cls):
        # 调用登录模块中driver
        cls.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        cls.driver.maximize_window()
        cls.driver.get(LoGin.URL)

    def sub_tearDown(self):
        # 关闭游览器、命令框
        self.driver.quit()

    def test_search(self):
        try:
            self.sub_setUp()  # 调用sub_setUp方法
            p = LoGin(self.driver)
            p.test_search()
            time.sleep(2)
            self.driver.find_element(*self.search).clear()  # 清空搜索栏
            self.driver.find_element(*self.search).send_keys(Test_Order.search_goods)  #输入文字
            self.driver.find_element(*self.search_button).click()  #点击搜索按钮
            WebDriverWait(self.driver, 10).until(lambda driver:  #查询加入购物车按钮
                                                 self.driver.find_element(*self.add_shop_cat))
            above = self.driver.find_element(*self.add_shop_cat)  #定位加入购物车元素位置
            ActionChains(self.driver).move_to_element(above).click().perform()  #待元素显示，点击元素
            WebDriverWait(self.driver, 10).until(lambda driver:  # 查询加入购物车按钮
                                                 self.driver.find_element(*self.purchase_quantity))
            p = self.driver.find_element(*self.purchase_quantity)
            value = int(p.get_attribute("value"))
            print(type(value))
            f = random.randint(1, 10)
            print(type(f))
            for i in range(f):
                if f > value:
                    self.driver.find_element(*self.increase).click()
            print(3)
            time.sleep(3)
            logger.info('搜索成功')  # 登录成功日志
            self.sub_tearDown()  # 调用退出方法
        except Exception as msg:
            # 代码执行错误时，打印图片
            nowTime = time.strftime("%Y.%m.%d.%H.%M.%S")+".test_003_order"  # 图片名称格式
            # print(type(nowTime))
            self.driver.get_screenshot_as_file(
                "D:\\TestCase\\Hypweb.Frame\\Test_framework\\log\\%s.png" % nowTime)  # 截屏图片
            # print(type(msg))
            age = "test_003_login:"
            logger.info("%s：%s" % (age, msg))
            self.sub_tearDown()  # 调用退出方法


if __name__ == '__main__':
    unittest.main()
