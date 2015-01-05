import sys
from pyvirtualdisplay import Display
from selenium import webdriver

USERNAME = '123456789'
PASSWORD = '123456789'


display = Display(visible=0, size=(800, 600))
display.start()

browser = webdriver.Firefox()
browser.get('http://www.1and1.com/domain-names?__lf=Static&linkId=hd.subnav.domainheader.nameregistration#stage')
element = browser.find_element_by_css_selector('.domaincheckbox-input-wrapper input[type=text]')
element.send_keys(sys.argv[1] + "\n")
element = browser.find_element_by_css_selector('#content-bottom button[type=submit]')
element.click()
print browser.title
element = browser.find_element_by_css_selector('a.btn-eh')
element.click()
print browser.title
element = browser.find_element_by_css_selector('#button-ct-btn-additionaldomains-continue-without-selection')
element.click()
print browser.title
element = browser.find_element_by_css_selector('button')
element.click()
print browser.title
element = browser.find_element_by_css_selector('input[name="recurringcustomer.AccountIdentifier"]')
element.send_keys(USERNAME)
element = browser.find_element_by_css_selector('input[name="recurringcustomer.AccountPassword"]')
element.click()
element.send_keys(PASSWORD + "\n")
print browser.title
element = browser.find_element_by_css_selector('span[id="contactdata.UseContactData-contactdata_proxy.unchecked"]')
element.click()
element = browser.find_element_by_css_selector('button[type=submit]')
element.click()
print browser.title
element = browser.find_element_by_css_selector('button[type=submit]')
element.click()
print browser.title
browser.quit()

display.stop()