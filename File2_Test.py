#!/bin/usr/python
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import sys

for line in range(3):
	a = sys.argv[line]
	#print a
fh = open('Sel_Test.py','w')
fh.write(a)
#for Lines in fh:
#	print Lines
fh.close()
