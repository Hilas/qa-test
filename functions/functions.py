from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver import ActionChains
import time


class GlobalFunctions():
    def __init__(self, driver):
        self.driver = driver

    def pause(self, code):
        x = input("Escribe Y si quieres continuar: ")
        if x == 'Y':
            code
        else:
            self.driver.close()

    def tiempo(self, timer):
        t = time.sleep(timer)
        return t
    
    def nav(self, url, timer):
        self.driver.get(url)
        t = time.sleep(timer)
        return t

    def text_xpath(self, xpath, text, timer):
        val = self.driver.find_element(By.XPATH, xpath).send_keys(text)
        t = time.sleep(timer)
        return t

    def text_id(self, id, text, timer):
        val = self.driver.find_element(By.ID, id)
        val.clear()
        val.send_keys(text)
        t = time.sleep(timer)
        return t

    def mouse_over_linktext(self, text):
        n = self.driver.find_element(By.LINK_TEXT, text)
        a = ActionChains(self.driver)
        a.move_to_element(n).perform()

    def mouse_over_xpath(self, text):
        n = self.driver.find_element(By.XPATH, text)
        a = ActionChains(self.driver)
        a.move_to_element(n).perform()
