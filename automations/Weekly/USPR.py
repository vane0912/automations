from .imports import *
def USPR_PASSPORT_RENEWAL(url, email):
    Order_numbers = []
    chrome_options = Options()
    chrome_options.add_argument('--headless') 
    chrome_options.add_argument('window-size=1920,1080')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    #chrome_options.add_argument("--incognito")
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
    
            dob_day = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'general.passport_issued_date.day'))))
            dob_day.select_by_value('4')
            dob_month = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'general.passport_issued_date.month'))))
            dob_month.select_by_value('5')
            dob_year = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'general.passport_issued_date.year'))))
            dob_year.select_by_value("2022")
    
            dob_day = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'general.passport_expiration_date.day'))))
            dob_day.select_by_value('9')
            dob_month = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'general.passport_expiration_date.month'))))
            dob_month.select_by_value('7')
            dob_year = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'general.passport_expiration_date.year'))))
            dob_year.select_by_value("2024")
          
            dob_day = Select(wait.until(EC.element_to_be_clickable((By.XPATH, '//select[@data-handle="dropdown-general.upcoming_trip_exists"]'))))
            dob_day.select_by_value('No')
            
            wait.until(EC.element_to_be_clickable((By.ID, 'btnContinueUnderSection'))).click()

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
            time.sleep(3)
            home_address.send_keys(Keys.ARROW_DOWN)
            home_address.send_keys(Keys.ENTER)
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
            wait.until(EC.element_to_be_clickable((By.ID, 'btnContinueSidebar'))).click()
            try:
                WebDriverWait(browser, 8).until(EC.text_to_be_present_in_element((By.ID, 'app'), 'Possible Duplicate'))
                btn_disclaimer = wait.until(EC.element_to_be_clickable((By.ID, "btnDisclaimerNext")))
                btn_disclaimer.click()

                btn_submit_payment = wait.until(EC.element_to_be_clickable((By.ID, "btnSubmitPayment")))
                btn_submit_payment.click()
                
                order_number = wait.until(EC.visibility_of_element_located((By.XPATH, '//h2[@data-handle="order-id"]')))
                Order_numbers.append(re.findall(r'\d+', order_number.text))
                
                btn_complete = wait.until(EC.element_to_be_clickable((By.ID, "btnCompleteProcess")))
                btn_complete.click()
            except: 
                btn_submit_payment = wait.until(EC.element_to_be_clickable((By.ID, "btnSubmitPayment")))
                btn_submit_payment.click()

                order_number = wait.until(EC.visibility_of_element_located((By.XPATH, '//h2[@data-handle="order-id"]')))
                Order_numbers.append(re.findall(r'\d+', order_number.text))
                
                btn_complete = wait.until(EC.element_to_be_clickable((By.ID, "btnCompleteProcess")))
                btn_complete.click()
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
        requests.post('https://costumer-facing1-automations-pr-6.up.railway.app' + '/check-automation-status',json=automation_results, headers={'Content-type': 'application/json', 'Accept': 'text/plain'})
        return automation_results
    except Exception as e:
        requests.post('https://costumer-facing1-automations-pr-6.up.railway.app' + '/check-automation-status',json={'ERROR': str(e).splitlines()[0], 'Status' : 'Failed'}, headers={'Content-type': 'application/json', 'Accept': 'text/plain'})
        logging.debug('Debug message: %s', e)
        logging.error('Error occurred: %s', traceback.format_exc())
        return {'Status': e}