import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('https://www.vlaanderenkiest.be/verkiezingen2012/#/gemeente/uitslagen')

selenium.click("id=subnav_gemeente_10000")

browser.quit()
