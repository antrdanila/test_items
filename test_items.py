from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

# Пожалуйста, прочтите README
# В README описано, как не засорить ПК и сэкономить нервы
# В README описаны все шаги для корректной проверки
def test_basket_button(browser):
    browser.get(link)
    button = browser.find_element(By.XPATH, "//*[@id='add_to_basket_form']/button")
    assert button.text