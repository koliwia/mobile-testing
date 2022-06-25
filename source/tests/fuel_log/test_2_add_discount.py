from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from config_oliwia import desired_cap
from locators.discount_container import DiscountLocators
from locators.fuel_log import FuelLogLocators
from helpers.fuel_log_preconditions import existing_log
from selenium.webdriver.support import expected_conditions as EC

price_discount_text = "20"


def test_add_discount(existing_log):
    driver = existing_log
    scroll(driver)
    set_discount(driver)
    check_added_discount(driver)


def scroll(driver):
    """Scrollowanie do sekcji"""
    driver.find_element(By.ID, FuelLogLocators.existing_log_click).click()
    driver.swipe(100, 700, 100, 100)


def set_discount(driver):
    """Ustawienie rabatu"""
    driver.find_element(By.ID, DiscountLocators.button_discount_click).click()
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "com.kajda.fuelio:id/tv_title")))
    discount_yes = driver.find_element(By.ID, 'com.kajda.fuelio:id/radio_yes')
    discount_yes.click()

    add_note = driver.find_element(By.ID, DiscountLocators.switch_add_note).get_attribute("checked")
    switch_click = driver.find_element(By.ID, DiscountLocators.switch_add_note)
    if add_note == 'false':
        switch_click.click()
    else:
        pass

    price_discount = driver.find_element(By.ID, DiscountLocators.button_total_discount)
    price_discount.click()
    price_discount.send_keys(price_discount_text)

    driver.find_element(By.XPATH, DiscountLocators.save_button).click()

    add_ok = driver.find_element(By.ID, 'com.kajda.fuelio:id/send')
    add_ok.click()


def check_added_discount(driver):
    total_odo = driver.find_element(By.ID, 'com.kajda.fuelio:id/tv_totalodo')
    fuel_amount = driver.find_element(By.ID, 'com.kajda.fuelio:id/tv_fuelamount')
    discount_note = driver.find_element(By.ID, 'com.kajda.fuelio:id/tv_note')

    assert total_odo.text == '200 000 km'
    assert fuel_amount.text == '25 l'
    assert discount_note.text == 'Rabat: 20,00 zł'
