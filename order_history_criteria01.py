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
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Proceed to checkout").click()
    f.time(1)
    driver.find_element(By.LINK_TEXT, "Proceed to checkout").click()
    driver.find_element(By.NAME, "processAddress").click()


def test_continue_step_4():
    time.sleep(2)
    driver.find_element(By.XPATH, "//INPUT[@id='cgv']").click()
    driver.find_element(By.NAME, "processCarrier").click()


def test_continue_step_5():
    driver.find_element(By.CLASS_NAME, "bankwire").click()


def test_confirm_order_and_validate_history():
    driver.find_element(By.XPATH, "//span[contains(.,'I confirm my order')]").click()
    text_box = driver.find_element(By.XPATH, "//div[@class='box']").text
    order_reference = re.findall(r"reference (\w+) in", text_box)
    driver.find_element(By.CLASS_NAME, "header_user_info").click()
    driver.find_element(By.XPATH, "//SPAN[text()='Order history and details']").click()
    order_reference_list = driver.find_element(By.XPATH, "(//a[contains(@class,'color-myaccount')])[1]").text
    assert order_reference[0] == order_reference_list
    print("Se creo la orden con código de referencia", order_reference[0], "y se valida en el listado de historial de ordenes.")


