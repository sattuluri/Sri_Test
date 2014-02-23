#!/bin/usr/python
import selenium
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.ubuntu.com')
Firstbutton = driver.find_element_by_class_name("first active")
Firstbutton.click()
