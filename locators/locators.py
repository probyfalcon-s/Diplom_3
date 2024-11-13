from selenium.webdriver.common.by import By

class Locators:
    #form register/restore_password
    BUTTON_RECOVER_PASSWORD = (By.XPATH, "//a[text()='Восстановить пароль']") #Кнопка "Восстановить пароль" под формой входа
    INPUT_EMAIL = (By.XPATH, "//input[@name='name']")  # Поле "Email"
    BUTTON_SUBMIT_RECOVERY = (By.XPATH, "//button[text()='Восстановить']") #кнопка восстановить в востановление пароля
    INPUT_PASSWORD = (By.XPATH, "//input[@name='Введите новый пароль']") #поле пароль в восстановление пароля
    INPUT_CODE = (By.XPATH, "//input[@name='name']") #поле код из письма
    BUTTON_SAVE = (By.XPATH, "//button[text()='Сохранить']") #кнопка сохранить в восстановление пароля
    INPUT_ACVIVE = (By.XPATH, "//div[@class='input_status_code'") #видимость пароля
    #-----------
    INPUT_NAME = (By.XPATH, "//fieldset[1][@class='Auth_fieldset__1QzWN mb-6']/div/div/input[@class='text input__textfield text_type_main-default']") #Поле Имя
    INPUT_LOGIN = (By.XPATH, "//fieldset[2][@class='Auth_fieldset__1QzWN mb-6']/div/div/input[@class='text input__textfield text_type_main-default']") # Поле "Email"
    INPUT_PASSWORD_LOGIN = (By.XPATH, "//input[@name='Пароль']")  # Поле "Пароль"
    BUTTON_REGISTER = (By.XPATH, "//button[text()='Зарегистрироваться']") #Кнопка "Зарегистрироваться"
    LABEL_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")  #ошибка при регистрации

    #personal account
    BUTTON_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']") #Кнопка "Личный кабинет"
    LINK_PROFILE = (By.XPATH, "//a[text()='Профиль']") #ссылка "Профиль" в личном кабинете
    BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выход']")  # Кнопка "Выход"
    SECTION_ORDER_HISTORY = (By.XPATH, "//a[text()='История заказов']")  #кнопка история заказов
    BUTTON_LOGIN = (By.XPATH, "//button[text()='Выход']")  # Кнопка "Войти"

    #main page/constructor
    HEADER_PAGE = (By.XPATH, "//a[@class='AppHeader_header__link__3D_hX AppHeader_header__link_active__1IkJo']") # Заголовок страницы
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']") #Кнопка "Конструктор"
    BUTTON_LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']/a") #Кнопка burger
    HEADER_MAKE_BURGER = (By.XPATH, "//h1[text()='Соберите бургер']")  #header "Собери бургер"
    BUTTON_ORDER_FEED = (By.XPATH, "//p[text()='Лента Заказов']")  #Кнопка "Лента Заказов"
    INGREDIENT_ITEM = (By.XPATH, "//a[@class='OrderHistory_link__1iNby']") #пункт заказа
    INGREDIENT_DETAILS_MODAL = (By.XPATH, "//div[@class='Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']") #модальное окно пункт заказа
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']") #кнопка закрытия модуля
    BUTTON_ADD_TO_ORDER = (By.XPATH, "//a[@class='BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8']") #добавление товара
    TARGET_ELEMENT = (By.XPATH, "//div[@class='constructor-element constructor-element_pos_top']") #DragnDrop поле
    INGREDIENT_COUNTER = (By.XPATH, "//div[@class='counter_counter__ZNLkj counter_default__28sqi']") #counter заказа
    BUTTON_CHECKOUT = (By.XPATH, "//div[@class='counter_counter__ZNLkj counter_default__28sqi']") #кнопка оформить заказ
    ORDER_CONFIRMATION_MESSAGE = (By.XPATH, "//p[text()='идентификатор заказа']']") #кнопка оформить заказ

    #form login

    BUTTON_LOGIN = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']") # Кнопка «Войти»
    LABEL_ENTER = (By.XPATH, "//h2[text()='Вход']")  # h2 'Вход'

    #button login
    BUTTON_LOGIN_RESTORE = (By.XPATH, "//a[@class='Auth_link__1fOlj']")  # кнопка войти - форма восстановления пароля
    BUTTON_REGISTER_LOGIN = (By.XPATH, "//a[text()='Зарегистрироваться']") #Кнопка "Зарегистрироваться" под формой входа

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


