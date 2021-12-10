#Importing all dependecies
import time
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

#Path of chromedriver
#locate your file for chromedriver.exe
PATH = "C:\\Users\hidru\\OneDrive\\Documents\\COde\\OnlineTyping-Bot\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#website we link to
driver.get("https://onlinetyping.org/typing-test/typing-test-wpm-2minute.php")

timz = driver.find_element_by_id('timer')
resp = driver.find_element_by_id('word-section').text
main = driver.find_element_by_class_name('current-word').text

while timz.text>'0:0':
    pyautogui.typewrite(driver.find_element_by_class_name('current-word').text, interval=0.08)
    pyautogui.press('space')
    driver.implicitly_wait(1)
