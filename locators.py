from selenium.webdriver.common.by import By


class StellarBurgersLocators:
    # Поле ввода логина
    LOGIN_INPUT_FIELD = (By.XPATH, ".//input[@name='name']")
    # Поле ввода пароля
    PASSWORD_INPUT_FIELD = (By.XPATH, ".//input[@name='Пароль']")
    # кнопка "Войти в аккаунт" на главной странице
    LOGIN_BUTTON_MAIN = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")
    # кнопка "Войти"
    LOGIN_BUTTON_MAIN_FORM = (By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']/button[text()='Войти']")
    # кнопка "Личный кабинет"
    BUTTON_PERSONAL_ACCOUNT = (By.LINK_TEXT, "Личный Кабинет")
    # кнопка в форме регистрации
    LOGIN_BUTTON_FORM_REGISTRATION = (By.LINK_TEXT, "Зарегистрироваться")
    # ссылка "Войти" в форме регистрации
    LOGIN_LINK_FORM_REGISTRATION = (By.LINK_TEXT, "Войти")
    # кнопка в форме восстановления пароля
    LOGIN_BUTTON_FORM_PASSWORD_RECOVERY = (By.LINK_TEXT, "Восстановить пароль")
    # кнопка "Оформить заказ"
    PLACE_AN_ORDER = (By.XPATH, ".//button[text()='Оформить заказ']")
    # Поле с плейсхолдером "Имя" в личном кабинете
    NAME_FIELD = (By.XPATH, ".//label[text()='Имя']")
    # Конструктор
    BUILDER = (By.XPATH, ".//p[text() = 'Конструктор']")
    BUTTON_LOGOUT = (By.XPATH, ".//button[text() = 'Выход']")
    # Заголовок "Вход"
    HEADER_ENTRY = (By.XPATH, ".//h2[text() = 'Вход']")
    # Раздел "Булки"
    SECTION_BREAD = (By.XPATH, ".//span[text() = 'Булки']")
    # Раздел "Соусы"
    SECTION_SAUCES = (By.XPATH, ".//span[text() = 'Соусы']")
    # Раздел "Начинки"
    SECTION_TOPPINGS = (By.XPATH, ".//span[text() = 'Начинки']")
    # Индикатор активности таба "Начинки"
    TAB_INDICATOR_TOPPINGS = (By.XPATH, ".//span[text() = 'Начинки']/parent::*[contains(@class, 'current')]")
    # Заголовок "Начинки"
    TITLE_TOPPINGS = (By.XPATH, ".//h2[text() = 'Начинки']")
    # Индикатор активности таба "Булки"
    TAB_INDICATOR_BREAD = (By.XPATH, ".//span[text() = 'Булки']/parent::*[contains(@class, 'current')]")
    # Заголовок "Булки"
    TITLE_BREAD = (By.XPATH, ".//h2[text() = 'Булки']")
    # Индикатор активности таба "Соусы"
    TAB_INDICATOR_SAUCES = (By.XPATH, ".//span[text() = 'Соусы']/parent::*[contains(@class, 'current')]")
    # Заголовок "Соусы"
    TITLE_SAUCES = (By.XPATH, ".//h2[text() = 'Соусы']")
    # Поле ввода имени в форме регистрации
    REGISTRATION_FORM_NAME = (By.XPATH, ".//fieldset[1]//input")
    # Поле ввода e-mail в форме регистрации
    REGISTRATION_FORM_EMAIL = (By.XPATH, ".//fieldset[2]//input")
    # Поле ввода пароля в форме регистрации
    REGISTRATION_FORM_PASSWORD = (By.XPATH, ".//fieldset[3]//input")
    # Кнопка "Зарегистрироваться"
    REGISTRATION_BUTTON = (By.XPATH, ".//button[text() = 'Зарегистрироваться']")
    # Ошибка ввода пароля в форме регистрации
    PASSWORD_INPUT_ERROR = (By.XPATH, ".//p[@class = 'input__error text_type_main-default']")
    # Форма регистрации
    REGISTRATION_FORM = (By.XPATH, ".//h2[text() = 'Регистрация']")
