import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from config_oliwia import desired_cap
from locators.fuel_log import FuelLogLocators
from helpers.fuel_log_preconditions import preconditions

input_odometer_text = "190000"
input_fuel_text = "30"
input_liter_text = "7.43"


def test_fuel_log_with_valid_data(preconditions):
    driver = preconditions
    set_odometer(driver)
    set_fuel(driver)
    set_price(driver)
    set_date_fuel_log(driver)
    set_full_tank(driver)
    set_gas_station(driver)
    set_localization(driver)
    check_added_fuel_log(driver)


def set_odometer(driver):
    """Ustawienie licznika"""
    driver.find_element(By.XPATH, FuelLogLocators.button_plus).click()
    driver.find_element(By.XPATH, FuelLogLocators.button_plus)
    set_the_odometer = driver.find_element(By.ID, FuelLogLocators.odometer_set)
    set_the_odometer.click()
    choose_option_odometer = driver.find_element(By.XPATH, FuelLogLocators.odometer_option_licznik)
    choose_option_odometer.click()
    input_odometer = driver.find_element(By.ID, FuelLogLocators.odometer_input)
    input_odometer.send_keys(input_odometer_text)


def set_fuel(driver):
    """Ustawienie paliwa"""
    input_fuel = driver.find_element(By.ID, FuelLogLocators.fuel_amout)
    input_fuel.click()
    input_fuel.send_keys(input_fuel_text)
    set_the_fuel = driver.find_element(By.ID, FuelLogLocators.fuel_type)
    set_the_fuel.click()
    choose_option_fuel = driver.find_element(By.XPATH, FuelLogLocators.fuel_ON_Diesel)
    choose_option_fuel.click()


def set_price(driver):
    """Ustawienie ceny za litr"""
    input_liter = driver.find_element(By.ID, FuelLogLocators.fuel_price_liter)
    input_liter.click()
    input_liter.send_keys(input_liter_text)
    input_total_cost = driver.find_element(By.ID, FuelLogLocators.fuel_price_total_cost)
    assert input_total_cost.text == "222.90"


def set_date_fuel_log(driver):
    """Ustawienie daty tankowania"""
    choose_date = driver.find_element(By.ID, FuelLogLocators.date_choose)
    choose_date.click()
    set_date = driver.find_element(AppiumBy.ACCESSIBILITY_ID, FuelLogLocators.set_date)
    set_date.click()
    click_OK = driver.find_element(By.ID, FuelLogLocators.OK_date)
    click_OK.click()

    choose_time = driver.find_element(By.ID, FuelLogLocators.time_choose)
    choose_time.click()

    driver.find_element(AppiumBy.ACCESSIBILITY_ID, '18').click()
    el0 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '0')
    el5 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '5')

    actions = ActionChains(driver)
    actions.click_and_hold(el0)
    actions.move_to_element_with_offset(el5, 0, 25)
    actions.perform()

    click_OK2 = driver.find_element(By.ID, FuelLogLocators.OK_date2)
    click_OK2.click()

    choose_date = driver.find_element(By.ID, FuelLogLocators.date_choose)

    assert choose_date.text == "2022-06-25"
    assert choose_time.text == "18:03"


def set_full_tank(driver):
    """Ustawienie tankowania do pełna"""
    full_tank_of_gas = driver.find_element(AppiumBy.ID, FuelLogLocators.switch_full).get_attribute("checked")
    switch_click = driver.find_element(AppiumBy.ID, FuelLogLocators.switch_full)
    if full_tank_of_gas == 'true':
        pass
    else:
        switch_click.click()


def set_gas_station(driver):
    """Ustawienie stacji benzynowej"""
    location_choose = driver.find_element(By.ID, FuelLogLocators.button_location)
    location_choose.click()
    nearby = driver.find_element(By.XPATH, FuelLogLocators.button_nearby)
    nearby.click()


def set_localization(driver):
    """Ustawienie geolokalizacji"""
    driver.set_location(54.391048, 18.589788, 0)

    gas_station = driver.find_element(By.XPATH, FuelLogLocators.bp_gas_station)
    gas_station.click()
    gas_station_current = driver.find_element(By.ID, FuelLogLocators.current_gas_station)
    assert gas_station_current.text == "BP"


def check_added_fuel_log(driver):
    """Potwierdzenie dodania wpisu"""
    add_ok = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "OK")
    add_ok.click()

    total_cost = driver.find_element(By.ID, 'com.kajda.fuelio:id/tv_totalcost')
    total_date = driver.find_element(By.ID, 'com.kajda.fuelio:id/tv_date')
    total_odo = driver.find_element(By.ID, 'com.kajda.fuelio:id/tv_totalodo')
    fuel_amount = driver.find_element(By.ID, 'com.kajda.fuelio:id/tv_fuelamount')
    fuel_price = driver.find_element(By.ID, 'com.kajda.fuelio:id/tv_fuelprice')
    consumption = driver.find_element(By.ID, 'com.kajda.fuelio:id/tv_consumption')
    final_location = driver.find_element(By.ID, 'com.kajda.fuelio:id/tv_location')

    assert total_cost.text == '222,90 zł'
    assert total_date.text == '2022-06-25'
    assert total_odo.text == '190 000 km'
    assert fuel_amount.text == '30 l'
    assert fuel_price.text == '7,43 zł/l'
    assert consumption.text == 'Pierwsze pełne tankowanie'
    assert final_location.text == 'BP - Gdańsk'

