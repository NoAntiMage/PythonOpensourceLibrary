# demo from https://selenium-python.readthedocs.io/navigating.html
# navigating an element

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("https://www.baidu.com/")
element1 = browser.find_element_by_id("kw")
element2 = browser.find_element_by_name("wd")
element3 = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/span[1]/input")

element1.send_keys('hello world')
element1.send_keys(" and some", Keys.ARROW_DOWN)
element1.clear()
