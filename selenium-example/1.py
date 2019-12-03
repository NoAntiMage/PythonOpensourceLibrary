from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("http://bing.com/")
search_field = driver.find_element_by_name("q")
search_field.clear()
search_field.send_keys("phone")

products = driver.find_element_by_xpath("//h2[@class='product-name]/a")

print("Found" + str(len(products)) + " products:")

for product in products:
    print(product.text)

driver.quit()
