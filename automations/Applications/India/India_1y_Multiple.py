from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, pyautogui, automations.Global_Variables as Global_Variables

def India_1y_Multiple():
    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, 60)
    ## Open Ivisa page with selenium
    browser.get(Global_Variables.url + '/india/apply-now')
    nationality = wait.until(EC.element_to_be_clickable((By.NAME, 'general.common_nationality_country')))
    nationality.click()
    pyautogui.write(Global_Variables.country)
    pyautogui.hotkey('enter')
    product = browser.find_element(By.XPATH, "//div[@data-ivisa-slug='visa_type_id']")
    product.click()
    pyautogui.hotkey('down')
    pyautogui.hotkey('enter')
    time.sleep(2)
    continue_btn = browser.find_element(By.ID, "btnContinueUnderSection")
    continue_btn.click()
    ## Step 2
    destination_input = wait.until(EC.element_to_be_clickable((By.NAME, "general.arrival_date")))
    destination_input.click()
    wait.until(EC.visibility_of(browser.find_element(By.CLASS_NAME, "vc-weeks")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.is-right"))).click()
    time.sleep(1)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.day-13"))).click()
    port_arrival = browser.find_element(By.NAME, "general.port_of_arrival")
    port_arrival.click()
    pyautogui.hotkey('down')
    pyautogui.hotkey('enter')
    email = browser.find_element(By.NAME,"general.email")
    email.send_keys(Global_Variables.email_txt)
    time.sleep(2)
    continue_btn_sidebar = browser.find_element(By.ID, "btnContinueSidebar")
    continue_btn_sidebar.click()
    ## Step 3
    first_name = wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.first_name')))
    first_name.send_keys(Global_Variables.first_name_txt)
    last_name = browser.find_element(By.NAME, "applicant.0.last_name")
    last_name.send_keys(Global_Variables.last_name_txt)
    gender_select = browser.find_element(By.XPATH, "//select[@data-handle='dropdown-applicant.0.gender']")
    gender_select.click()
    gender_select.send_keys('f')
    gender_select.send_keys(Keys.ENTER)

    dob_day = browser.find_element(By.NAME, "applicant.0.dob.day")
    dob_day.send_keys('23')
    dob_day.send_keys(Keys.ENTER)
    dob_month = browser.find_element(By.NAME, "applicant.0.dob.month")
    dob_month.send_keys('d')
    dob_month.send_keys(Keys.ENTER)

    dob_year = browser.find_element(By.NAME, "applicant.0.dob.year")
    dob_year.send_keys('1997')
    dob_year.send_keys(Keys.ENTER)
    time.sleep(2)
    continue_btn_sidebar.click()
    time.sleep(8)
    browser.quit()
