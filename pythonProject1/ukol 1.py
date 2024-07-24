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

#buton na potvrzeni formulare a klik
button = driver.find_element(By.CSS_SELECTOR, ".btn.ContactForm_contact-form__button__EuaVy.btn.btn-contained")
button.click()

#pockani na ukazani alertu
WebDriverWait(driver,2)

#lokalizace alertu
alert = driver.find_element(By.CSS_SELECTOR,".invalid-feedback.m-0.fs-7")

print(alert.is_displayed())