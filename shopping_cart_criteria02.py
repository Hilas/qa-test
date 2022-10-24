import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from functions.functions import GlobalFunctions
from selenium.webdriver import ActionChains
import re


def setup():
    global driver
    driver = webdriver.Chrome(executable_path="/opt/homebrew/bin/chromedriver")
    f = GlobalFunctions(driver)
    driver.implicitly_wait(1)
    f.nav("http://automationpractice.com", 1)


def test_add_item_to_cart_logged_out():
    f = GlobalFunctions(driver)
    driver.find_element(By.CLASS_NAME, "shopping_cart").click()
    f.mouse_over_linktext("WOMEN")
    driver.find_element(By.XPATH,"(//A[@href='http://automationpractice.com/index.php?id_category=5&controller=category'][text()='T-shirts'])[1]").click()
    f.mouse_over_xpath("//*[@id='center_column']/ul/li/div")
    time.sleep(1)
    driver.find_element(By.XPATH, "//SPAN[text()='Add to cart']").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Proceed to checkout").click()

def test_login():
    f = GlobalFunctions(driver)
    driver.find_element(By.CLASS_NAME, "login").click()
    f.text_id("email", "stefano.viacava@gmail.com", 0)
    f.text_id("passwd", "123456", 0)
    driver.find_element(By.ID, "SubmitLogin").click()
    f.time(0.5)

def test_validate_quantity_cart():
    f = GlobalFunctions(driver)
    driver.find_element(By.XPATH, "(//A[@href='http://automationpractice.com/index.php?controller=order'])[1]").click()
    f.validate_quantity_more_than(1)
    driver.close()