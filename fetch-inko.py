#!/usr/bin/env python2

import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Firefox()

if not os.path.exists('inko'):
	os.mkdir('inko')

browser.get('http://unro.minjust.ru/NKOReports.aspx?request_type=inko')
WebDriverWait(browser, 30).until(lambda d: d.find_element_by_xpath("//select[@id='filter_dt_from']/option[@value='']"))
browser.find_element_by_xpath("//select[@id='filter_dt_from']/option[@value='']").click()

WebDriverWait(browser, 30).until(lambda d: d.find_element_by_xpath("//img[@id='b_refresh']"))
browser.find_element_by_xpath("//img[@id='b_refresh']").click()

WebDriverWait(browser, 30).until(lambda d: d.find_element_by_xpath("//td[@class='pdg_count' and contains(text(), '500')]"))
browser.find_element_by_xpath("//td[@class='pdg_count' and contains(text(), '500')]").click()

for n in range(1, 1000):
	WebDriverWait(browser, 300).until(lambda d: d.find_element_by_xpath("//*[@id='pdg_next']"))
	open('inko/page%03u.html' % n, 'wb').write(browser.page_source.encode('windows-1251'))
	try:
		browser.find_element_by_xpath("//*[@id='pdg_next' and @dsbl='n']").click()
	except NoSuchElementException:
		break

browser.close()

