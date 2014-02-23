#!usr/bin/python
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select

webelement = webdriver.Firefox()
webelement.get("http://www.ubuntu.com")

Commu_link = webelement.find_element_by_partial_link_text("Server")
Commu_link.click()
print webelement.get_location()
#for option in Commu_link.find_element_by_tag_name("li"):
#	if option.text ==option.select_by_index("1") :
#		option.click()
#		break

#webelements = Commu_link.find_element_by_tag_name("li")
#print webelement.title
#webelement.switch_to_default_content()
#elements = Select(Commu_link)
#elements.select_by_value("1")


