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
    #agregar validacion de carro de compra vacio (se puede valdiar desde el empty de arriba)
    f.mouse_over_linktext("WOMEN")
    driver.find_element(By.XPATH,"(//A[@href='http://automationpractice.com/index.php?id_category=5&controller=category'][text()='T-shirts'])[1]").click()
    f.mouse_over_xpath("//*[@id='center_column']/ul/li/div")
    time.sleep(1)
    driver.find_element(By.XPATH, "//SPAN[text()='Add to cart']").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Proceed to checkout").click()
    #validar que se agrego un producto


def test_add_2nd_item_to_cart():
    f = GlobalFunctions(driver)
    f.mouse_over_linktext("WOMEN")
    driver.find_element(By.XPATH,"(//A[@href='http://automationpractice.com/index.php?id_category=5&controller=category'][text()='T-shirts'])[1]").click()
    f.mouse_over_xpath("//*[@id='center_column']/ul/li/div")
    time.sleep(1)
    driver.find_element(By.XPATH, "//SPAN[text()='Add to cart']").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Proceed to checkout").click()
    quantity = driver.find_element(By.CLASS_NAME, "cart_quantity_input").get_attribute('value')
    assert int(quantity) >= 2
    driver.find_element(By.LINK_TEXT, "Proceed to checkout").click()


# def add_new_address(): #desde el paso 3
#     f = GlobalFunctions(driver)
#     driver.find_element(By.LINK_TEXT, "Add a new address").click()
#     time.sleep(1)
#     f.text_xpath("//INPUT[@id='address1']", "Mi dirección 2", 0.5)
#     f.text_xpath("//INPUT[@id='city']", "Santiago", 0.5)
#     select = Select(driver.find_element(By.ID, "id_state"))
#     select.select_by_visible_text("Alabama")
#     time.sleep(1)
#     f.text_xpath("//INPUT[@id='postcode']", "00000", 0.5)
#     f.text_xpath("//INPUT[@id='phone']", "99999999", 0.5)
#     # f.text_xpath("//INPUT[@id='alias']", "New Address", 0.5)
#     ad = driver.find_element(By.XPATH, "//INPUT[@id='alias']")
#     ad.clear()
#     ad.send_keys("New Address 2")
#     ad.send_keys(Keys.TAB)
#     driver.find_element(By.ID, "submitAddress").click()

def test_edit_address(): # desde el paso 3
    f = GlobalFunctions(driver)
    driver.find_element(By.LINK_TEXT, "Update").click()
    update_address = driver.find_element(By.XPATH, "//INPUT[@id='address1']")
    update_address.clear()
    update_address.send_keys("Dirección modificada")
    f.text_xpath("//INPUT[@id='city']", "Santiago", 0.5)
    select = Select(driver.find_element(By.ID, "id_state"))
    select.select_by_visible_text("Alabama")
    time.sleep(1)
    # f.text_xpath("//INPUT[@id='alias']", "New Address", 0.5)
    ad = driver.find_element(By.XPATH, "//INPUT[@id='alias']")
    ad.clear()
    ad.send_keys("My new updated Address")
    ad.send_keys(Keys.TAB)
    driver.find_element(By.ID, "submitAddress").click()
    # valdiar que se cambió la dirección
    driver.find_element(By.NAME, "processAddress").click()


def test_continue_step_4():
    time.sleep(2)
    driver.find_element(By.XPATH, "//INPUT[@id='cgv']").click()
    driver.find_element(By.NAME, "processCarrier").click()


def test_continue_step_5():
    # valdiar productos de carro de compra
    driver.find_element(By.CLASS_NAME, "bankwire").click()


def test_confirm_order():
    driver.find_element(By.XPATH, "//span[contains(.,'I confirm my order')]").click()


def test_get_order_reference():
    text_box = driver.find_element(By.XPATH, "//div[@class='box']").text
    order_reference = re.findall(r"reference (\w+) in", text_box)
    print(type(order_reference))
    print(order_reference[0])
    print(type(order_reference))



MC;4nt0n3ll4t34m0












# def ir_a_categoria_tshirt_agregar_carro():
#     a = ActionChains(driver) #mover a setup
#     n = driver.find_element(By.LINK_TEXT, "WOMEN")
#     a.move_to_element(n).perform()
#     driver.find_element(By.XPATH, "(//A[@href='http://automationpractice.com/index.php?id_category=5&controller=category'][text()='T-shirts'])[1]").click()
#     driver.find_element(By.XPATH, "//SPAN[text()='Add to cart']").click()
#     driver.find_element(By.XPATH, "(//SPAN)[31]").click()


