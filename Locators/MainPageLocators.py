from selenium.webdriver.common.by import By


class MainPageLocators:
    BUTTON_COOKIES = (By.ID, "rcc-confirm-button")  # кнопка подтвержения куки
    LOGO_YANDEX = (By.XPATH, ".//img[@alt='Yandex']")  # логотип Яндекс
    BUTTON_HEADER_ORDER = (By.XPATH, ".//button[@class='Button_Button__ra12g']")  # кнопка заказать вверху страницы
    BUTTON_FINISH_ORDER = (By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']")  # кнопка заказать внизу страницы
    ORDER_STATUS = (By.XPATH, ".//button[text()='Статус заказа']")  # кнопка статус заказа
    PRICE_QUESTION = (By.ID, 'accordion__heading-0')  # Сколько это стоит? И как оплатить?
    QUANTITY_QUESTION = (By.ID, 'accordion__heading-1')  # Хочу сразу несколько самокатов! Так можно?
    RENT_QUESTION = (By.ID, 'accordion__heading-2')  # Как рассчитывается время аренды?
    TODAY_ORDER = (By.ID, 'accordion__heading-3')  # Можно ли заказать самокат прямо на сегодня?
    PROLONGATION_QUESTION = (By.ID, 'accordion__heading-4')  # Можно ли продлить заказ или вернуть самокат раньше?
    CHARGER_QUESTION = (By.ID, 'accordion__heading-5')  # Вы привозите зарядку вместе с самокатом?
    CANCEL_QUESTION = (By.ID, 'accordion__heading-6')  # Можно ли отменить заказ?
    TAKE_QUESTION = (By.ID, 'accordion__heading-7')  # Я жизу за МКАДом, привезёте?
    OPEN_ANSWER = (By.XPATH, ".//div[@role='region' and not(@hidden)]/p")  # развернутый ответ
