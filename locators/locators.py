from selenium.webdriver.common.by import By

class Locators:
    #form register
    INPUT_NAME = (By.XPATH, "//fieldset[1][@class='Auth_fieldset__1QzWN mb-6']/div/div/input[@class='text input__textfield text_type_main-default']") #Поле Имя
    INPUT_LOGIN = (By.XPATH, "//fieldset[2][@class='Auth_fieldset__1QzWN mb-6']/div/div/input[@class='text input__textfield text_type_main-default']") # Поле "Email"
    INPUT_PASSWORD = (By.XPATH, "//input[@name='Пароль']")  # Поле "Пароль"
    BUTTON_REGISTER = (By.XPATH, "//button[text()='Зарегистрироваться']") #Кнопка "Зарегистрироваться"
    LABEL_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")  # ошибка при регистрации

    #main page
    HEADER_PAGE = (By.XPATH, "//a[@class='AppHeader_header__link__3D_hX AppHeader_header__link_active__1IkJo']") # Заголовок страницы
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']") #Кнопка "Конструктор"
    BUTTON_LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']/a") #Кнопка burger
    HEADER_MAKE_BURGER = (By.XPATH, "//h1[text()='Соберите бургер']")  # header "Собери бургер"

    #personal account
    BUTTON_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']") #Кнопка "Личный кабинет"
    LINK_PROFILE = (By.XPATH, "//a[text()='Профиль']") #ссылка "Профиль" в личном кабинете
    BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выход']")  # Кнопка "Выход"

    #form login
    INPUT_EMAIL_LOGIN = (By.XPATH, "//input[@name='name']") #Поле "Email"
    BUTTON_LOGIN = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']") # Кнопка «Войти»
    LABEL_ENTER = (By.XPATH, "//h2[text()='Вход']")  # h2 'Вход'

    #button login
    BUTTON_LOGIN_RESTORE = (By.XPATH, "//a[@class='Auth_link__1fOlj']")  # кнопка войти - форма восстановления пароля
    BUTTON_REGISTER_LOGIN = (By.XPATH, "//a[text()='Зарегистрироваться']") #Кнопка "Зарегистрироваться" под формой входа
    BUTTON_RESTORE = (By.XPATH, "//a[text()='Восстановить пароль']") #Кнопка "Восстановить пароль" под формой входа
    BUTTON_LOGIN_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']") #Кнопка "Войти в аккаунт" на главной
    LABEL_ENTER_REGISTER = (By.XPATH, "//a[text()='Войти']")  #кнопка войти на странице регистрации

    #tabs navigations
    BUTTON_BUNS = (By.XPATH, "//span[text()='Булки']") #Кнопка "Булки"
    BUTTON_SAUCE = (By.XPATH, "//span[text()='Соусы']") #Кнопка "Соусы"
    BUTTON_FILLING = (By.XPATH, "//span[text()='Начинки']") #Кнопка "Начинки"
    HEADER_BUNS = (By.XPATH, "//h2[text()='Булки']") #h2 булки
    HEADER_FILLINGS = (By.XPATH, "//h2[text()='Начинки']") #h2 начинки
    HEADER_SAUCES = (By.XPATH, "//h2[text()='Соусы']") #h2 соусы

    #доступ при авторизации
    BUTTON_ORDER = (By.XPATH, "//button[text()='Оформить заказ']") #кнопка 'Оформить заказ'


