import getpass
import requests
import re
from lxml import html
import lxml.etree,json
from selenium import webdriver


browser = webdriver.PhantomJS() # or add to your PATH
browser.set_window_size(1024, 768) # optional
browser.get('http://www.eastbay.com/_-_/keyword-sep1616newreleases+jordan?SID=8698&SID=8698&cm_mmc=Linkshare-_-Deeplink-_-Text-_-Eastbay')

# print browser.title

## set username
header_icon = browser.find_element_by_id("header_account_link")
header_icon.click()

email_input = browser.find_element_by_id("login_email")
email_input.send_keys('mark_penaranda@icloud.com')
passsword_input = browser.find_element_by_id("login_password")
password_input.send_keys('mark171328')

submit_btn = browser.find_element_by_id("login_submit")

submit_btn.submit()

browser.save_screenshot('screen.png')
