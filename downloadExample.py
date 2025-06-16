from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class WebAutomation:

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")

        download_path = os.getcwd()
        prefs = {"download.default_directory": download_path}
        chrome_options.add_experimental_option('prefs', prefs)

        service = Service('drivers/chromedriver.exe')
        self.driver = webdriver.Chrome(options=chrome_options, service=service)

        self.driver.set_page_load_timeout(time_to_wait=10)


    def login(self, username, password):
        self.driver.get('https://demoqa.com/login')
        self.driver.maximize_window()

        userNameField = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        passwordField = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'login')))

        # login
        userNameField.send_keys(username)
        passwordField.send_keys(password)
        login_button.click()

    def fill_form(self):
        elementsButton = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains (text(), 'Elements')]/parent::div")))
        elementsButton.click()

    def download(self):
        downloadModule = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "item-7")))
        downloadModule.click()

        # Form
        downloadButton = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "downloadButton")))
        downloadButton.click()

    def close(self):
        input("Press Enter to Close the Browser: ")
        self.driver.quit()

if __name__ == '__main__':
    webautomation = WebAutomation()
    webautomation.login('aeendale', '1Cb9u1^KYRb!P6QS')
    webautomation.fill_form()
    webautomation.download()
    webautomation.close()