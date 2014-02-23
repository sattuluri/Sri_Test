#!bin/usr/python
import selenium
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.gmail.com")
checkbox = driver.find_element_by_id("PersistentCookie")
get_value(checkbox) 
