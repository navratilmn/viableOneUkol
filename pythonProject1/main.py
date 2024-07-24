from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://v1-web-git-test-viableone.vercel.app/")

kariera_link = driver.find_element(By.CSS_SELECTOR, "a[href='/kariera']")
kariera_link.click()


form = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "careerContactForm")))

ActionChains(driver).scroll_to_element(form).perform()


button = driver.find_element(By.CSS_SELECTOR, ".btn.ContactForm_contact-form__button__EuaVy.btn.btn-contained")
button.click()


#ukol 2

parent_elem = driver.find_element(By.ID , "careerContactForm")

input_name_surname = parent_elem.find_element(By.NAME, "name")
input_name_surname.send_keys("Alfonz Mucha")

input_email = parent_elem.find_element(By.NAME, "email")
input_email.send_keys("alfonz@gmail.com")

input_phone = parent_elem.find_element(By.NAME, "phone")
input_phone.send_keys("727123456")

input_message = parent_elem.find_element(By.NAME, "message")
input_message.send_keys("test")


