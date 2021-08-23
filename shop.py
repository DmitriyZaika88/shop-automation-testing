import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()

# Product page representation

#1
driver.get("http://practice.automationtesting.in/")
time.sleep(0.5)

#2
my_account_menu = driver.find_element_by_partial_link_text('My Account')
my_account_menu.click()
time.sleep(0.5)

login_email = driver.find_element_by_id('username')
login_email.send_keys('dmitriydmz1997@gmail.com')
time.sleep(0.5)

login_password = driver.find_element_by_id('password')
login_password.send_keys('Dmitriy1Dmitriy2')
time.sleep(0.5)

login_btn = driver.find_element_by_css_selector("[value='Login']")
login_btn.click()
time.sleep(0.5)

#3
shopTab = driver.find_element_by_id('menu-item-40')
shopTab.click()
time.sleep(0.5)

#4
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(1)

book_HTML5Forms_link = driver.find_element_by_partial_link_text('HTML5 Forms')
book_HTML5Forms_link.click()
time.sleep(1)

#5
book_name_header = driver.find_element_by_class_name('entry-title')
HTML_5_Forms_text = book_name_header.text
assert HTML_5_Forms_text == "HTML5 Forms" # Проверка присутствия на странице элемента "HTML5 Forms"
print('Элемент', HTML_5_Forms_text, 'найден')


# Number of goods in category

#1
driver.get("http://practice.automationtesting.in/")
time.sleep(0.5)

#2
my_account_menu = driver.find_element_by_partial_link_text('My Account')
my_account_menu.click()
time.sleep(0.5)

login_email = driver.find_element_by_id('username')
login_email.send_keys('dmitriydmz1997@gmail.com')
time.sleep(0.5)

login_password = driver.find_element_by_id('password')
login_password.send_keys('Dmitriy1Dmitriy2')
time.sleep(0.5)

login_btn = driver.find_element_by_css_selector("[value='Login']")
login_btn.click()
time.sleep(0.5)

#3
shopTab = driver.find_element_by_id('menu-item-40')
shopTab.click()
time.sleep(0.5)

#4
driver.get("http://practice.automationtesting.in/shop/")
time.sleep(0.5)

category_html5 = driver.find_element_by_css_selector('.cat-item-19 > a')
category_html5.click()
time.sleep(0.5)

#5
number_of_goods = driver.find_element_by_class_name('type-product')
number_of_goods = number_of_goods.get_attribute("class='type-product'")
if number_of_goods < 3:
    print("Меньше")
if number_of_goods > 3:
    print("Больше")
else:
    print("Равно")



# Sorting of goods

#1
driver.get("http://practice.automationtesting.in/")
time.sleep(0.5)

#2
my_account_menu = driver.find_element_by_partial_link_text('My Account')
my_account_menu.click()
time.sleep(0.5)

login_email = driver.find_element_by_id('username')
login_email.send_keys('dmitriydmz1997@gmail.com')
time.sleep(0.5)

login_password = driver.find_element_by_id('password')
login_password.send_keys('Dmitriy1Dmitriy2')
time.sleep(0.5)

login_btn = driver.find_element_by_css_selector("[value='Login']")
login_btn.click()
time.sleep(0.5)

#3
shopTab = driver.find_element_by_id('menu-item-40')
shopTab.click()
time.sleep(0.5)

#4
default_sorting_check = driver.find_element_by_css_selector('[value="menu_order"]')
default_sorting_check = default_sorting_check.get_attribute('selected')

if default_sorting_check is not None:
    print('Выбрана сортировка по умолчанию')
else:
    print('Сортировка по умолчанию не выбрана')
time.sleep(0.5)

#5
from selenium.webdriver.support.select import Select
sorting = driver.find_element_by_class_name("orderby")
select = Select(sorting)
select.select_by_value("price")
time.sleep(0.5)

#6
default_sorting_check = driver.find_element_by_css_selector('[value="menu_order"]')

#7
default_sorting_check = driver.find_element_by_css_selector('[value="menu_order"]')
default_sorting_check = default_sorting_check.get_attribute('selected')

if default_sorting_check is not None:
    print('Выбрана сортировка по умолчанию')
else:
    print('Сортировка по умолчанию не выбрана')
time.sleep(0.5)


# Visibility and sale of goods

#1
driver.get("http://practice.automationtesting.in/")
time.sleep(0.5)


#2
my_account_menu = driver.find_element_by_partial_link_text('My Account')
my_account_menu.click()
time.sleep(0.5)

