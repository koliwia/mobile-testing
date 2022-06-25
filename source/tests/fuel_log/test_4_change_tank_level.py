from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config_oliwia import desired_cap
from locators.fuel_log import FuelLogLocators
from helpers.fuel_log_preconditions import existing_log
from locators.tank_level_container import TankLevelLocators

tank_capacity_text = "30"


def test_change_tank_level(existing_log):
    driver = existing_log
    edit_log(driver)
    change_level(driver)
    set_tank_capacity(driver)
    set_seekbar(driver)
    check_tank_level(driver)


def edit_log(driver):
    """Edycja wpisu"""
    kebab_menu = driver.find_element(By.ID, FuelLogLocators.kebab_menu)
    kebab_menu.click()
    edit_button = driver.find_element(By.XPATH, FuelLogLocators.edit_log)
    edit_button.click()


def change_level(driver):
    """ Zmiana tankowania na "Znam poziom paliwa w baku" """
    full_tank_of_gas = driver.find_element(AppiumBy.ID, FuelLogLocators.switch_full).get_attribute("checked")
    switch_click = driver.find_element(AppiumBy.ID, FuelLogLocators.switch_full)
    if full_tank_of_gas == 'true':
        switch_click.click()
    else:
        print("Something is wrong!")
    switch_tank_level_known = driver.find_element(By.ID, 'com.kajda.fuelio:id/tankLevelisKnown')
    switch_tank_level_known.click()
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "com.kajda.fuelio:id/root_container")))
    assert driver.find_element(By.ID, 'com.kajda.fuelio:id/radio_after').is_displayed()


def set_tank_capacity(driver):
    """Ustawienie pojemności baku"""
    tank_capacity = driver.find_element(By.ID, TankLevelLocators.tank_level_capacity)
    tank_capacity.click()
    tank_capacity.send_keys(tank_capacity_text)


def set_seekbar(driver):
    """Ustawienie paska"""
    seekbar = driver.find_element(By.ID, 'com.kajda.fuelio:id/seekBarFuel')
    seekbar_height = seekbar.size.get('height')
    seekbar_width = seekbar.size.get('width')
    ### klikam na lewy górny róg elementu (0,0) , przesuwam do: max width i połowy wysokości
    actions = ActionChains(driver).click_and_hold(seekbar).move_to_element_with_offset(seekbar, seekbar_width,
                                                                                       seekbar_height / 2).perform()
    driver.find_element(By.ID, 'android:id/button1').click()
    add_ok = driver.find_element(By.ID, 'com.kajda.fuelio:id/send')
    add_ok.click()


def check_tank_level(driver):
    """Czy wyświetla się poziom paliwa w baku?"""
    tank_level = driver.find_element(By.ID, 'com.kajda.fuelio:id/tv_tank_lvl')
    assert tank_level.text == '30.0 l (100.0%)'
