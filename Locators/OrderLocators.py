from selenium.webdriver.common.by import By


class UserDataLocators:
    LOGO_SCOOTER = (By.XPATH, ".//img[@alt='Scooter']")  # логотип Самокат
    NAME_INPUT = (By.XPATH, ".//input[@placeholder='* Имя']")  # поле ввода имени заказчика
    SURNAME_INPUT = (By.XPATH, ".//input[@placeholder='* Фамилия']")  # поле ввода фамилии заказчика
    ADDRESS_INPUT = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")  # поле ввода адреса доставки
    UNDEGROUND_INPUT = (By.XPATH, ".//input[@placeholder='* Станция метро']")  # поле выбора станции метро
    UNDEGROUND_STATION_1 = (By.XPATH, ".//*[@data-index='4' and @data-value='5']")  # выбранная станция Красносельская
    UNDEGROUND_STATION_2 = (By.XPATH, ".//*[@data-index='3' and @data-value='4']")  # выбранная станция Сокольники
    PHONE_INPUT = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")  # поле ввода телефона
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")  # кнопка далее


class OrderDataLocators:
    DATE_FIELD = (By.XPATH, ".//div[@class='react-datepicker__input-container']")  # поле даты достаки
    DATE_INPUT = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")  # поле ввода даты
    DATE_IN_CALENDAR = (By.CLASS_NAME, "react-datepicker__day react-datepicker__day--010") # указание в календаре
    RENT_CLICK = (By.CLASS_NAME, "App_App__15LM-")  # переход для выбора срока аренды
    RENT_PERIOD_INPUT=(By.XPATH,".//div[@class='Dropdown-placeholder']")  # поле ввода периода аренды
    RENT_PERIOD_1_DAY = (By.XPATH, ".//div[@class='Dropdown-option'][1]")  # период 1 сутки
    RENT_PERIOD_5_DAYS = (By.XPATH, ".//div[@class='Dropdown-option'][5]")  # период 5 суток
    COLOR_CHOICE_BLACK = (By.XPATH, ".//label[@for='black']")  # выбор цвета самоката -  черный
    COLOR_CHOICE_GREY = (By.XPATH, ".//label[@for='grey']")  # выбор цвета самоката - серый
    COMMENT_FOR_COURIER = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")  # поле комментарий
    MAKE_ORDER_BUTTON = (
    By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']") # кнопка заказать
    ACCEPT_WINDOW = (By.CLASS_NAME, "Order_Modal__YZ-d3")  # окно подтверждения заказа
    YES_ORDER_BUTTON = (By.XPATH, ".//button[text()='Да']")  # кнопка Да
    MAKED_ORDER_WINDOW = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")  # окно информации о процессе заказа
    VIEW_STATUS_BUTTON = (By.XPATH, ".//button[text()='Посмотреть статус']")  # кнопка посмотреть статус
