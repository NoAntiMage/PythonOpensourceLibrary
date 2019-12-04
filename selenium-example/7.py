# coding: utf-8
# a demo from https://pypi.org/project/selenium/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("http://www.baidu.com/")
assert "百度一下，你就知道"

elem = browser.find_element_by_id("kw")
elem.send_keys("hello world" + Keys.RETURN)
elem.submit()
elem.quit()
