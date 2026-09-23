import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, RegistrationPageLocators


class TestRegistration:

    def test_registration_success(self, driver):
        driver.get("https://qa-desk.education-services.ru/")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationPageLocators.NO_ACCOUNT_BUTTON)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_FIELD)
        ).send_keys(f"user{random.randint(100000, 999999)}@example.com")
        driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys("Password123")
        driver.find_element(*RegistrationPageLocators.REPEAT_PASSWORD_FIELD).send_keys("Password123")
        driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.USER_NAME)
        )
        assert driver.find_element(*MainPageLocators.USER_NAME).is_displayed()

    def test_registration_invalid_email(self, driver):
        driver.get("https://qa-desk.education-services.ru/")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationPageLocators.NO_ACCOUNT_BUTTON)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_FIELD)
        ).send_keys("invalid_email")
        driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys("Password123")
        driver.find_element(*RegistrationPageLocators.REPEAT_PASSWORD_FIELD).send_keys("Password123")
        driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationPageLocators.ERROR_MESSAGE)
        )
        assert driver.find_element(*RegistrationPageLocators.ERROR_MESSAGE).is_displayed()

    def test_registration_existing_user(self, driver):
        driver.get("https://qa-desk.education-services.ru/")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationPageLocators.NO_ACCOUNT_BUTTON)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_FIELD)
        ).send_keys("vladimirkhoz@gmail.com")
        driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys("212121")
        driver.find_element(*RegistrationPageLocators.REPEAT_PASSWORD_FIELD).send_keys("212121")
        driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationPageLocators.ERROR_MESSAGE)
        )
        assert driver.find_element(*RegistrationPageLocators.ERROR_MESSAGE).is_displayed()