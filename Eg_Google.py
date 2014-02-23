#!/bin/usr/python
import selenium
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

webelement = webdriver.Firefox()
webelement.implicitly_wait(10)
webelement.get("http://www.google.com")
print webelement.title
print webelement.get_location()
Searchelement = webelement.find_element_by_name("q")
Searchelement.send_keys("Cheese")
Searchelement.submit()
#try:
#	WebDriverWait(webelement,10).until(EC.title_contains("cheese"))
#	print driver.title
#except:
#	print("Webpage waited for 10 sec")
#finally:
#	webelement.quit()

#from selenium.webdriver.common.by import By
#element = driver.find_element(by=By.ID, value="coolestWidgetEvah")



labels = webelement.find_elements_by_tag_name("label")
inputs = webelement.execute_script(
    "var labels = arguments[0], inputs = []; for (var i=0; i < labels.length; i++){" +
    "inputs.push(document.getElementById(labels[i].getAttribute('for'))); } return inputs;", labels)
#User Input - Filling In Forms

select = driver.find_element_by_tag_name("select")
allOptions = select.find_elements_by_tag_name("option")
for option in allOptions:
    print "Value is: " + option.get_attribute("value")
    option.click()

#Switch to windows()

for handle in driver.window_handles:
    driver.switch_to_window(handle)
#Switching the frames

driver.switch_to_frame("frameName")

it’s possible to access subframes by separating the path with a dot, and you can specify the frame by its index too. That is:

driver.switch_to_frame("frameName.0.child")


list_id[]

def read_txt()
id1 = open("id.txt","w")
for id in id1:
id = id.rstrip()




