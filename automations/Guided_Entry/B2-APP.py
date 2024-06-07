from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options
Global_Variables = {
    'url': 'https://deploy-20240610--73a8cdd1.visachinaonline.com',
    'Country': "MX",
    'Email': "test@mailinator.com",
    'First_name' : 'Pedro',
    'Last_name' : 'Gonzalez',
    'Passport_num' : '123456789'   
}
def B1_B2():
    ## Open Ivisa page with selenium
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run Chrome in headless mode
    browser = webdriver.Chrome(options=chrome_options)
    for x in range(1):
        
        wait = WebDriverWait(browser, 150)
        browser.get(Global_Variables.url + '/usa/apply-now')
        if(x == 0):
            nationality = wait.until(EC.element_to_be_clickable((By.NAME, 'general.common_nationality_country')))
            nationality.click()
            #pyautogui.write(Global_Variables.country)
            #pyautogui.hotkey('enter')
        product = browser.find_element(By.XPATH, "//div[@data-ivisa-slug='visa_type_id']")
        product.click()
        #pyautogui.hotkey('down')
        #pyautogui.hotkey('enter')
        time.sleep(4)
        continue_btn = browser.find_element(By.ID, "btnContinueUnderSection")
        continue_btn.click()
        ## Step 2
        destination_input = wait.until(EC.element_to_be_clickable((By.NAME, "general.arrival_date")))
        destination_input.click()
        wait.until(EC.visibility_of(browser.find_element(By.XPATH, "//div[@placement='bottom-start']")))
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.is-right"))).click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.day-13"))).click()
        departure_input = wait.until(EC.element_to_be_clickable((By.NAME, "general.departure_date")))
        departure_input.click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.is-right"))).click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.day-18"))).click()
        if x == 0:
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

        phone = browser.find_element(By.NAME, "telephone")
        phone.send_keys('6141212321')
        time.sleep(2)
        continue_btn_sidebar.click()
        # step 4
        applying_from_country = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@data-handle='dropdown-applicant.0.living_country_residence']")))
        applying_from_country.click()
        #pyautogui.hotkey('enter')
        time.sleep(2)
        continue_btn_sidebar.click()
        # step 5
        time.sleep(2)
        continue_btn_sidebar.click()
        passport_num = wait.until(EC.element_to_be_clickable((By.NAME, "applicant.0.passport_num")))
        passport_num.send_keys(Global_Variables.passport_num)
        time.sleep(1)
        passport_day = browser.find_element(By.NAME, "applicant.0.passport_expiration_date.day")
        passport_day.send_keys('23')
        passport_day.send_keys(Keys.ENTER)
        time.sleep(1)
        passport_month = browser.find_element(By.NAME, "applicant.0.passport_expiration_date.month")
        passport_month.send_keys('d')
        passport_month.send_keys(Keys.ENTER)
        time.sleep(1)
        passport = browser.find_element(By.NAME, "applicant.0.passport_expiration_date.year")
        passport.send_keys('2032')
        passport.send_keys(Keys.ENTER)
        time.sleep(3)
        ## 
        passport_issue_day = browser.find_element(By.NAME, "applicant.0.passport_issued_date.day")
        passport_issue_day.send_keys('23')
        passport_issue_day.send_keys(Keys.ENTER)
        time.sleep(1)
        passport_issue_month = browser.find_element(By.NAME, "applicant.0.passport_issued_date.month")
        passport_issue_month.send_keys('d')
        passport_issue_month.send_keys(Keys.ENTER)
        time.sleep(1)
        passport_issue_year = browser.find_element(By.NAME, "applicant.0.passport_issued_date.year")
        passport_issue_year.send_keys('2020')
        passport_issue_year.send_keys(Keys.ENTER)
        time.sleep(1)
        applying_from_country = browser.find_element(By.XPATH, "//select[@data-handle='dropdown-applicant.0.which_statement_applies']")
        applying_from_country.click()
        #pyautogui.hotkey('enter')
        time.sleep(3)
        continue_btn_sidebar.click()
        time.sleep(3)
        appointment_location = browser.find_element(By.NAME, "applicant.0.appointment_location_id")
        appointment_location.click()
        #pyautogui.hotkey('down')
        #pyautogui.hotkey('enter')
        time.sleep(2)
        continue_btn_sidebar.click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@data-handle='no-subscription']"))).click()
        time.sleep(3)
        continue_btn_sidebar.click()
        time.sleep(3)
        continue_btn_sidebar.click()
        time.sleep(3)
        if browser.find_elements(By.ID, "btnDisclaimerNext"):
            browser.find_element(By.ID, "btnDisclaimerNext").click()
        wait.until(EC.element_to_be_clickable((By.ID, "btnSubmitPayment"))).click()
        wait.until(EC.element_to_be_clickable((By.ID, "btnCompleteProcess"))).click()
        #Post payment
        wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@data-handle='dropdown-general.type_of_contact']"))).click()
        #pyautogui.hotkey('down')
        #pyautogui.hotkey('enter')
        time.sleep(3)
        contact_name = browser.find_element(By.NAME, "general.contact_first_name")
        contact_name.send_keys('Pedrito')
        contact_last_name = browser.find_element(By.NAME, "general.contact_last_name")
        contact_last_name.send_keys('Gonzalez')
        contact_relationship = browser.find_element(By.XPATH, "//select[@data-handle='dropdown-general.destination_contact_relationship']")
        contact_relationship.click()
        #pyautogui.hotkey('down')
        #pyautogui.hotkey('enter')
        contact_adress = browser.find_element(By.NAME, "general.contact_address")
        contact_adress.click()
        contact_adress.send_keys('1150 Broadway')
        #pyautogui.hotkey('down')
        #pyautogui.hotkey('enter')
        contact_phone = browser.find_element(By.XPATH, "//div[@data-flip='false']")
        contact_phone.click()
        #pyautogui.hotkey('down')
        #pyautogui.hotkey('enter')
        phone_postpayment = browser.find_element(By.NAME, "telephone")
        phone_postpayment.send_keys('6141212321')
        time.sleep(10)
