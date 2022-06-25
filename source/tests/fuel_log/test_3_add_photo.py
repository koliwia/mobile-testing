from appium import webdriver
from selenium.webdriver.common.by import By
from config_oliwia import desired_cap
from locators.fuel_log import FuelLogLocators
from locators.photos_container import PhotoLocators
from helpers.fuel_log_preconditions import existing_log


def test_add_photo(existing_log):
    driver = existing_log
    scroll(driver)
    choose_photos(driver)
    check_added_photo(driver)


def scroll(driver):
    driver.find_element(By.ID, FuelLogLocators.existing_log_click).click()
    """Scrollowanie do sekcji"""
    driver.swipe(100, 700, 100, 100)


def choose_photos(driver):
    """Dodanie zdjęcia"""
    add_photo = driver.find_element(By.ID, PhotoLocators.add_photo_button)
    add_photo.click()
    add_gallery = driver.find_element(By.XPATH, PhotoLocators.add_from_gallery)
    add_gallery.click()
    choose_gallery_option = driver.find_element(By.XPATH, PhotoLocators.gallery_option)
    choose_gallery_option.click()

    choose_photo = driver.find_element(By.XPATH, PhotoLocators.add_photo)
    choose_photo.click()


def check_added_photo(driver):
    """Czy obrazek się dodał?"""
    assert driver.find_element(By.ID, 'com.kajda.fuelio:id/image').is_displayed()

    add_ok = driver.find_element(By.ID, 'com.kajda.fuelio:id/send')
    add_ok.click()

    assert driver.find_element(By.ID, 'com.kajda.fuelio:id/tv_picture').is_displayed()
