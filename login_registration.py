import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()

#Registration

#1
driver.get("http://practice.automationtesting.in/")
time.sleep(0.5)

#2
my_account_menu = driver.find_element_by_partial_link_text('My Account')
my_account_menu.click()
time.sleep(0.5)

#3
register_email = driver.find_element_by_id('reg_email')
register_email.send_keys('dmitriydmz1997@gmail.com')
time.sleep(3)

#4
register_password = driver.find_element_by_id('reg_password')
register_password.send_keys('Dmitriy1Dmitriy2')
time.sleep(3)

#5
register_btn = driver.find_element_by_css_selector("[value='Register']")
register_btn.click()
time.sleep(0.5)


#Login

#1
driver.get("http://practice.automationtesting.in/")
time.sleep(0.5)

#2
my_account_menu = driver.find_element_by_partial_link_text('My Account')
my_account_menu.click()
time.sleep(0.5)

#3
login_email = driver.find_element_by_id('username')
login_email.send_keys('dmitriydmz1997@gmail.com')
time.sleep(0.5)

#4
login_password = driver.find_element_by_id('password')
login_password.send_keys('Dmitriy1Dmitriy2')
time.sleep(0.5)

#5
login_btn = driver.find_element_by_css_selector("[value='Login']")
login_btn.click()
time.sleep(0.5)

#6
logout_check = driver.find_element_by_class_name('woocommerce-MyAccount-navigation-link--customer-logout')
logout_text = logout_check.text
assert logout_text == "Logout" # Проверка присутствия на странице элемента "Logout"
print('Элемент', logout_text, 'найден')

