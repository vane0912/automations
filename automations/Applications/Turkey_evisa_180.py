from .imports import *
logging.basicConfig(level=logging.ERROR)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)  

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

logging.getLogger().addHandler(console_handler)

def TR_App_P2(data):
    setArguments(data)
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
            #print('Passed Step 1')
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
            #print('Passed Step 2')
            # step 5
            continue_sidebar.click() if continue_sidebar.is_enabled() else wait.until(EC.element_to_be_clickable((By.ID, "btnContinueSidebar"))).click()
            #print('Passed Step 3')
            for user in range(int(Global_Variables['applicants'])):
                try:
                    passport_num = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.NAME, "applicant."+ str(user) +".passport_num")))
                    passport_num.send_keys(Global_Variables['Passport_num'])
                    passport_day = Select(WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.NAME, "applicant."+ str(user) +".passport_expiration_date.day")))) 
                    passport_day.select_by_value('23')
                    passport_month = Select(WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.NAME, "applicant."+ str(user) +".passport_expiration_date.month")))) 
                    passport_month.select_by_value('10')
                    passport_year = Select(WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.NAME, "applicant."+ str(user) +".passport_expiration_date.year")))) 
                    passport_year.select_by_value('2032')

                    passport_issue_day = Select(WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.NAME, "applicant."+ str(user) +".passport_issued_date.day")))) 
                    passport_issue_day.select_by_value('23')
                    passport_issue_month = Select(WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.NAME, "applicant."+ str(user) +".passport_issued_date.month")))) 
                    passport_issue_month.select_by_value('10')
                    passport_issue_year = Select(WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.NAME, "applicant."+ str(user) +".passport_issued_date.year")))) 
                    passport_issue_year.select_by_value('2020')

                    if user == int(Global_Variables['applicants']) - 1:
                        continue_sidebar.click() if continue_sidebar.is_enabled() else wait.until(EC.element_to_be_clickable((By.ID, "btnContinueSidebar"))).click()
                except ElementNotInteractableException:
                    wait.until(EC.element_to_be_clickable((By.ID, 'btnPreviousSidebar'))).click()
                    passport_num = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.NAME, "applicant."+ str(user) +".passport_num")))
                    passport_num.send_keys(Global_Variables['Passport_num'])
                    passport_day = Select(WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.NAME, "applicant."+ str(user) +".passport_expiration_date.day")))) 
                    passport_day.select_by_value('23')
                    passport_month = Select(WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.NAME, "applicant."+ str(user) +".passport_expiration_date.month")))) 
                    passport_month.select_by_value('10')
                    passport_year = Select(WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.NAME, "applicant."+ str(user) +".passport_expiration_date.year")))) 
                    passport_year.select_by_value('2032')

                    passport_issue_day = Select(WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.NAME, "applicant."+ str(user) +".passport_issued_date.day")))) 
                    passport_issue_day.select_by_value('23')
                    passport_issue_month = Select(WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.NAME, "applicant."+ str(user) +".passport_issued_date.month")))) 
                    passport_issue_month.select_by_value('10')
                    passport_issue_year = Select(WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.NAME, "applicant."+ str(user) +".passport_issued_date.year")))) 
                    passport_issue_year.select_by_value('2020')
                    if user == int(Global_Variables['applicants']) - 1:
                        continue_sidebar.click() if continue_sidebar.is_enabled() else wait.until(EC.element_to_be_clickable((By.ID, "btnContinueSidebar"))).click()
                except StaleElementReferenceException:
                    print('ERROR')
                    wait.until(EC.element_to_be_clickable((By.ID, 'btnPreviousSidebar'))).click()
                    passport_num = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.NAME, "applicant."+ str(user) +".passport_num")))
                    passport_num.send_keys(Global_Variables['Passport_num'])
                    passport_day = Select(WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.NAME, "applicant."+ str(user) +".passport_expiration_date.day")))) 
                    passport_day.select_by_value('23')
                    passport_month = Select(WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.NAME, "applicant."+ str(user) +".passport_expiration_date.month")))) 
                    passport_month.select_by_value('10')
                    passport_year = Select(WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.NAME, "applicant."+ str(user) +".passport_expiration_date.year")))) 
                    passport_year.select_by_value('2032')

                    passport_issue_day = Select(WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.NAME, "applicant."+ str(user) +".passport_issued_date.day")))) 
                    passport_issue_day.select_by_value('23')
                    passport_issue_month = Select(WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.NAME, "applicant."+ str(user) +".passport_issued_date.month")))) 
                    passport_issue_month.select_by_value('10')
                    passport_issue_year = Select(WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.NAME, "applicant."+ str(user) +".passport_issued_date.year")))) 
                    passport_issue_year.select_by_value('2020')
                    if user == int(Global_Variables['applicants']) - 1:
                        continue_sidebar.click() if continue_sidebar.is_enabled() else wait.until(EC.element_to_be_clickable((By.ID, "btnContinueSidebar"))).click()
                except TimeoutException:
                    print('ERROR2')
                    wait.until(EC.element_to_be_clickable((By.ID, 'btnPreviousSidebar'))).click()
                    passport_num = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.NAME, "applicant."+ str(user) +".passport_num")))
                    passport_num.send_keys(Global_Variables['Passport_num'])
                    passport_day = Select(WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.NAME, "applicant."+ str(user) +".passport_expiration_date.day")))) 
                    passport_day.select_by_value('23')
                    passport_month = Select(WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.NAME, "applicant."+ str(user) +".passport_expiration_date.month")))) 
                    passport_month.select_by_value('10')
                    passport_year = Select(WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.NAME, "applicant."+ str(user) +".passport_expiration_date.year")))) 
                    passport_year.select_by_value('2032')

                    passport_issue_day = Select(WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.NAME, "applicant."+ str(user) +".passport_issued_date.day")))) 
                    passport_issue_day.select_by_value('23')
                    passport_issue_month = Select(WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.NAME, "applicant."+ str(user) +".passport_issued_date.month")))) 
                    passport_issue_month.select_by_value('10')
                    passport_issue_year = Select(WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.NAME, "applicant."+ str(user) +".passport_issued_date.year")))) 
                    passport_issue_year.select_by_value('2020')
                    if user == int(Global_Variables['applicants']) - 1:
                        continue_sidebar.click() if continue_sidebar.is_enabled() else wait.until(EC.element_to_be_clickable((By.ID, "btnContinueSidebar"))).click()
                
            continue_step_6 = (By.ID, "btnContinueSidebar")
            print('before speeds')
            wait.until(EC.text_to_be_present_in_element((By.ID, "app"), '+ Standard, 24 hours'))
            safe_element_click(browser, continue_step_6) 
            print('after speeds')
            wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, 'h1'), 'Review your order'))
            wait.until(EC.text_to_be_present_in_element((By.ID, "btnContinueSidebar"), 'Continue to Payment'))
            safe_element_click(browser, continue_step_6) 
            try:
                WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, 'app'), 'Possible Duplicate'))
                btn_disclaimer = wait.until(EC.element_to_be_clickable((By.ID, "btnDisclaimerNext")))
                btn_disclaimer.click()

                btn_submit_payment = wait.until(EC.element_to_be_clickable((By.ID, "btnSubmitPayment")))
                btn_submit_payment.click()
            
                btn_complete = wait.until(EC.element_to_be_clickable((By.ID, "btnCompleteProcess")))

                btn_complete.click()
            except: 
                btn_submit_payment = wait.until(EC.element_to_be_clickable((By.ID, "btnSubmitPayment")))
                btn_submit_payment.click()

                btn_complete = wait.until(EC.element_to_be_clickable((By.ID, "btnCompleteProcess")))
                btn_complete.click()
            #print('Passed Step 8')
            for post_payment_user in range(int(Global_Variables['applicants'])):    
                gender_select = Select(wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@data-handle='dropdown-applicant." + str(post_payment_user) + ".gender']"))) ) 
                gender_select.select_by_index(0)
                print(post_payment_user)
                if post_payment_user == int(Global_Variables['applicants']) - 1:
                    print('here 2')
                    wait.until(EC.element_to_be_clickable((By.ID, 'btnSubmitApplication'))).click()
                    wait.until(EC.element_to_be_clickable((By.ID, 'btnDismissAppDownload'))).click()
                else:
                    print('here')
                    wait.until(EC.element_to_be_clickable((By.ID, 'btnContinueUnderSection'))).click()
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
            #print('ORDER ' + str(order))
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
        ##https://costumer-facing1-production.up.railway.app
        ##https://costumer-facing1-automations-pr-6.up.railway.app
        ##http://127.0.0.1:5000
        requests.post('https://costumer-facing1-automations-pr-6.up.railway.app' + '/check-automation-status',json=automation_results, headers={'Content-type': 'application/json', 'Accept': 'text/plain'})
        return automation_results
    except Exception as e:
        requests.post('https://costumer-facing1-automations-pr-6.up.railway.app' + '/check-automation-status',json={'ERROR': str(e).splitlines()[0], 'Status' : 'Failed'}, headers={'Content-type': 'application/json', 'Accept': 'text/plain'})
        logging.debug('Debug message: %s', e)
        logging.error('Error occurred: %s', traceback.format_exc())
        print(str(e).splitlines()[0])
        return {'Status': e}