login_email = driver.find_element_by_id('username')
login_email.send_keys('dmitriydmz1997@gmail.com')
time.sleep(0.5)

login_password = driver.find_element_by_id('password')
login_password.send_keys('Dmitriy1Dmitriy2')
time.sleep(0.5)

login_btn = driver.find_element_by_css_selector("[value='Login']")
login_btn.click()
time.sleep(0.5)

#3
shopTab = driver.find_element_by_id('menu-item-40')
shopTab.click()
time.sleep(0.5)

#4
book_AndroidQSG_link = driver.find_element_by_partial_link_text('Android Quick Start Guide')
book_AndroidQSG_link.click()
time.sleep(1)

#5 Из-за символа не получается провести проверку. При добавлении переменной с символом тест падает

old_price_check = driver.find_element_by_css_selector('.price > del > span')
old_price_text = old_price_check.text
#old_price_symbol = driver.find_element_by_class_name('woocommerce-Price-currencySymbol')
assert old_price_text == "600.00" # Проверка присутствия на странице элемента "Logout"
print('Элемент', old_price_text, 'найден')

new_price_check = driver.find_element_by_css_selector('.price > ins > span:')
new_price_text = new_price_check.text
#old_price_symbol = driver.find_element_by_class_name('woocommerce-Price-currencySymbol')
assert new_price_text == "450.00" # Проверка присутствия на странице элемента "Logout"
print('Элемент', new_price_text, 'найден')


#6
closeBtn = WebDriverWait(driver,5 ).until(
    EC.invisibility_of_element_located((By.ID, "fullResImage")))

img = driver.find_element_by_class_name('wp-post-image')
img.click()

#7

closeBtn = WebDriverWait(driver,5 ).until(
    EC.invisibility_of_element_located((By.ID, "fullResImage")))

img = driver.find_element_by_class_name('wp-post-image')
img.click()

#8 Здесь баг: is not clickable at point (649, 457). Курсор не попадает в область крестика
closeBtn = WebDriverWait(driver,5 ).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))

cross_btn = driver.find_element_by_class_name('pp_close')
cross_btn.click()

# Basket price check

#1
driver.get("http://practice.automationtesting.in/")
time.sleep(0.5)

#2
shopTab = driver.find_element_by_id('menu-item-40')
shopTab.click()
time.sleep(0.5)

#3
basket_price_btn = driver.find_element_by_css_selector('[data-product_id="182"]')
basket_price_btn.click()
time.sleep(2)

#4
cart_item_num = driver.find_element_by_css_selector('.cartcontents')
cart_item_num_text = cart_item_num.text
assert cart_item_num_text == "1 Item" # Проверка присутствия на странице элемента "1 item"
print('Элемент', cart_item_num_text, 'найден')

cart_item_price = driver.find_element_by_class_name('amount')
cart_item_price_text = cart_item_price.text
assert cart_item_price_text == "₹180.00" # Проверка присутствия на странице элемента "₹180.00"
print('Элемент', cart_item_price_text, 'найден')

#5
cart_link = driver.find_element_by_class_name('wpmenucart-contents')
cart_link.click()

#6
subtotal_text = WebDriverWait(driver,5 ).until(
    EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, "td.Subtotal > .amount"), "180.00"))

#7
total_text = WebDriverWait(driver,5 ).until(
    EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, "td.Total > strong > span.amount"), "189.00"))



# Basket

#1
driver.get("http://practice.automationtesting.in/")
time.sleep(0.5)

#2
shopTab = driver.find_element_by_id('menu-item-40')
shopTab.click()
time.sleep(0.5)

#3
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(1)
add_to_cart_btn_1 = driver.find_element_by_css_selector('[data-product_id="182"]')
add_to_cart_btn_1.click()
time.sleep(1)
add_to_cart_btn_2 = driver.find_element_by_css_selector('[data-product_id="180"]')
add_to_cart_btn_2.click()
time.sleep(1)

#4
cart_link = driver.find_element_by_class_name('wpmenucart-contents')
cart_link.click()
time.sleep(1)

#5
remove_1st_book = driver.find_element_by_css_selector('tbody > tr.cart_item > .product-remove > a')
remove_1st_book.click()
time.sleep(3)

#6
undo_remove_link = driver.find_element_by_partial_link_text('Undo?')
undo_remove_link.click()
time.sleep(2)

#7
quantity_of_goods = driver.find_element_by_css_selector('.quantity > input').clear().setAttribute("value", "3");

#8
upd_basket = driver.find_element_by_css_selector('.coupon > .button')
upd_basket.click()
#9
#10
#11





