from ..imports import *
def CHINA_90_DAYS(data):
    setArguments(data)
    questions = app_questions(Global_Variables['url'], 10845, Global_Variables['App_Version'])
    Global_Variables['Order_Numbers'] = []
    chrome_options = Options()
    #chrome_options.add_argument('--headless') 
    chrome_options.add_argument('window-size=1920,1080')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    wait = WebDriverWait(browser, 150, ignored_exceptions=(NoSuchElementException,StaleElementReferenceException))
    try:
        for order in range(int(Global_Variables['N. Orders'])):
            browser.get(Global_Variables['url'] + '/china/apply-now')
            current_url = browser.current_url
            if order == 0:
                nationality = wait.until(EC.element_to_be_clickable((By.NAME, 'general.common_nationality_country')))
                nationality.click()
                nationality_values = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@data-handle='dropdown-general.common_nationality_country']")))
                nationality_values.send_keys(Global_Variables['Country'], Keys.ENTER)
            product = Select(wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@data-handle='dropdown-general.visa_type_id']"))))
            product.select_by_value('5500')
            #wait.until(EC.element_to_be_clickable((By.ID, "btnContinueUnderSection"))).click() 
            wait.until(lambda driver: driver.current_url != current_url) 
            sections_arr = []
            values_arr = []
            for key,value in questions['questions'].items():
                values_arr.append(value)
                sections_arr.append(value.get('multipart_section'))
            for section in sections_arr:
                current_url = browser.current_url
                arr_section_questions = [item for item in values_arr if item["multipart_section"] in current_url]
                for question in arr_section_questions:
                    print(question['slug'])
                    if question['slug'] == 'arrival_date':
                        arrival_date = wait.until(EC.element_to_be_clickable((By.NAME, "general." + question['slug'])))
                        arrival_date.click()
                        svg_locator = (By.CSS_SELECTOR, "div.is-right svg")
                        day_month = (By.CSS_SELECTOR, "div.day-13")
                        safe_element_click(browser, svg_locator)
                        safe_element_click(browser, day_month)
                    elif question['slug'] == 'departure_date': 
                        departure_date = wait.until(EC.element_to_be_clickable((By.NAME, "general." + question['slug'])))
                        departure_date.click()
                        svg_locator = (By.CSS_SELECTOR, "div.is-right svg")
                        day_month = (By.CSS_SELECTOR, "div.day-13")
                        safe_element_click(browser, svg_locator)
                        safe_element_click(browser, day_month)
                    elif question['slug'] == 'email' and order == 0:
                        email = wait.until(EC.element_to_be_clickable((By.NAME, 'general.' + question['slug'])))
                        email.send_keys(Global_Variables['Email'])
                    elif question['slug'] == 'dob':
                        dob_day = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'] + '.day'))))
                        dob_day.select_by_value('10')
                        dob_month = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'] + '.month'))))
                        dob_month.select_by_value('10')
                        dob_year = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'] + '.year'))))
                        dob_year.select_by_value("2000") 
                    elif question['field_type'] == 'textbox':
                        input_field = wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'])))
                        input_field.send_keys('aaaaa') 
                    elif 'expiration' in question['slug']:
                        passport_expiration_day = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'] + '.day'))))
                        passport_expiration_day.select_by_value('10')
                        passport_expiration_month = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'] + '.month'))))
                        passport_expiration_month.select_by_value('10')
                        passport_expiration_year = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'] + '.year'))))
                        passport_expiration_year.select_by_value("2028") 
                    elif question['slug'] == 'appointment_location_id':
                        input_field_speciality = wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'] + '_autocomplete')))
                        input_field_speciality.send_keys('Nueva York, EE. UU') 
                        time.sleep(3)
                        input_field_speciality.send_keys(Keys.ARROW_DOWN)
                        input_field_speciality.send_keys(Keys.ENTER)
                        runner_pilot = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-handle="boolean-No, I want to go to the embassy myself"]')))
                        runner_pilot.click()
                if "payment" in current_url:
                    try:
                        WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, 'app'), 'Possible Duplicate'))
                        btn_disclaimer = wait.until(EC.element_to_be_clickable((By.ID, "btnDisclaimerNext")))
                        btn_disclaimer.click()

                        btn_submit_payment = wait.until(EC.element_to_be_clickable((By.ID, "btnSubmitPayment")))
                        btn_submit_payment.click()

                        btn_complete = wait.until(EC.element_to_be_clickable((By.ID, "btnCompleteProcess")))

                        btn_complete.click()
                        time.sleep(4)
                    except: 
                        btn_submit_payment = wait.until(EC.element_to_be_clickable((By.ID, "btnSubmitPayment")))
                        btn_submit_payment.click()

                        btn_complete = wait.until(EC.element_to_be_clickable((By.ID, "btnCompleteProcess")))
                        btn_complete.click()
                        time.sleep(4)
                else:
                    continue_sidebar = wait.until(EC.visibility_of_element_located((By.ID, "btnContinueSidebar")))
                    continue_sidebar.click() if continue_sidebar.is_enabled() else wait.until(EC.element_to_be_clickable((By.ID, "btnContinueSidebar"))).click()
                    wait.until(lambda driver: driver.current_url != current_url) 
            time.sleep(5)

    except:
        failed_request()


