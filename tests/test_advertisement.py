import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import (
    MainPageLocators,
    LoginPageLocators,
    AdvertisementPageLocators,
)


class TestAdvertisement:
    def test_create_ad_unauthorized(self, driver):
        driver.get("https://qa-desk.education-services.ru/")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PLACE_AD_BUTTON)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.AUTH_MODAL_TITLE)
        )
        assert driver.find_element(*LoginPageLocators.AUTH_MODAL_TITLE).is_displayed()

    def test_create_ad_authorized(self, driver):
        driver.get("https://qa-desk.education-services.ru/")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)
        ).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_FIELD)
        ).send_keys("vladimirkhoz@gmail.com")
        driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys("212121")
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.USER_AVATAR)
        )

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PLACE_AD_BUTTON)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(AdvertisementPageLocators.NAME_FIELD)
        )

        driver.find_element(*AdvertisementPageLocators.NAME_FIELD).send_keys(
            f"Тестовое объявление {random.randint(1000, 9999)}"
        )

        driver.find_element(*AdvertisementPageLocators.DESCRIPTION_FIELD).send_keys("Описание товара")

        driver.find_element(*AdvertisementPageLocators.PRICE_FIELD).send_keys("1000")

        driver.find_element(*AdvertisementPageLocators.CATEGORY_DROPDOWN).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(AdvertisementPageLocators.category_option("Авто"))
        ).click()

        driver.find_element(*AdvertisementPageLocators.CITY_DROPDOWN).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(AdvertisementPageLocators.city_option("Санкт-Петербург"))
        ).click()

        driver.find_element(*AdvertisementPageLocators.CONDITION_NEW).click()

        driver.find_element(*AdvertisementPageLocators.PUBLISH_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.PLACE_AD_BUTTON)
        )

        assert driver.find_element(*MainPageLocators.PLACE_AD_BUTTON).is_displayed()