from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from config_oliwia import desired_cap
from locators.fuel_log import FuelLogLocators
from locators.tank_level_container import TankLevelLocators
from helpers.fuel_log_preconditions import preconditions

input_odometer_text = "190900"
input_fuel_text = "25"
input_liter_text = "7.40"
input_hour_text = "19"
input_minute_text = "00"


def test_fuel_log_with_invalid_data(preconditions):
    driver = preconditions
    set_invalid_odometer(driver)
    set_fuel(driver)
    set_price_per_liter(driver)
    set_invalid_date(driver)
    check_visibility_of_odometer(driver)


def set_invalid_odometer(driver):
    """Ustawienie licznika"""
    driver.find_element(By.XPATH, FuelLogLocators.button_plus).click()
    set_odometer = driver.find_element(By.ID, FuelLogLocators.odometer_set)
    set_odometer.click()
    choose_option_odometer = driver.find_element(By.XPATH, FuelLogLocators.odometer_option_licznik)
    choose_option_odometer.click()
    input_odometer = driver.find_element(By.ID, FuelLogLocators.odometer_input)
    input_odometer.send_keys(input_odometer_text)


def set_fuel(driver):
    """Ustawienie paliwa"""
    input_fuel = driver.find_element(By.ID, FuelLogLocators.fuel_amout)
    input_fuel.click()
    input_fuel.send_keys(input_fuel_text)
    set_my_fuel = driver.find_element(By.ID, FuelLogLocators.fuel_type)
    set_my_fuel.click()
    choose_option_fuel = driver.find_element(By.XPATH, FuelLogLocators.fuel_ON_Diesel)
    choose_option_fuel.click()


def set_price_per_liter(driver):
    """Ustawienie ceny za litr"""
    input_liter = driver.find_element(By.ID, FuelLogLocators.fuel_price_liter)
    input_liter.click()
    input_liter.send_keys(input_liter_text)
    input_total_cost = driver.find_element(By.ID, FuelLogLocators.fuel_price_total_cost)
    assert input_total_cost.text == "185.00"


def set_invalid_date(driver):
    """Ustawienie niepoprawnej daty tankowania"""
    choose_date = driver.find_element(By.ID, FuelLogLocators.date_choose)
    choose_date.click()
    driver.find_element(By.ID, 'android:id/next').click()
    driver.find_element(By.XPATH, '//android.view.View[@text="16"]').click()
    click_OK = driver.find_element(By.ID, FuelLogLocators.OK_date)
    click_OK.click()
    choose_time = driver.find_element(By.ID, FuelLogLocators.time_choose)
    choose_time.click()
    set_manual_time = driver.find_element(By.ID, 'android:id/toggle_mode')
    set_manual_time.click()
    input_hour = driver.find_element(By.ID, FuelLogLocators.input_hour)
    input_hour.click()
    input_hour.send_keys(input_hour_text)
    input_minute = driver.find_element(By.ID, FuelLogLocators.input_minutes)
    input_minute.click()
    input_minute.send_keys(input_minute_text)
    click_ok2 = driver.find_element(By.ID, FuelLogLocators.OK_date2)
    click_ok2.click()
    add_ok = driver.find_element(By.ID, 'com.kajda.fuelio:id/send')
    add_ok.click()


def check_visibility_of_odometer(driver):
    """Czy pole do wpisania licznika jest dalej widoczne?"""
    assert driver.find_element(By.ID, FuelLogLocators.odometer_set).is_displayed()
    driver.quit()