"""
if value['slug'] == 'arrival_date':
                            arrival_date = wait.until(EC.element_to_be_clickable((By.NAME, "general." + value['slug'])))
                            arrival_date.click()
                            svg_locator = (By.CSS_SELECTOR, "div.is-right svg")
                            day_month = (By.CSS_SELECTOR, "div.day-13")
                            safe_element_click(browser, svg_locator)
                            safe_element_click(browser, day_month)
                        if value['slug'] == 'departure_date': 
                            departure_date = wait.until(EC.element_to_be_clickable((By.NAME, "general." + value['slug'])))
                            departure_date.click()
                            svg_locator = (By.CSS_SELECTOR, "div.is-right svg")
                            day_month = (By.CSS_SELECTOR, "div.day-13")
                            safe_element_click(browser, svg_locator)
                            safe_element_click(browser, day_month)
                        if value['slug'] == 'email' and order == 0:
                            email = wait.until(EC.element_to_be_clickable((By.NAME, 'general.' + value['slug'])))
                            email.send_keys(Global_Variables['Email'])
                        if value['field_type'] == 'textbox':
                            print(value['slug'])
                            input_field = wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + value['slug'])))
                            input_field.send_keys('Pedro')
                            print(input_field)
if value.get('multipart_section') == browser.current_url.split("=")[1]:
                    if value['slug'] == 'arrival_date':
                        arrival_date = wait.until(EC.element_to_be_clickable((By.NAME, "general." + value['slug'])))
                        arrival_date.click()

                        svg_locator = (By.CSS_SELECTOR, "div.is-right svg")
                        day_month = (By.CSS_SELECTOR, "div.day-13")
                        safe_element_click(browser, svg_locator)
                        safe_element_click(browser, day_month)
                    if value['slug'] == 'departure_date': 
                        departure_date = wait.until(EC.element_to_be_clickable((By.NAME, "general." + value['slug'])))
                        departure_date.click()

                        svg_locator = (By.CSS_SELECTOR, "div.is-right svg")
                        day_month = (By.CSS_SELECTOR, "div.day-13")
                        safe_element_click(browser, svg_locator)
                        safe_element_click(browser, day_month)
                    if value['slug'] == 'email' and order == 0:
                        email = wait.until(EC.element_to_be_clickable((By.NAME, 'general.' + value['slug'])))
                        email.send_keys(Global_Variables['Email'])
                    continue_sidebar = wait.until(EC.visibility_of_element_located((By.ID, "btnContinueSidebar")))
                    continue_sidebar.click() if continue_sidebar.is_enabled() else wait.until(EC.element_to_be_clickable((By.ID, "btnContinueSidebar"))).click()
                    print(value['slug'])
"""