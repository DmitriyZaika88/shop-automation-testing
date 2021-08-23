import time

from selenium import webdriver
driver = webdriver.Chrome()

#1
driver.get("http://practice.automationtesting.in/")
time.sleep(0.5)

#2
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(0.5)

#3
link_SeleniumRuby = driver.find_element_by_partial_link_text('Selenium Ruby')
link_SeleniumRuby.click()
time.sleep(0.5)

#4
reviews_Tab = driver.find_element_by_class_name('reviews_tab')
reviews_Tab.click()
time.sleep(0.5)

#5
driver.execute_script("window.scrollBy(0, 400);")
time.sleep(1)

rating_Stars = driver.find_element_by_class_name("star-5")
rating_Stars.click()
time.sleep(0.5)

#6
review = driver.find_element_by_id('comment')
review.send_keys('Nice book!')
time.sleep(0.5)

#7
name_Field = driver.find_element_by_id('author')
name_Field.send_keys('Dmitriy')
time.sleep(0.5)

#8
email_Field = driver.find_element_by_id('email')
email_Field.send_keys('dmitriydmz1997@gmail.com')
time.sleep(0.5)

#9
submit_Btn = driver.find_element_by_id('submit')
submit_Btn.click()
time.sleep(0.5)


