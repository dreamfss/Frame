# 登录模块
import time
# import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_framework.src.utils.config import Config, DRIVER_PATH, DATA_PATH
# from Test_framework.src.utils.log import logger
from Test_framework.src.utils.file_reader import ExcelReader


class login(object):
    URL = Config().get('URL')
    excel = DATA_PATH + '\TestLogin.xlsx'
    locator_button = (By.XPATH, Config().get('loginxpath'))
    phone = (By.XPATH, Config().get('phone'))
    Username = (By.ID, Config().get('Username'))
    password = (By.XPATH, Config().get('password'))
    login_button = (By.XPATH, Config().get('login_button'))
    quit = (By.XPATH, Config().get('quit'))
    driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
    driver.maximize_window()
    driver.get(URL)

    # def __init__(self):
    #     self.driver = login.driver
    #     # self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
    #     self.driver.maximize_window()
    #     self.driver.get(self.URL)


    # driver = ''
    # def __init__(self):
    #     self.driver = driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
    #     self.driver.maximize_window()
    #     self.driver.get(self.URL)
    #     return self.driver

    def test_search(self):
        datas = ExcelReader(self.excel).data
        self.driver.find_element(*self.locator_button).click()
        time.sleep(3)
        self.driver.find_element(*self.phone).clear()
        self.driver.find_element(*self.phone).send_keys(datas[2]['username'])
        self.driver.find_element(*self.password).clear()
        self.driver.find_element(*self.password).send_keys(datas[2]['password'])
        time.sleep(2)
        self.driver.find_element(*self.login_button).click()
        time.sleep(2)