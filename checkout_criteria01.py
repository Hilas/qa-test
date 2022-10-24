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
    driver.find_element(By.CLASS_NAME, "login").click()
    f.text_id("email", "stefano.viacava@gmail.com", 0)
    f.text_id("passwd", "123456", 0)
    driver.find_element(By.ID, "SubmitLogin").click()
    if driver.title == "My account - My Store":
        assert True
    else:
        assert False

def test_add_item_to_cart():
    f = GlobalFunctions(driver)
    driver.find_element(By.CLASS_NAME, "shopping_cart").click()
    f.mouse_over_linktext("WOMEN")
    driver.find_element(By.XPATH,"(//A[@href='http://automationpractice.com/index.php?id_category=5&controller=category'][text()='T-shirts'])[1]").click()
    f.mouse_over_xpath("//*[@id='center_column']/ul/li/div")
    time.sleep(1)
    driver.find_element(By.XPATH, "//SPAN[text()='Add to cart']").click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Proceed to checkout").click()

def test_edit_address():
    f = GlobalFunctions(driver)
    driver.find_element(By.LINK_TEXT, "Proceed to checkout").click()
    time.sleep(1)
    address_old = driver.find_element(By.CLASS_NAME, "address_city").text
    driver.find_element(By.LINK_TEXT, "Update").click()
    update_address = driver.find_element(By.XPATH, "//INPUT[@id='address1']")
    update_address.clear()
    update_address.send_keys("Dirección modificada")
    f.text_xpath("//INPUT[@id='city']", "Santiago", 0.5)
    select = Select(driver.find_element(By.ID, "id_state"))
    select.select_by_visible_text("Alabama")
    time.sleep(1)
    ad = driver.find_element(By.XPATH, "//INPUT[@id='alias']")
    ad.clear()
    ad.send_keys("My new updated Address")
    ad.send_keys(Keys.TAB)
    driver.find_element(By.ID, "submitAddress").click()
    address_new = driver.find_element(By.XPATH, "(//LI[@class='address_city address_state_name address_postcode'])[1]").text
    assert address_new != address_old
    print("\nLa Dirección ", address_old, "fue cambiada por:", address_new)
    driver.close()
