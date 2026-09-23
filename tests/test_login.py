from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, LoginPageLocators


class TestLogin:
    def test_login_success(self, driver):
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
            EC.presence_of_element_located(MainPageLocators.USER_NAME)
        )
        assert driver.find_element(*MainPageLocators.USER_NAME).is_displayed()