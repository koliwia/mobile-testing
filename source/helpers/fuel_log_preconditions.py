import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from config_oliwia import desired_cap
from locators.fuel_log import FuelLogLocators
from locators.start_page import StartLocators
from locators.menu_options import MenuOptionsLocators
from locators.preconditions_fuel_log import PreconditionsFuelLog

""" Warunki wstępne """


@pytest.fixture()
def preconditions():
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

    driver.find_element(By.ID, StartLocators.button_skip).click()
    driver.find_element(By.XPATH, MenuOptionsLocators.button_menu).click()
    driver.find_element(By.ID, MenuOptionsLocators.button_cars).click()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, PreconditionsFuelLog.preconditions_button_plus).click()
    driver.find_element(By.ID, PreconditionsFuelLog.preconditions_button_fuel_type).click()
    driver.find_element(By.XPATH, PreconditionsFuelLog.preconditions_button_diesel).click()
    driver.find_element(By.ID, PreconditionsFuelLog.preconditions_button_send).click()
    driver.find_element(By.XPATH, MenuOptionsLocators.button_menu).click()
    driver.find_element(By.ID, MenuOptionsLocators.button_fuel_log).click()

    yield driver

    driver.quit()


@pytest.fixture()
def existing_log():
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

    driver.find_element(By.ID, StartLocators.button_skip).click()
    driver.find_element(By.XPATH, MenuOptionsLocators.button_menu).click()
    driver.find_element(By.ID, MenuOptionsLocators.button_cars).click()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, PreconditionsFuelLog.preconditions_button_plus).click()
    driver.find_element(By.ID, PreconditionsFuelLog.preconditions_button_fuel_type).click()
    driver.find_element(By.XPATH, PreconditionsFuelLog.preconditions_button_diesel).click()
    driver.find_element(By.ID, PreconditionsFuelLog.preconditions_button_send).click()
    driver.find_element(By.XPATH, MenuOptionsLocators.button_menu).click()
    driver.find_element(By.ID, MenuOptionsLocators.button_fuel_log).click()
    driver.find_element(By.XPATH, FuelLogLocators.button_plus).click()
    driver.find_element(By.XPATH, FuelLogLocators.button_plus)
    set_odometer = driver.find_element(By.ID, FuelLogLocators.odometer_set)
    set_odometer.click()
    choose_option_odometer = driver.find_element(By.XPATH, FuelLogLocators.odometer_option_licznik)
    choose_option_odometer.click()
    input_odometer = driver.find_element(By.ID, FuelLogLocators.odometer_input)
    input_odometer.send_keys("200000")
    input_fuel = driver.find_element(By.ID, FuelLogLocators.fuel_amout)
    input_fuel.click()
    input_fuel.send_keys("25")
    add_ok = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "OK")
    add_ok.click()

    yield driver

    driver.quit()
