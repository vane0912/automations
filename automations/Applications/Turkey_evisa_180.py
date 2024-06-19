import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

logging.basicConfig(level=logging.ERROR)
Global_Variables = {
    'url': '',
    'applicants': 5,
    'Country': "MX",
    'Email': "",
    'First_name' : 'Pedro',
    'Last_name' : 'Gonzalez',
    'Passport_num' : '123456789',
    'N. Orders': 0  
}

def TR_App_P2(data):
    for x in data:
        if x['type'] == 'ULR':
            Global_Variables['url'] = x['value']
        if x['type'] == 'Email':
            Global_Variables['Email'] = x['value']
        if x['type'] == 'Applicants':
            Global_Variables['applicants'] = x['value']
        if x['type'] == 'N. Orders':
            Global_Variables['N. Orders'] = x['value']
    print('Running')
    chrome_options = Options()
    chrome_options.add_argument('--headless') 
    chrome_options.add_argument('window-size=1920,1080')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome(ChromeDriverManager(version='114.0.5735.90').install(), options=chrome_options)
    print('Running')
    try:
        wait = WebDriverWait(browser, 150)
        for order in range(int(Global_Variables['N. Orders'])):
            browser.get(Global_Variables['url'] + '/turkey/apply-now')
            print('Running')
            if order == 0:
                print('Running')
                nationality = wait.until(EC.element_to_be_clickable((By.NAME, 'general.common_nationality_country')))
                nationality.click()
                print('Running')
                nationality_values = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@data-handle='dropdown-general.common_nationality_country']")))
                nationality_values.send_keys(Global_Variables['Country'], Keys.ENTER)
                print('Running')
                
            product = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@data-handle='dropdown-general.visa_type_id']")))
            product.click()
            product_type = product.find_elements(By.TAG_NAME, 'option')
            product_type[0].click()
            time.sleep(2)
            div_continue_btn = browser.find_element(By.ID, "btnContinueUnderSection")
            continue_btn = div_continue_btn.find_element(By.TAG_NAME, 'button')
            continue_btn.click()
            print('Step 1 Done')
            ## Step 2
            destination_input = wait.until(EC.element_to_be_clickable((By.NAME, "general.arrival_date")))
            destination_input.click()
            wait.until(EC.visibility_of(browser.find_element(By.XPATH, "//div[@placement='bottom-start']")))
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.is-right"))).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.day-13"))).click()
            if order == 0:
                email = browser.find_element(By.NAME,"general.email")
                email.send_keys(Global_Variables['Email'])
            time.sleep(2)
            continue_btn_sidebar = browser.find_element(By.ID, "btnContinueSidebar")
            continue_btn_sidebar.click()
            time.sleep(3)
            print('Step 3 Done')
            for x in range(int(Global_Variables['applicants']) - 1):
                add_traveler_div = browser.find_element(By.XPATH, "//div[@data-handle='add-traveler']")
                add_traveler_div2 = add_traveler_div.find_elements(By.TAG_NAME, "div")
                add_traveler_btn = add_traveler_div2[1].find_element(By.TAG_NAME, 'button')
                add_traveler_btn.click()
            for applicant in range(int(Global_Variables['applicants'])):
            ## Step 3
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
            # step 4
            time.sleep(2)
            continue_btn_sidebar.click()
            print('Step  5 Done')
            # step 5
            time.sleep(2)
            continue_btn_sidebar.click()
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
            print('Step  6 Done')
            time.sleep(4)
            continue_btn_sidebar.click()
            print('Step  7 Done')
            time.sleep(4)
            continue_btn_sidebar.click()
            print('Step  8 Done')
            time.sleep(2)
            popup_wraper = browser.find_elements(By.XPATH, '//div[@role="dialog"]')
            subscription_popup = popup_wraper[1].find_element(By.TAG_NAME, 'main')
            get_buttons = subscription_popup.find_elements(By.TAG_NAME, "button")
            get_buttons[1].click()
            time.sleep(4)
            wait.until(EC.element_to_be_clickable((continue_btn_sidebar))).click()
            print('Step 9 Done')
            time.sleep(4)
            if browser.find_elements(By.ID, "btnDisclaimerNext"):
                browser.find_element(By.ID, "btnDisclaimerNext").click()
            wait.until(EC.element_to_be_clickable((By.ID, "btnSubmitPayment"))).click()
            wait.until(EC.element_to_be_clickable((By.ID, "btnCompleteProcess"))).click()
            if order == 0:
                print('got here')
                browser.get(Global_Variables['url'] + '/account/settings/security')
                password = wait.until(EC.element_to_be_clickable((By.ID, "new_password")))
                print('got here')
                password.send_keys('testivisa5!')
                password_repeat = wait.until(EC.element_to_be_clickable((By.ID, "password_repeat")))
                password_repeat.send_keys('testivisa5!') 
                browser.find_element(By.XPATH, '//button[@data-handle="updatePasswordBtn"]').click()
            time.sleep(4)
            print('Payment Done')
    except Exception as e :
        print(logging.error("An error occurred:" + str(e)))
