import os
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException, ElementClickInterceptedException
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

logging.basicConfig(level=logging.ERROR)
Global_Variables = {
    'url': '',
    'applicants': 5,
    'Country': "MX",
    'Email': "",
    'First_name' : 'Pedro',
    'Last_name' : 'Gonzalez',
    'Passport_num' : '123456789',
    'N. Orders': '0',
    'Status': ''
}
def safe_element_click(driver, locator):
    attempts = 0
    max_attempts = 3  
    while attempts < max_attempts:
        try:
            element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
            element.click()
            return True  # Click successful, return True
        except EC.StaleElementReferenceException:
            print(f"StaleElementReferenceException occurred, retrying attempt {attempts + 1}")
            attempts += 1
    print(f"Failed to click element after {max_attempts} attempts")
    return False  

def India_1y_Multiple(data):
    for x in data:
        if x['type'] == 'ULR':
            Global_Variables['url'] = x['value']
        if x['type'] == 'Email':
            Global_Variables['Email'] = x['value']
        if x['type'] == 'Applicants':
            Global_Variables['applicants'] = x['value']
        if x['type'] == 'N. Orders':
            Global_Variables['N. Orders'] = x['value']
        if x['type'] == 'Status':
            Global_Variables['Status'] = x['value']
        chrome_options = Options()
        chrome_options.add_argument('--headless') 
        chrome_options.add_argument('window-size=1920,1080')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--incognito")
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        wait = WebDriverWait(browser, 150, ignored_exceptions=(NoSuchElementException,StaleElementReferenceException))
    try:
        for order in range(int(Global_Variables['N. Orders'])):
            browser.get(Global_Variables['url'] + '/india/apply-now')
            if order == 0:
                nationality = wait.until(EC.element_to_be_clickable((By.NAME, 'general.common_nationality_country')))
                nationality.click()
                nationality_values = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@data-handle='dropdown-general.common_nationality_country']")))
                nationality_values.send_keys(Global_Variables['Country'], Keys.ENTER)
            product = Select(wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@data-handle='dropdown-general.visa_type_id']"))))
            product.select_by_index(1)

            div_continue_btn = wait.until(EC.visibility_of_element_located((By.ID, "btnContinueUnderSection")))
            if div_continue_btn.find_element(By.TAG_NAME, 'button').is_enabled():
                div_continue_btn.find_element(By.TAG_NAME, 'button').click()
            else:
                continue_button_step1 = wait.until(EC.element_to_be_clickable((div_continue_btn.find_element(By.TAG_NAME, 'button'))))
                continue_button_step1.click()

            arrival_date = wait.until(EC.element_to_be_clickable((By.NAME, "general.arrival_date")))
            arrival_date.click()
            print('Got here')
            svg_locator = (By.CSS_SELECTOR, "div.is-right svg")
            day_month = (By.CSS_SELECTOR, "div.day-13")
            safe_element_click(browser, svg_locator)
            safe_element_click(browser, day_month)

            port_arrival = wait.until(EC.element_to_be_clickable((By.NAME, "general.port_of_arrival")))
            port_arrival.click()
            port_arrival_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@data-handle='dropdown-general.port_of_arrival']"))) 
            port_arrival_input.send_keys('del', Keys.ENTER)
            if order == 0:
                email = browser.find_element(By.NAME,"general.email")
                email.send_keys(Global_Variables['Email'])
            continue_btn_sidebar = wait.until(EC.element_to_be_clickable((By.ID, "btnContinueSidebar")))
            continue_btn_sidebar.click()
            
            for x in range(int(Global_Variables['applicants']) - 1):
                add_traveler_div = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-handle='add-traveler']")))
                add_traveler_div2 = add_traveler_div.find_elements(By.TAG_NAME, "div")
                add_traveler_btn = add_traveler_div2[1].find_element(By.TAG_NAME, 'button')
                add_traveler_btn.click()

            for applicant in range(int(Global_Variables['applicants'])):
                first_name = wait.until(EC.visibility_of((browser.find_element(By.NAME, 'applicant.' + str(applicant) + '.first_name'))))
                first_name.send_keys(Global_Variables['First_name'])
                last_name = browser.find_element(By.NAME, "applicant." + str(applicant) + ".last_name")
                last_name.send_keys(Global_Variables['Last_name'])
                gender_select = browser.find_element(By.XPATH, "//select[@data-handle='dropdown-applicant." + str(applicant) + ".gender']")
                gender_select.click()
                gender_select.send_keys('f')
                gender_select.send_keys(Keys.ENTER)
                dob_day = browser.find_element(By.NAME, "applicant." + str(applicant) + ".dob.day")
                dob_day.send_keys('23')
                dob_day.send_keys(Keys.ENTER)
                dob_month = browser.find_element(By.NAME, "applicant." + str(applicant) + ".dob.month")
                dob_month.send_keys('d')
                dob_month.send_keys(Keys.ENTER)
                dob_year = browser.find_element(By.NAME, "applicant." + str(applicant) + ".dob.year")
                dob_year.send_keys('1997')
                dob_year.send_keys(Keys.ENTER)
            wait.until(EC.element_to_be_clickable((continue_btn_sidebar))).click()
            wait.until(EC.element_to_be_clickable((continue_btn_sidebar))).click()
            for user in range(int(Global_Variables['applicants'])):
                passport_num = wait.until(EC.element_to_be_clickable((By.NAME, "applicant."+ str(user) +".passport_num")))
                passport_num.send_keys(Global_Variables['Passport_num'])
                passport_day = browser.find_element(By.NAME, "applicant."+ str(user) +".passport_expiration_date.day")
                passport_day.send_keys('23')
                passport_day.send_keys(Keys.ENTER)
                passport_month = browser.find_element(By.NAME, "applicant."+ str(user) +".passport_expiration_date.month")
                passport_month.send_keys('d')
                passport_month.send_keys(Keys.ENTER)
                passport = browser.find_element(By.NAME, "applicant."+ str(user) +".passport_expiration_date.year")
                passport.send_keys('2032')
                passport.send_keys(Keys.ENTER)
                passport_issue_day = browser.find_element(By.NAME, "applicant."+ str(user) +".passport_issued_date.day")
                passport_issue_day.send_keys('23')
                passport_issue_day.send_keys(Keys.ENTER)
                passport_issue_month = browser.find_element(By.NAME, "applicant."+ str(user) + ".passport_issued_date.month")
                passport_issue_month.send_keys('d')
                passport_issue_month.send_keys(Keys.ENTER)
                passport_issue_year = browser.find_element(By.NAME, "applicant."+ str(user) +".passport_issued_date.year")
                passport_issue_year.send_keys('2020')
                passport_issue_year.send_keys(Keys.ENTER)
                pakistan_parents_select = Select(browser.find_element(By.XPATH, "//select[@data-handle='dropdown-applicant." + str(user) + ".pakistan_parents']"))
                pakistan_parents_select.select_by_index(1)
            wait.until(EC.element_to_be_clickable((continue_btn_sidebar))).click()
            time.sleep(2)
            wait.until(EC.element_to_be_clickable((continue_btn_sidebar))).click()
            print('subscription popup')
            subscription_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-handle="no-subscription"]')))
            subscription_button.click()
            time.sleep(2)
            wait.until(EC.element_to_be_clickable((continue_btn_sidebar))).click()
            try:
                btn_disclaimer = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "btnDisclaimerNext")))
                btn_disclaimer.click()
                wait.until(EC.element_to_be_clickable((By.ID, "btnSubmitPayment"))).click()
                wait.until(EC.element_to_be_clickable((By.ID, "btnCompleteProcess"))).click()
                print('ORDER DONE ' + str(order + 1))
            except TimeoutException: 
                wait.until(EC.element_to_be_clickable((By.ID, "btnSubmitPayment"))).click()
                wait.until(EC.element_to_be_clickable((By.ID, "btnCompleteProcess"))).click()
                print('ORDER DONE ' + str(order + 1))

            ## RECEIVED STATUS
            if Global_Variables['Status'] == 'Received':
                number_input = wait.until(EC.visibility_of_element_located((By.NAME, 'telephone')))
                number_input.send_keys('2343414124')
                continue_btn_post_payment_div = browser.find_element(By.ID, 'btnContinueUnderSection')
                continue_btn_post_payment = continue_btn_post_payment_div.find_element(By.TAG_NAME, 'button')
                continue_btn_post_payment.click()
                receive_texts = Select(browser.find_element(By.XPATH, '//select[@data-handle="dropdown-general.order_notification_signup"]'))
                receive_texts.select_by_index(2)
                continue_btn_post_payment.click()
                for user_post in range(int(Global_Variables['applicants'])):
                    city_birth = wait.until(EC.visibility_of_element_located((By.NAME, 'applicant.' + str(user_post) + '.birth_city')))
                    city_birth.send_keys('Mexico')
                    religion = Select(browser.find_element(By.XPATH, '//select[@data-handle="dropdown-applicant.' + str(user_post) + '.statements_my_arrivalcard"]'))
                    religion.select_by_index(1)
                    home_address = browser.find_element(By.NAME,'applicant.'+ str(user_post) + '.home_address')
                    home_address.send_keys('30 Rockefeller Plaza')
                    time.sleep(3)
                    home_address.send_keys(Keys.ARROW_DOWN)
                    home_address.send_keys(Keys.ENTER)
                    time.sleep(3)
                    continue_btn_post_payment.click()
                    ocupation_div = wait.until(EC.visibility_of_element_located((By.NAME, 'applicant.'+ str(user_post) + '.occupation')))
                    ocupation_div.click()
                    ocupation_input = browser.find_element(By.XPATH, "//input[@data-handle='dropdown-applicant." + str(user_post) + ".occupation']")
                    ocupation_input.send_keys('unemployed')
                    ocupation_input.send_keys(Keys.ENTER)
                    continue_btn_post_payment.click()
                    marital_status = wait.until(EC.presence_of_element_located((By.XPATH, '//select[@data-handle="dropdown-applicant.' + str(user_post) + '.marital_status"]')))
                    marital_status_selector = Select(marital_status)
                    marital_status_selector.select_by_index(1)
                    fathers_name = browser.find_element(By.NAME,'applicant.'+ str(user_post) + '.fathers_name')
                    fathers_name.send_keys('Jose')
                    mother_name = browser.find_element(By.NAME,'applicant.'+ str(user_post) + '.mothers_name')
                    mother_name.send_keys('Rebeca')
                    continue_btn_post_payment.click()

                    wait.until(EC.presence_of_element_located((By.ID,'btn-applicant.'+ str(user_post) + '.passport_photo'))).click()
                    wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@role="dialog"]')))
                    applicant_options = browser.find_element(By.XPATH, "//button[@data-handle='show-upload-options-btn']")
                    browser.execute_script("arguments[0].scrollIntoView();", applicant_options)
                    applicant_options.click()
                    applicant_upload = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@role="dialog"]')))
                    applicant_upload_button = applicant_upload.find_elements(By.TAG_NAME, 'input')
                    file_path = os.path.abspath('automations/Applications/uploads/Applicant-Photo.jpg')
                    applicant_upload_button[0].send_keys(file_path)
                    wait.until(EC.text_to_be_present_in_element((By.XPATH, '//div[@role="dialog"]'),'Successfully uploaded document(s)'))
                    next_document = applicant_upload.find_elements(By.TAG_NAME, 'button')
                    next_document[3].click()

                    wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@role="dialog"]')))
                    passport_options = browser.find_element(By.XPATH, "//button[@data-handle='show-upload-options-btn']")
                    browser.execute_script("arguments[0].scrollIntoView();", passport_options)
                    passport_options.click()
                    passport_upload = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@role="dialog"]')))
                    passport_upload_button = passport_upload.find_elements(By.TAG_NAME, 'input')
                    file_path_passport = os.path.abspath('automations/Applications/uploads/passport.png')
                    passport_upload_button[0].send_keys(file_path_passport)
                    wait.until(EC.text_to_be_present_in_element((By.XPATH, '//div[@role="dialog"]'),'Successfully uploaded document(s)'))
                    next_document = passport_upload.find_element(By.XPATH, '//button[@data-handle="exit-upload-modal-btn"]')
                    next_document.click()
                    time.sleep(3)
                    if user_post + 1 < int(Global_Variables['applicants']):
                        continue_btn_post_payment.click()
                    else:
                        browser.find_element(By.ID, 'btnSubmitApplication').click()
                        wait.until(EC.text_to_be_present_in_element((By.ID, 'app'), 'Download our app'))
            if order == 0:
                browser.get(Global_Variables['url'] + '/account/settings/security')
                password = wait.until(EC.element_to_be_clickable((By.ID, "new_password")))
                password.send_keys('testivisa5!')
                password_repeat = wait.until(EC.element_to_be_clickable((By.ID, "password_repeat")))
                password_repeat.send_keys('testivisa5!') 
                browser.find_element(By.XPATH, '//button[@data-handle="updatePasswordBtn"]').click()
    except NameError as e :
        print(e)
        print(logging.error("An error occurred:" + str(e)))

