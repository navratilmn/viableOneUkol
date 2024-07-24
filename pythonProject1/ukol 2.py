from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

#otevreni baseurl
driver.get("https://v1-web-git-test-viableone.vercel.app/")

#nalezeni stranky kariera a klik
kariera_link = driver.find_element(By.CSS_SELECTOR, "a[href='/kariera']")
kariera_link.click()

#cekani nez se nacte formular
form = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "careerContactForm")))

#scrolovani
ActionChains(driver).scroll_to_element(form).perform()

#nalezeni formulare
parent_elem = driver.find_element(By.ID , "careerContactForm")

#vyplneni jednotlivych poli !chybi pridat soubor!
input_name_surname = parent_elem.find_element(By.NAME, "name")
input_name_surname.send_keys("Alfonz Mucha")

input_email = parent_elem.find_element(By.NAME, "email")
input_email.send_keys("alfonz@gmail.com")

input_phone = parent_elem.find_element(By.NAME, "phone")
input_phone.send_keys("727123456")

input_message = parent_elem.find_element(By.NAME, "message")
input_message.send_keys("test")

#checkbox na potvrzeni
checkbox = driver.find_element(By.CLASS_NAME,"form-check-input")
checkbox.click()

#buton na potvrzeni formulare a klik
button = driver.find_element(By.CSS_SELECTOR, ".btn.ContactForm_contact-form__button__EuaVy.btn.btn-contained")
button.click()

