#!/usr/bin/env python2

import os
from selenium import webdriver

browser = webdriver.Firefox()

if not os.path.exists('nko'):
	os.mkdir('nko')

browser.get('http://unro.minjust.ru/NKOReports.aspx?request_type=nko')
open('nko/page000.html', 'wb').write(browser.page_source.encode('windows-1251'))

browser.find_element_by_id("pdg_next").click()

open('nko/page001.html', 'wb').write(browser.page_source.encode('windows-1251'))

browser.close()

