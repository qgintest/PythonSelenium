from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

service = Service('drivers/chromedriver.exe')
driver = webdriver.Chrome(options=chrome_options, service=service)
driver.get('https://demoqa.com/login')

userNameField = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
passwordField = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'login')))

userNameField.send_keys("aeendale")
passwordField.send_keys("1Cb9u1^KYRb!P6QS")
login_button.click()

input("Press Enter to Close the Browser: ")
driver.quit()
