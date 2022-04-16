import time
from selenium.webdriver.common.by import By


link ="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_is_visible(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element(By.CSS_SELECTOR, value='.btn-add-to-basket')
    assert button, 'Кнопка добавления товара отсутвует'