from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, LoginPageLocators


class TestLogout:
    def test_logout_success(self, driver):
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
            EC.element_to_be_clickable(MainPageLocators.USER_AVATAR)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGOUT_BUTTON)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.LOGIN_BUTTON)
        )
        assert driver.find_element(*MainPageLocators.LOGIN_BUTTON).is_displayed()