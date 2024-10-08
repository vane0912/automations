from ..imports import *


def USPR_PASSPORT_RENEWAL(url, email):
    Order_numbers = []
    chrome_options = Options()
    chrome_options.add_argument('--headless') 
    chrome_options.add_argument('window-size=1920,1080')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    wait = WebDriverWait(browser, 200, ignored_exceptions=(NoSuchElementException,StaleElementReferenceException))
    
    try: 
        for x in range(3):
            browser.get(url + '/passport-renewal/united-states/application')
            dob_day = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'general.dob.day'))))
            dob_day.select_by_value('10')
            dob_month = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'general.dob.month'))))
            dob_month.select_by_value('10')
            dob_year = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'general.dob.year'))))
            dob_year.select_by_value("2000")
    
            passport_issued_day = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'general.passport_issued_date.day'))))
            passport_issued_day.select_by_value('4')
            passport_issued_month = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'general.passport_issued_date.month'))))
            passport_issued_month.select_by_value('5')
            passport_issued_year = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'general.passport_issued_date.year'))))
            passport_issued_year.select_by_value("2022")
    
            passport_expiration_day = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'general.passport_expiration_date.day'))))
            passport_expiration_day.select_by_value('9')
            passport_expiration_month = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'general.passport_expiration_date.month'))))
            passport_expiration_month.select_by_value('7')
            passport_expiration_year = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'general.passport_expiration_date.year'))))
            passport_expiration_year.select_by_value("2024")
          
            upocoming_trips = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@name="general.upcoming_trip_exists"]')))
            no_trips = upocoming_trips.find_elements(By.TAG_NAME, 'button')
            no_trips[1].click()
            
            continue_btn = wait.until(EC.visibility_of_element_located((By.ID, 'btnContinueUnderSection')))
            click_btn = continue_btn.find_elements(By.TAG_NAME, 'button')
            wait.until(EC.element_to_be_clickable(click_btn[0])).click()

            passport_num = wait.until(EC.element_to_be_clickable((By.NAME, 'general.passport_num')))
            passport_num.send_keys('1111111111')
            telephone = wait.until(EC.element_to_be_clickable((By.NAME, 'telephone')))
            telephone.send_keys('202123213')
            first_name = wait.until(EC.element_to_be_clickable((By.NAME, 'general.first_name')))
            first_name.send_keys('Pedro')
            last_name = wait.until(EC.element_to_be_clickable((By.NAME, 'general.last_name')))
            last_name.send_keys('Gonzalez')
            if x == 0:
                email_user = wait.until(EC.element_to_be_clickable((By.NAME, 'general.email')))
                email_user.send_keys(email)
            home_address = wait.until(EC.element_to_be_clickable((By.NAME, 'general.home_address')))
            home_address.send_keys('281 West Lane Avenue') if x == 2 else home_address.send_keys('700 Exposition Park Drive')
            home_city = wait.until(EC.element_to_be_clickable((By.NAME, 'general.home_city')))
            home_city.send_keys('Columbus') if x == 2 else home_city.send_keys('Los Angeles')
            home_state = wait.until(EC.element_to_be_clickable((By.NAME, 'general.home_state')))
            home_state.send_keys('OH') if x == 2 else home_state.send_keys('CA')
            home_zip = wait.until(EC.element_to_be_clickable((By.NAME, 'general.home_zip')))
            home_zip.send_keys('43210') if x == 2 else home_zip.send_keys('90037')
            time.sleep(3)
            wait.until(EC.element_to_be_clickable((By.ID, 'btnContinueSidebar'))).click()
            wait.until(EC.text_to_be_present_in_element((By.ID, 'question-container'), 'Renewal Kit Delivery Speed'))
            wait.until(EC.element_to_be_clickable((By.ID, 'btnContinueSidebar'))).click()
            time.sleep(3)
            wait.until(EC.text_to_be_present_in_element((By.ID, 'question-container'), 'Get Your New Passport Between'))
            gov_expedited_service = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@data-ivisa-question-selector="general.renewal_gov_lead_time"]')))
            get_options = gov_expedited_service.find_elements(By.TAG_NAME, 'ul')
            get_li = get_options[0].find_elements(By.TAG_NAME, 'li')
            wait.until(EC.element_to_be_clickable((get_li[1]))).click() if x == 0 else wait.until(EC.element_to_be_clickable((get_li[0]))).click()
            wait.until(EC.element_to_be_clickable((By.ID, 'btnContinueSidebar'))).click()
            wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, 'h1'), 'Review your order'))
            try:
                WebDriverWait(browser, 8).until(EC.text_to_be_present_in_element((By.ID, 'app'), 'Possible Duplicate'))
                btn_disclaimer = wait.until(EC.element_to_be_clickable((By.ID, "btnDisclaimerNext")))
                btn_disclaimer.click()
                wait.until(EC.element_to_be_clickable((By.ID, 'btnContinueSidebar'))).click()

                btn_submit_payment = wait.until(EC.element_to_be_clickable((By.ID, "btnSubmitPayment")))
                btn_submit_payment.click()
                wait.until(EC.text_to_be_present_in_element((By.ID, 'question-container'), 'General Information'))
            except: 
                wait.until(EC.element_to_be_clickable((By.ID, 'btnContinueSidebar'))).click()
                btn_submit_payment = wait.until(EC.element_to_be_clickable((By.ID, "btnSubmitPayment")))
                btn_submit_payment.click()
                wait.until(EC.text_to_be_present_in_element((By.ID, 'question-container'), 'General Information'))
            if x == 0:
                browser.get(url + '/account/settings/security')
                password = wait.until(EC.element_to_be_clickable((By.ID, "new_password")))
                password.send_keys('testivisa5!')
                password_repeat = wait.until(EC.element_to_be_clickable((By.ID, "password_repeat")))
                password_repeat.send_keys('testivisa5!') 
                browser.find_element(By.XPATH, '//button[@data-handle="updatePasswordBtn"]').click()
        automation_results = {
            'Order_numbers' : Order_numbers,
            'Status' : 'Success',
            'email' : email,
        }
        requests.post('https://costumer-facing1-production.up.railway.app' + '/check-automation-status',json=automation_results, headers={'Content-type': 'application/json', 'Accept': 'text/plain'})
        return automation_results
    except Exception as e:
        requests.post('https://costumer-facing1-production.up.railway.app' + '/check-automation-status',json={'ERROR': str(e).splitlines()[0], 'Status' : 'Failed'}, headers={'Content-type': 'application/json', 'Accept': 'text/plain'})
        logging.debug('Debug message: %s', e)
        logging.error('Error occurred: %s', traceback.format_exc())
        return {'Status': e}