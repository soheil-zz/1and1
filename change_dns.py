import os
import sys
import time
from pyvirtualdisplay import Display
from selenium import webdriver

USERNAME = '123456789'
PASSWORD = '123456789'

 
display = Display(visible=0, size=(800, 600))
display.start()
 
browser = webdriver.Firefox()
browser.get('https://www.1and1.com/login?__lf=Static&linkId=hd.nav.login')
element = browser.find_element_by_css_selector('input[name="oaologin.username"]')
element.send_keys(USERNAME)
element = browser.find_element_by_css_selector('input[name="oaologin.password"]')
element.click()
element.send_keys(PASSWORD + "\n")
print browser.title
try:
  element = browser.find_element_by_css_selector('input[name="search.domainname"]')
except:
  element = browser.find_element_by_css_selector('.infobox.contract-selection a')
  element.click()
  element = browser.find_element_by_css_selector('a.core_button_normal')
  element.click()
  element = browser.find_element_by_css_selector('input[name="search.domainname"]')

element.send_keys(sys.argv[1] + "\n")
print browser.title
element = browser.find_element_by_css_selector('.low.marked a')
element.click()
browser.execute_script('document.querySelector(".entry-domainsselfserviceapp a").target=""')
element = browser.find_element_by_css_selector('.entry-domainsselfserviceapp a')
element.click()
time.sleep(30)
element = browser.find_element_by_css_selector('.slick-cell-checkboxsel span')
element.click()
element = browser.find_element_by_css_selector('.type.settings')
element.click()
element = browser.find_element_by_css_selector('label[for="menu_settings_dnsSettings"]')
element.click()
print browser.title
time.sleep(15)
element = browser.find_element_by_css_selector('div[id="dns-edit-ns-custom-option"] a')
element.click()
element = browser.find_element_by_css_selector('div[id="dns-edit-ns-custom"] .selected-item')
element.click()
element = browser.find_element_by_css_selector('div[id="dns-edit-ns-custom"] div[data-value=custom]')
element.click()
element = browser.find_element_by_css_selector('input[name="custom-ns-1"]')
element.send_keys(sys.argv[2])
element = browser.find_element_by_css_selector('input[name="custom-ns-2"]')
element.send_keys(sys.argv[3])
element = browser.find_element_by_css_selector('input[name="custom-ns-3"]')
element.send_keys(sys.argv[4])
element = browser.find_element_by_css_selector('input[name="custom-ns-4"]')
element.send_keys(sys.argv[5])
element = browser.find_element_by_css_selector('.save-changes .button-wrapper.primary')
element.click()
time.sleep(15)
browser.execute_script('document.querySelectorAll("a[class=rain_modal_button]:not([style])")[1].click()')
time.sleep(15)
element = browser.find_element_by_css_selector('.ui-widget-content span[data-title="Update is in progress."]')
browser.quit()
display.stop()

os.system('rm /etc/cron.hourly/' + sys.argv[1])
