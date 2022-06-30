from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

# Перед запуском выберите подходящий язык: 
# ar ca cs da de el es fi fr it ko nl pl pt pt-br ro ru sk uk zh-hans en-gb

def test_link_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert button, 'Button is not found'