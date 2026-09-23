from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Вход и регистрация']")
    PLACE_AD_BUTTON = (By.XPATH, "//button[text()='Разместить объявление']")
    USER_AVATAR = (By.XPATH, "//button[contains(@class, 'circleSmall')]")
    USER_NAME = (By.XPATH, "//h3[text()='User.']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")


class RegistrationPageLocators:
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Нет аккаунта']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    REPEAT_PASSWORD_FIELD = (By.NAME, "submitPassword")
    ERROR_MESSAGE = (By.XPATH, "//span[text()='Ошибка']")


class LoginPageLocators:
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    AUTH_MODAL_TITLE = (By.XPATH, "//h1[text()='Чтобы разместить объявление, авторизуйтесь']")


class AdvertisementPageLocators:
    NAME_FIELD = (By.NAME, "name")
    DESCRIPTION_FIELD = (By.XPATH, "//div[contains(@class, 'textarea_inputDefault')]//textarea[@name='description']")
    PRICE_FIELD = (By.NAME, "price")
    CATEGORY_DROPDOWN = (By.XPATH, "//input[@name='category']/following-sibling::button")
    CITY_DROPDOWN = (By.XPATH, "//input[@name='city']/following-sibling::button")
    CONDITION_NEW = (By.XPATH, "//label[text()='Новый']")
    CONDITION_USED = (By.XPATH, "//label[text()='Б/У']")
    PUBLISH_BUTTON = (By.XPATH, "//button[text()='Опубликовать']")

    @staticmethod
    def category_option(category_name):
        return (By.XPATH, f"//button[.//span[text()='{category_name}']]")

    @staticmethod
    def city_option(city_name):
        return (By.XPATH, f"//button[.//span[text()='{city_name}']]")


class ProfilePageLocators:
    MY_ADS_BLOCK = (
        By.XPATH,
        "//div[contains(@class, 'profilePage_listningBlock')][.//h1[text()='Мои объявления']]"
    )
    MY_ADS_TITLE = (By.XPATH, "//h1[text()='Мои объявления']")