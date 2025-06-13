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
driver.set_page_load_timeout(time_to_wait=10)
driver.get('https://demoqa.com/login')
driver.maximize_window()

userNameField = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
passwordField = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'login')))

# login
userNameField.send_keys("aeendale")
passwordField.send_keys("1Cb9u1^KYRb!P6QS")
login_button.click()


# Elements and Text Box
elementsButton = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains (text(), 'Elements')]/parent::div")))
elementsButton.click()

textBox = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains (text(), 'Text Box')]")))
textBox.click()

# Form
fullNameFieldBox = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "userName")))
emailFieldBox = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "userEmail")))
currentAddressFieldBox = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "currentAddress")))
permanentAddressFieldBox = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "permanentAddress")))
submitButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "submit")))





fullNameFieldBox.send_keys("name")
emailFieldBox.send_keys("email")
currentAddressFieldBox.send_keys("address")
permanentAddressFieldBox.send_keys("address-permanent")
submitButton.click()




input("Press Enter to Close the Browser: ")
driver.quit()
