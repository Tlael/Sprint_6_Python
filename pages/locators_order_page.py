from selenium.webdriver.common.by import By

LOGO_SCOOTER = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
LOGO_YANDEX = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')

BUTTON_ORDER_IN_HEADER = (By.CLASS_NAME, 'Button_Button__ra12g')
BUTTON_ORDER_IN_PAGE = (By.XPATH, '//div/div/div[4]/div[2]/div[5]/button')
FIELD_NAME = (By.XPATH, "//div/div[2]/div[2]/div[1]/input")
FIELD_SURNAME = (By.XPATH, '//div/div[2]/div[2]/div[2]/input')
FIELD_ADDRESS = (By.XPATH, '//div/div[2]/div[2]/div[3]/input')
FIELD_SUBWAY = (By.XPATH, '//div/div[2]/div[2]/div[4]/div/div/input')
LIST_SUBWAY = (By.CLASS_NAME, 'select-search__select')
FIELD_PHONE = (By.XPATH, '//div/div[2]/div[2]/div[5]/input')

BUTTON_NEXT = (By.XPATH, '//div/div[2]/div[3]/button')

FIELD_TIME = (By.XPATH, '//div/div[2]/div[2]/div[1]/div/div/input')
CALENDAR = (By.CLASS_NAME, 'react-datepicker__month-container')
DROPDOWN_RENTS = (By.XPATH, '//div/div[2]/div[2]/div[2]/div[1]')
TIME_RENTS = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[3]')

CHECKBOX_COLOR_BLACK = (By.XPATH, '//*[@id="black"]')
CHECKBOX_COLOR_GRAY = (By.XPATH, '//*[@id="grey"]')
FIELD_COMMENT = (By.XPATH, '//div/div[2]/div[2]/div[4]/input')
BUTTON_ORDER = (By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/button[2]')

BUTTON_YES = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/div[2]/button[2]')
VIEW_STATUS = (By.XPATH, '/html/body/div/div/div[2]/div[5]/div[2]/button')
MESSAGE_ORDER = 'Посмотреть статус'