import logging, time, re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, ElementClickInterceptedException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
logging.basicConfig(level=logging.ERROR)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)  

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

logging.getLogger().addHandler(console_handler)
Global_Variables = {
    'url': 'https://deploy-20240619--079f7edd.visachinaonline.com',
    'applicants': 5,
    'Country': "MX",
    'Email': "",
    'First_name' : 'Pedro',
    'Last_name' : 'Gonzalez',
    'Passport_num' : '123456789',
    'N. Orders': 0,
    'Order_Numbers': [],
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

def TR_App_P2(data):
    for x in data:
        if x['type'] == 'ULR':
            Global_Variables['url'] = x['value']
        if x['type'] == 'Email':
            Global_Variables['Email'] = x['value']
        if x['type'] == 'Applicants':
            Global_Variables['applicants'] = x['value']
        if x['type'] == 'Status':
            Global_Variables['Status'] = x['value']
        if x['type'] == 'N. Orders':
            Global_Variables['N. Orders'] = x['value']
    
    Global_Variables['Order_Numbers'] = []
    chrome_options = Options()
    chrome_options.add_argument('--headless') 
    chrome_options.add_argument('window-size=1920,1080')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    wait = WebDriverWait(browser, 150, ignored_exceptions=(NoSuchElementException,StaleElementReferenceException))
    try:
        for order in range(int(Global_Variables['N. Orders'])):
            browser.get(Global_Variables['url'] + '/turkey/apply-now')
            if order == 0:
                nationality = wait.until(EC.element_to_be_clickable((By.NAME, 'general.common_nationality_country')))
                nationality.click()
                nationality_values = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@data-handle='dropdown-general.common_nationality_country']")))
                nationality_values.send_keys(Global_Variables['Country'], Keys.ENTER)
            product = Select(wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@data-handle='dropdown-general.visa_type_id']"))))
            product.select_by_index(0)
            div_continue_btn = wait.until(EC.visibility_of_element_located((By.ID, "btnContinueUnderSection")))
            
            div_continue_btn.find_element(By.TAG_NAME, 'button').click() if div_continue_btn.find_element(By.TAG_NAME, 'button').is_enabled() else wait.until(EC.element_to_be_clickable((div_continue_btn.find_element(By.TAG_NAME, 'button')))).click()
            
            arrival_date = wait.until(EC.element_to_be_clickable((By.NAME, "general.arrival_date")))
            arrival_date.click()

            svg_locator = (By.CSS_SELECTOR, "div.is-right svg")
            day_month = (By.CSS_SELECTOR, "div.day-13")
            safe_element_click(browser, svg_locator)
            safe_element_click(browser, day_month)
            if order == 0:
                email = browser.find_element(By.NAME,"general.email")
                email.send_keys(Global_Variables['Email'])
            continue_sidebar = wait.until(EC.visibility_of_element_located((By.ID, "btnContinueSidebar")))
            continue_sidebar.click() if continue_sidebar.is_enabled() else wait.until(EC.element_to_be_clickable((By.ID, "btnContinueSidebar"))).click()
            print('Passed Step 1')
            for x in range(int(Global_Variables['applicants']) - 1):
                add_traveler_div = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-handle='add-traveler']")))
                add_traveler_div2 = add_traveler_div.find_elements(By.TAG_NAME, "div")
                add_traveler_btn = add_traveler_div2[1].find_element(By.TAG_NAME, 'button')
                add_traveler_btn.click()
            
            for applicant in range(int(Global_Variables['applicants'])):
                first_name = wait.until(EC.visibility_of_element_located((By.NAME, 'applicant.' + str(applicant) + '.first_name')))
                first_name.send_keys(Global_Variables['First_name'])
                last_name = wait.until(EC.visibility_of_element_located((By.NAME, "applicant." + str(applicant) + ".last_name"))) 
                last_name.send_keys(Global_Variables['Last_name'])
                gender_select = Select(wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@data-handle='dropdown-applicant." + str(applicant) + ".gender']"))) ) 
                gender_select.select_by_index(0)
                dob_day = wait.until(EC.visibility_of_element_located((By.NAME, "applicant." + str(applicant) + ".dob.day"))) 
                dob_day.send_keys('23')
                dob_day.send_keys(Keys.ENTER)
                dob_month = wait.until(EC.visibility_of_element_located((By.NAME, "applicant." + str(applicant) + ".dob.month")))  
                dob_month.send_keys('d')
                dob_month.send_keys(Keys.ENTER)
                dob_year = wait.until(EC.visibility_of_element_located((By.NAME, "applicant." + str(applicant) + ".dob.year")))
                dob_year.send_keys('1997')
                dob_year.send_keys(Keys.ENTER)
            # step 4
            continue_sidebar.click() if continue_sidebar.is_enabled() else wait.until(EC.element_to_be_clickable((By.ID, "btnContinueSidebar"))).click()
            print('Passed Step 2')
            # step 5
            continue_sidebar.click() if continue_sidebar.is_enabled() else wait.until(EC.element_to_be_clickable((By.ID, "btnContinueSidebar"))).click()
            print('Passed Step 3')
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
            time.sleep(3)
            continue_sidebar.click() if continue_sidebar.is_enabled() else wait.until(EC.element_to_be_clickable((By.ID, "btnContinueSidebar"))).click()
            print('Passed Step 4')
            time.sleep(3)
            continue_sidebar.click() if continue_sidebar.is_enabled() else wait.until(EC.element_to_be_clickable((By.ID, "btnContinueSidebar"))).click()
            print('Passed Step 5')
            time.sleep(3)
            try:
                continue_sidebar.click() if continue_sidebar.is_enabled() else wait.until(EC.element_to_be_clickable((By.ID, "btnContinueSidebar"))).click()
            except ElementClickInterceptedException:
                subscription_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@data-handle="no-subscription"]')))
                subscription_button.click() if subscription_button.is_enabled() else wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-handle="no-subscription"]'))).click()
            print('Passed Step 6')
            time.sleep(3)
            continue_step_6 = (By.ID, "btnContinueSidebar")
            try:
               safe_element_click(browser, continue_step_6) if continue_sidebar.is_enabled() else safe_element_click(browser, continue_step_6)
            except ElementClickInterceptedException:
                subscription_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@data-handle="no-subscription"]')))
                subscription_button.click() if subscription_button.is_enabled() else wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-handle="no-subscription"]'))).click()
            print('Passed Step 7')
            try:
                btn_submit_payment = wait.until(EC.element_to_be_clickable((By.ID, "btnSubmitPayment")))
                btn_submit_payment.click()
            
                btn_complete = wait.until(EC.element_to_be_clickable((By.ID, "btnCompleteProcess")))
                btn_complete.click()
            except ElementClickInterceptedException: 
                btn_disclaimer = wait.until(EC.element_to_be_clickable((By.ID, "btnDisclaimerNext")))
                btn_disclaimer.click()

                btn_submit_payment = wait.until(EC.element_to_be_clickable((By.ID, "btnSubmitPayment")))
                btn_submit_payment.click()

                btn_complete = wait.until(EC.element_to_be_clickable((By.ID, "btnCompleteProcess")))
                btn_complete.click()
            except TimeoutException: 
                btn_disclaimer = wait.until(EC.element_to_be_clickable((By.ID, "btnDisclaimerNext")))
                btn_disclaimer.click()

                btn_submit_payment = wait.until(EC.element_to_be_clickable((By.ID, "btnSubmitPayment")))
                btn_submit_payment.click()

                btn_complete = wait.until(EC.element_to_be_clickable((By.ID, "btnCompleteProcess")))
                btn_complete.click()
            except NoSuchElementException: 
                btn_disclaimer = wait.until(EC.element_to_be_clickable((By.ID, "btnDisclaimerNext")))
                btn_disclaimer.click()

                btn_submit_payment = wait.until(EC.element_to_be_clickable((By.ID, "btnSubmitPayment")))
                btn_submit_payment.click()

                btn_complete = wait.until(EC.element_to_be_clickable((By.ID, "btnCompleteProcess")))
                btn_complete.click()
            print('Passed Step 8')
            wait.until(EC.element_to_be_clickable((By.ID, 'btnDismissAppDownload'))).click()
            order_number = wait.until(EC.visibility_of_element_located((By.ID, 'h1-tag-container')))
            Global_Variables['Order_Numbers'].append(re.findall(r'\d+', order_number.text))
            if order == 0:
                browser.get(Global_Variables['url'] + '/account/settings/security')
                password = wait.until(EC.element_to_be_clickable((By.ID, "new_password")))
                password.send_keys('testivisa5!')
                password_repeat = wait.until(EC.element_to_be_clickable((By.ID, "password_repeat")))
                password_repeat.send_keys('testivisa5!') 
                browser.find_element(By.XPATH, '//button[@data-handle="updatePasswordBtn"]').click()
                wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'swal-button--confirm'))).click()
            print('ORDER ' + str(order))
        ## MIN STATUS
        if Global_Variables['Status'] == 'MIN':
            wait.until(EC.element_to_be_clickable((By.ID, 'loggedInUserContainer-chevron'))).click()
            wait.until(EC.element_to_be_clickable((By.ID, 'btnLogout'))).click()
            browser.get(Global_Variables['url'] + '/admin')
            admin_email = wait.until(EC.element_to_be_clickable((By.ID, 'email_login_input')))
            admin_email.send_keys('david@admin.com')
            wait.until(EC.element_to_be_clickable((By.ID, 'continue_button'))).click()
            admin_password = wait.until(EC.element_to_be_clickable((By.ID, 'password_login_input')))
            admin_password.send_keys('testivisa5!')
            wait.until(EC.element_to_be_clickable((By.ID, 'log_in_button'))).click()
            for order_numbers in (Global_Variables['Order_Numbers']):
                wait.until(EC.element_to_be_clickable((By.XPATH, '//li[@onclick="searchOrderID();"]'))).click()
                order_alert = Alert(browser)
                order_alert.send_keys(order_numbers[0])
                order_alert.accept()
                wait.until(EC.element_to_be_clickable((By.XPATH, '//section[@aria-labelledby="info-title"]'))).click()
                applicants_admin = wait.until(EC.visibility_of_any_elements_located((By.XPATH,'//div[@data-handle="applicant-details"]')))
                time.sleep(2)
                applicants_admin[0].click()
                time.sleep(2)
                table_wraper = browser.find_element(By.XPATH, '//section[@aria-labelledby="info-title"]')
                questions_table = table_wraper.find_element(By.TAG_NAME, 'table')
                first_and_middle_name_row = questions_table.find_elements(By.TAG_NAME, 'tr')
                send_name_min = first_and_middle_name_row[0].find_element(By.XPATH, '//span[@data-handle="min_checkbox_first_name"]')
                time.sleep(2)
                send_name_min.find_element(By.ID, 'Vector').click()
                wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@role="dialog"]')))
                browser.find_element(By.XPATH, '//label[@data-handle="Non-English characters"]').click()
                wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Search a MIN reason"]')))
                browser.find_element(By.ID, 'close').click()
                change_status = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'change-status'))))
                change_status.select_by_index(1)
                wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-handle="minModalYes"]'))).click()
                time.sleep(3)
                wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-handle="submitChangeStatus"]'))).click()
                wait.until_not(EC.visibility_of_element_located((By.XPATH, '//div[@data-vue-component="order-item-editor"]')))
        browser.quit()
        automation_results = {
            'Order_numbers' : Global_Variables['Order_Numbers'],
            'Status' : 'Success',
            'order_status' : Global_Variables['Status'],
            'email' : Global_Variables['Email'],
        }
        return automation_results
    except Exception as e:
        print(e)
        logging.debug('Debug message: %s', e)
        return e