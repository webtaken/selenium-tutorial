from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="./chromedriver")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://google.com")

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "gLFyf")))

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()
input_element.send_keys("real python" + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Real Python"))
)
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Real Python")
link.click()

time.sleep(5)
driver.quit()
