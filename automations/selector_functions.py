from .global_imports import *

def safe_element_click(driver, locator):
    attempts = 0
    max_attempts = 3  
    while attempts < max_attempts:
        try:
            element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable(locator))
            element.click()
            return True  # Click successful, return True
        except EC.StaleElementReferenceException:
            print(f"StaleElementReferenceException occurred, retrying attempt {attempts + 1}")
            attempts += 1
    print(f"Failed to click element after {max_attempts} attempts")
    return False 
def arrival_date(question, wait, browser, data):
    dates_calendar = wait.until(EC.element_to_be_clickable((By.NAME, "general." + question['slug'])))
    dates_calendar.click()
    svg_locator = (By.XPATH, '//button[@data-dp-element="action-next"]')
    if question['slug'] == 'arrival_date':
        get_all = browser.find_elements(By.CLASS_NAME, "dp--future")
        get_all[2].click()
    else:
        get_all = browser.find_elements(By.CLASS_NAME, "dp--future")
        get_all[5].click()
    safe_element_click(browser, svg_locator) 
def email(question, wait, browser, data):
    try: 
      if len(browser.find_elements(By.NAME, 'applicant.0.' + question['slug'])) > 0:
         email = WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'])))
      else: 
          email = WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.NAME, 'general.' + question['slug'])))
      email.send_keys(data['Email'])
    except:
       pass
def dob(question, wait, browser, data):
    try:
        WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.NAME, 'applicant.0.' + question['slug'] + '.day')))
        dob_day = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'] + '.day'))))
        dob_day.select_by_value('10')
        dob_month = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'] + '.month'))))
        dob_month.select_by_value('10')
        dob_year = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'] + '.year'))))
        dob_year.select_by_value("2000") 
    except: 
        pass
def textbox(question, wait, browser, data):
    attempts = 0
    max_attempts = 3
    while max_attempts > attempts:
        if attempts == 0:
            try:
                WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.NAME, 'applicant.0.' + question['slug'])))
                element = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'])))
                element.send_keys('aaaaaa')
                return True
            except:
                attempts += 1
        elif attempts == 1:
            try:
                WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.NAME, 'general.' + question['slug'])))
                element = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.NAME, 'general.' + question['slug'])))
                element.send_keys('aaaaaa')
                return True
            except:
                attempts += 1
        else:
            attempts = 3
def fieldset_repeat(question, wait, browser, data):
    attempts = 0
    max_attempts = 2  
    while attempts < max_attempts:
        if attempts == 0:
            try:
                WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, '//div[@data-ivisa-question-selector="applicant' + '.0.' + question['slug'] + '"]')))
                for field in question['fieldset']:
                    if field['field_type'] == 'textbox' :
                        input_field = wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'] + '.0.'+ field['slug'])))
                        input_field.send_keys('aaaaa')
                    if field['field_type'] == 'dropdown' or field['field_type'] == 'dropdown_country':
                        try:
                            dropdown_general = WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'] + '.0.'+ field['slug'])))
                            dropdown_general.click()
                            dropdown_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@data-handle="dropdown-applicant.' + '0.' + question['slug'] + '.0.'+ field['slug'] + '"]')))
                            dropdown_input.send_keys(Keys.ARROW_DOWN)
                            dropdown_input.send_keys(Keys.ENTER)
                        except:
                            dropdown_general = WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'] + '.0.'+ field['slug'])))
                            buttons = dropdown_general.find_elements(By.TAG_NAME, 'button')
                            buttons[0].click()
                    if field['field_type'] == 'datepicker' and 'dob' in field['slug']:
                        start_day = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'] + '.0.'+ field['slug'] + '.day'))))
                        start_day.select_by_value('10')
                        start_month = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'] + '.0.'+ field['slug'] + '.month'))))
                        start_month.select_by_value('11')
                        start_year = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'] + '.0.'+ field['slug'] + '.year'))))
                        start_year.select_by_value("2000") 
                    if field['field_type'] == 'datepicker' and 'start' in field['slug']:
                        start_day = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'] + '.0.'+ field['slug'] + '.day'))))
                        start_day.select_by_value('10')
                        start_month = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'] + '.0.'+ field['slug'] + '.month'))))
                        start_month.select_by_value('11')
                        start_year = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'] + '.0.'+ field['slug'] + '.year'))))
                        start_year.select_by_value("2023") 
                    if field['field_type'] == 'datepicker' and 'end' in field['slug']:
                        start_day = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'] + '.0.'+ field['slug'] + '.day'))))
                        start_day.select_by_value('20')
                        start_month = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'] + '.0.'+ field['slug'] + '.month'))))
                        start_month.select_by_value('11')
                        start_year = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'] + '.0.'+ field['slug'] + '.year'))))
                        start_year.select_by_value("2023")
                    if field['field_type'] == 'phone':
                        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@name="applicant' + '.0.' + question['slug'] + '.0.'+ field['slug'] + '"]' + '//div[@data-handle="filter-value"]'))).click()
                        input_code = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@data-handle="dial-codes"]')))
                        input_code.send_keys("+52")
                        input_code.send_keys(Keys.ARROW_DOWN)
                        input_code.send_keys(Keys.ENTER)
                        input_field = wait.until(EC.element_to_be_clickable((By.NAME, 'telephone')))
                        input_field.send_keys('11111111') 
                        input_field.send_keys(Keys.ENTER)
                attempts = 2 
            except:
                attempts += 1
        elif attempts == 1:
            try:
                WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, '//div[@data-ivisa-question-selector="general.' + question['slug'] + '"]')))
                for field in question['fieldset']:
                    if field['field_type'] == 'textbox':
                        input_field = wait.until(EC.element_to_be_clickable((By.NAME, 'general.' + question['slug'] + '.0.'+ field['slug'])))
                        input_field.send_keys('aaaaa')
                    if field['field_type'] == 'dropdown':
                        dropdown_general = wait.until(EC.element_to_be_clickable((By.NAME, 'general.' + question['slug'] + '.0.'+ field['slug'])))
                        dropdown_general.click()
                        dropdown_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@data-handle="dropdown-general.' + question['slug'] + '.0.'+ field['slug'] + '"]')))
                        dropdown_input.send_keys(Keys.ARROW_DOWN)
                        dropdown_input.send_keys(Keys.ENTER)
                    if field['field_type'] == 'datepicker' and 'start' or 'from' in field['slug']:
                        start_day = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'general.' + question['slug'] + '.0.'+ field['slug'] + '.day'))))
                        start_day.select_by_value('8')
                        start_month = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'general.' + question['slug'] + '.0.'+ field['slug'] + '.month'))))
                        start_month.select_by_value('8')
                        start_year = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'general.' + question['slug'] + '.0.'+ field['slug'] + '.year'))))
                        start_year.select_by_value("2025") 
                    if field['field_type'] == 'datepicker' and 'end' or 'to' in field['slug']:
                        start_day = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'general.' + question['slug'] + '.0.'+ field['slug'] + '.day'))))
                        start_day.select_by_value('20')
                        start_month = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'general.' + question['slug'] + '.0.'+ field['slug'] + '.month'))))
                        start_month.select_by_value('8')
                        start_year = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'general.' + question['slug'] + '.0.'+ field['slug'] + '.year'))))
                        start_year.select_by_value("2025")
                    if 'dob' in field['slug']:
                        dob_day = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'general.' + question['slug'] + '.0.' + field['slug'] + '.day'))))
                        dob_day.select_by_value('10')
                        dob_month = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'general.' + question['slug'] + '.0.' + field['slug'] + '.month'))))
                        dob_month.select_by_value('10')
                        dob_year = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'general.' + question['slug'] + '.0.' + field['slug'] +'.year'))))
                        dob_year.select_by_value("2000") 
                    if field['slug'] == 'gender':
                        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, '//div[@data-ivisa-question-selector="general.' + question['slug'] + '.0.'+ field['slug'] + '"]')))
                        div_dropdown = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@data-ivisa-question-selector="general.' + question['slug'] + '.0.'+ field['slug'] + '"]')))
                        options_inside = div_dropdown.find_elements(By.TAG_NAME, 'button')
                        options_inside[0].click()  
                attempts = 2
            except:
                attempts += 1
def phone(question, wait, browser, data):
    attempts = 0
    max_attempts = 2
    while max_attempts > attempts:
        if attempts == 0: 
            try:
                WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.NAME, "general." + question['slug'])))
                wait.until(EC.visibility_of_element_located((By.XPATH,'//div[@data-handle="filter-value"]'))).click()
                try:
                    input_code = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, '//input[@data-handle="dial-codes"]')))
                except: 
                    input_code = browser.find_element(By.XPATH, '//input[@data-handle="dial-codes"]')
                input_code.send_keys("+52")
                input_code.send_keys(Keys.ARROW_DOWN)
                input_code.send_keys(Keys.ENTER)
                input_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@name="general.'+ question['slug'] + '"]' + '//input[@name="telephone"]' )))
                input_field.send_keys('11111111') 
                input_field.send_keys(Keys.ENTER)
                attempts = 2
            except:
                attempts += 1
        elif attempts == 1:
            try:
                WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.NAME, "applicant" + '.0.' + question['slug'])))
                wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@name="applicant.0.'+ question['slug'] + '"]' + '//div[@data-handle="filter-value"]'))).click()
                try:
                    input_code = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, '//input[@data-handle="dial-codes"]')))
                except: 
                    input_code = browser.find_element(By.XPATH, '//div[@name="applicant.0.'+ question['slug'] + '"]' + '//input[@data-handle="dial-codes"]')
                input_code.send_keys("+52")
                input_code.send_keys(Keys.ARROW_DOWN)
                input_code.send_keys(Keys.ENTER)
                input_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@name="applicant.0.'+ question['slug'] + '"]' + '//input[@name="telephone"]' )))
                time.sleep(2)
                input_field.send_keys('11111111') 
                input_field.send_keys(Keys.ENTER)
                attempts = 2
            except: 
                attempts = 2
def dropdown(question, wait, browser, data):
    attempts = 0
    max_attempts = 4 
    while attempts < max_attempts:
        if question['field_type'] == 'dropdown_country' and question['multipart_section'] == 'step_3c':
            attempts = 4
        if question['options'] and len(question['options']) >= 5:
            if attempts == 0:
                try:
                    dropdown_general = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, '//select[@data-handle="dropdown-general.' + question['slug'] + '"]')))
                    if question['prevent_submission_if'] == None:
                        Select(dropdown_general).select_by_index(2)
                        attempts = 4
                    else:
                        prevent_values = question["prevent_submission_if"]["value"]
                        accepted_values = [e for e in question["options"] if all(val not in e["value"] for val in prevent_values)]
                        Select(dropdown_general).select_by_value(accepted_values[0]["value"])
                        attempts = 4
                    attempts = 4
                except:
                    attempts += 1
            elif attempts == 1:
                try:
                    dropdown_general = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, '//select[@data-handle="dropdown-applicant' + '.0.' + question['slug'] + '"]')))
                    if question['prevent_submission_if'] == None:
                        Select(dropdown_general).select_by_index(2)
                    else:
                        prevent_values = question["prevent_submission_if"]["value"]
                        accepted_values = [e for e in question["options"] if all(val not in e["value"] for val in prevent_values)]
                        Select(dropdown_general).select_by_value(accepted_values[0]["value"])
                        attempts = 4
                    attempts = 4
                except:
                    attempts += 1
            elif attempts == 2:
                try: 
                    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.NAME, 'general.' + question['slug'])))
                    dropdown_general = WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.NAME, 'general.' + question['slug'])))
                    dropdown_general.click()
                    dropdown_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@data-handle="dropdown-general.' + question['slug'] + '"]')))
                    if question['prevent_submission_if'] == None:
                        dropdown_input.send_keys(Keys.ARROW_DOWN)
                        dropdown_input.send_keys(Keys.ARROW_DOWN)
                        dropdown_input.send_keys(Keys.ARROW_DOWN)
                        dropdown_input.send_keys(Keys.ENTER)
                        attempts = 4
                    else:
                        prevent_values = question["prevent_submission_if"]["value"]
                        accepted_values = [e for e in question["options"] if all(val not in e["value"] for val in prevent_values)]
                        dropdown_input.send_keys(accepted_values[0]["value"])
                        dropdown_input.send_keys(Keys.ENTER)
                        attempts = 4
                    attempts = 4
                except:
                    attempts += 1
            elif attempts == 3:
                try: 
                    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.NAME, 'applicant.0.' + question['slug'])))
                    dropdown_general = WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'])))
                    dropdown_general.click()
                    dropdown_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@data-handle="dropdown-applicant.0.' + question['slug'] + '"]')))
                    if question['prevent_submission_if'] == None:
                        dropdown_input.send_keys(Keys.ARROW_DOWN)
                        dropdown_input.send_keys(Keys.ARROW_DOWN)
                        dropdown_input.send_keys(Keys.ARROW_DOWN)
                        dropdown_input.send_keys(Keys.ENTER)
                        attempts = 4
                    else:
                        prevent_values = question["prevent_submission_if"]["value"]
                        accepted_values = [e for e in question["options"] if all(val not in e["value"] for val in prevent_values)]
                        dropdown_input.send_keys(accepted_values[0]["value"])
                        dropdown_input.send_keys(Keys.ENTER)
                        attempts = 4
                except:
                    attempts += 1
        else:
            if attempts == 0:
                try:
                    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, '//div[@data-ivisa-question-selector="applicant' + '.0.' + question['slug'] + '"]')))
                    if question['prevent_submission_if'] == None:
                        div_dropdown = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@data-ivisa-question-selector="applicant' + '.0.' + question['slug'] + '"]')))
                        options_inside = div_dropdown.find_elements(By.TAG_NAME, 'button')
                        options_inside[0].click()
                        attempts = 4
                    else:
                        prevent_values = question["prevent_submission_if"]["value"]
                        accepted_values = [e for e in question["options"] if all(val not in e["value"] for val in prevent_values)]
                        div_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@data-ivisa-question-selector="applicant' + '.0.' + question['slug'] + '"]//button[@data-handle="boolean-' + accepted_values[0]["value"] + '"]')))
                        div_dropdown.click()
                        attempts = 4
                except: 
                    attempts += 1
            elif attempts == 1:
                try:
                    div_dropdown = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, '//div[@data-ivisa-question-selector="general.' + question['slug'] + '"]')))
                    options_inside = div_dropdown.find_elements(By.TAG_NAME, 'button')
                    options_inside[0].click()
                    attempts = 4
                except: 
                    attempts += 1
            elif attempts == 2:
                try: 
                    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.NAME, 'applicant.0.' + question['slug'])))
                    dropdown_general = WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'])))
                    dropdown_general.click()
                    dropdown_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@data-handle="dropdown-applicant.0.' + question['slug'] + '"]')))
                    if question['prevent_submission_if'] == None:
                        dropdown_input.send_keys(Keys.ARROW_DOWN)
                        dropdown_input.send_keys(Keys.ENTER)
                        attempts = 4
                    else:
                        prevent_values = question["prevent_submission_if"]["value"]
                        accepted_values = [e for e in question["options"] if all(val not in e["value"] for val in prevent_values)]
                        dropdown_input.send_keys(accepted_values[0]["value"])
                        dropdown_input.send_keys(Keys.ENTER)
                        attempts = 4
                except:
                    attempts = 4
def gender(question, wait, browser, data):
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, '//div[@data-ivisa-question-selector="applicant' + '.0.' + question['slug'] + '"]')))
    div_dropdown = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@data-ivisa-question-selector="applicant' + '.0.' + question['slug'] + '"]')))
    options_inside = div_dropdown.find_elements(By.TAG_NAME, 'button')
    options_inside[0].click() 
def address(question, wait, browser, data):
    attempts = 0
    max_attempts = 2
    while attempts < max_attempts:
        if attempts == 0:
            try:
                input_field =  WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.NAME, 'applicant' + '.0.' + question['slug'])))
                browser.execute_script("arguments[0].value = '136 West 40th Street';", input_field)
                input_field.send_keys(Keys.SPACE)
                time.sleep(2)
                try:
                    api_google = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.ID, 'autocomplete_results')))
                except:
                    api_google = browser.find_element(By.TAG_NAME, 'ul')
                select_option = api_google.find_elements(By.TAG_NAME, 'li')
                select_option[0].click()
                time.sleep(2)
                attempts = 2
            except:
                attempts += 1
        elif attempts == 1:
            try:
                input_field =  WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.NAME, 'general.' + question['slug'])))
                browser.execute_script("arguments[0].value = '136 West 40th Street';", input_field)
                input_field.send_keys(Keys.SPACE)
                time.sleep(2)
                try:
                    api_google = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.ID, 'autocomplete_results')))
                except:
                    api_google = browser.find_element(By.TAG_NAME, 'ul')
                select_option = api_google.find_elements(By.TAG_NAME, 'li')
                select_option[0].click()
                time.sleep(2)
                attempts = 2
            except: 
                attempts += 1
def appointment_location_id(question, wait, browser, data):
    try:
        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.NAME, 'applicant.0.' + question['slug'])))
        div_dropdown = wait.until(EC.visibility_of_element_located((By.NAME, 'applicant.0.' + question['slug'])))
        options_inside = div_dropdown.find_elements(By.TAG_NAME, 'button')
        options_inside[0].click()
    except:
        time.sleep(2)
        input_field_speciality = wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'] + '_autocomplete')))
        input_field_speciality.send_keys('New York, EE. UU')
        input_field_speciality.click()
        input_field_speciality.send_keys(Keys.SPACE)
        api_google = wait.until(EC.visibility_of_element_located((By.ID, 'autocomplete_results')))
        select_option = api_google.find_elements(By.TAG_NAME, 'li')
        select_option[0].click()
        time.sleep(2)
    # Runner Pilot code
    ## try:
    ##    runner_pilot = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-handle="boolean-No, I want to go to the embassy myself"]')))
    ##    runner_pilot.click()
    ## except:
    ##    passport_expiration_year = Select(wait.until(EC.element_to_be_clickable((By.XPATH, '//select[@data-handle="dropdown-applicant.0.runner_pilot"]'))))
    ##    passport_expiration_year.select_by_value("No") 
def boolean(question, wait, browser, data):
    attempts = 0
    max_attempts = 2
    while attempts < max_attempts:
        if attempts == 0:
            try: 
                boolean = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.NAME, "applicant.0." + question["slug"])))
                buttons_inside = boolean.find_elements(By.TAG_NAME, "button")
                if question['prevent_submission_if'] == None:
                    buttons_inside[1].click()
                else:
                    prevent_values = question["prevent_submission_if"]["value"]
                    buttons_inside[0].click() if prevent_values[0] == "No" else buttons_inside[1].click()
                attempts = 2 
            except:
                attempts += 1
        if attempts == 1:
            try:
                boolean = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.NAME, "general." + question["slug"])))
                buttons_inside = boolean.find_elements(By.TAG_NAME, "button")
                if question['prevent_submission_if'] == None:
                    buttons_inside[1].click()
                else:
                    prevent_values = question["prevent_submission_if"]["value"]
                    buttons_inside[0].click() if prevent_values[0] == "No" else buttons_inside[1].click()
                attempts = 2
            except:
                attempts += 1
def file_upload(question, wait, browser, data):
    if question['slug'] == 'passport_photo':
        try:
            file_upload_button = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.ID, "btn-applicant.0." + question["slug"])))
            file_upload_button.click()
            time.sleep(3)
            file_upload_in = browser.find_elements(By.NAME, 'applicant.0.' + question["slug"])
            get_image = os.path.abspath('automations/Applications/uploads/Applicant-Photo.jpg')
            file_upload_in[0].send_keys(get_image)
            accept_upload = WebDriverWait(browser, 120).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-handle="acceptFileUploadBtn"]')))
            accept_upload.click()
            WebDriverWait(browser, 8).until(EC.element_to_be_clickable((By.ID, 'nextDocumentBtn'))).click()
        except:
            pass
    else:
        try: 
            file_upload_button = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.ID, "btn-applicant.0." + question["slug"])))
            file_upload_button.click()
            time.sleep(3)
            file_upload_in = browser.find_elements(By.NAME, 'applicant.0.' + question["slug"])
            get_image = os.path.abspath('automations/Applications/uploads/1.jpg')
            file_upload_in[0].send_keys(get_image)
            accept_upload = WebDriverWait(browser, 120).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-handle="acceptFileUploadBtn"]')))
            accept_upload.click()
            WebDriverWait(browser, 8).until(EC.element_to_be_clickable((By.ID, 'nextDocumentBtn'))).click()
        except:
            pass 
def datepicker(question, wait, browser, data):
    if 'expiration' in question['slug'] or 'departure_date' in question['slug'] or 'end' in question['slug'] or 'last' in question['slug'] :
        attempts = 0
        max_attempts = 2  
        while attempts < max_attempts:
            if attempts == 0:
                try:
                    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.NAME, 'applicant.0.' + question['slug'] + '.day')))
                    passport_expiration_day = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'] + '.day'))))
                    passport_expiration_day.select_by_value('10')
                    passport_expiration_month = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'] + '.month'))))
                    passport_expiration_month.select_by_value('10')
                    passport_expiration_year = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'] + '.year'))))
                    if 'last' in question['slug']:
                        passport_expiration_year.select_by_value('2024')
                    else:
                        passport_expiration_year.select_by_index(2)
                    attempts = 2 
                except:
                    attempts += 1
            elif attempts == 1:
                try:
                    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.NAME, 'general.' + question['slug'] + '.day')))
                    passport_expiration_day = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'general.' + question['slug'] + '.day'))))
                    passport_expiration_day.select_by_value('10')
                    passport_expiration_month = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'general.' + question['slug'] + '.month'))))
                    passport_expiration_month.select_by_value('10')
                    passport_expiration_year = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'general.' + question['slug'] + '.year'))))
                    if 'last' in question['slug']:
                        passport_expiration_year.select_by_value('2024')
                    else:
                        passport_expiration_year.select_by_index(2)
                    attempts = 2 
                except:
                    attempts += 1
    elif 'issued' in question['slug'] or 'start' in question['slug']:
        attempts = 0
        max_attempts = 3
        while attempts < max_attempts:
            if attempts == 0:
                try:
                    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.NAME, 'applicant.0.' + question['slug'] + '.day')))
                    passport_expiration_day = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'] + '.day'))))
                    passport_expiration_day.select_by_value('10')
                    passport_expiration_month = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'] + '.month'))))
                    passport_expiration_month.select_by_value('10')
                    passport_expiration_year = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'] + '.year'))))
                    passport_expiration_year.select_by_value("2020") 
                    attempts = 3
                except:
                    attempts += 1
            elif attempts == 1:
                try:
                    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.NAME, 'general.' + question['slug'] + '.day')))
                    passport_expiration_day = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'general.' + question['slug'] + '.day'))))
                    passport_expiration_day.select_by_value('10')
                    passport_expiration_month = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'general.' + question['slug'] + '.month'))))
                    passport_expiration_month.select_by_value('10')
                    passport_expiration_year = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'general.' + question['slug'] +  '.year'))))
                    passport_expiration_year.select_by_value("2020") 
                    attempts = 3
                except:
                    attempts += 1
            else:
                attempts = 3
def money(question, wait, browser, data):
    try:
        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.NAME, 'amount')))
        element = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.NAME, 'amount')))
        element.send_keys('12342')
    except:
        pass
selectors = {
    'arrival_date': arrival_date,
    'departure_date': arrival_date,
    'email': email,
    'dob': dob,
    'textbox': textbox,
    'fieldset_repeat': fieldset_repeat,
    'phone': phone,
    'dropdown': dropdown,
    'dropdown_country': dropdown,
    'gender': gender,
    'datepicker': datepicker,
    'address': address,
    'appointment_location_id': appointment_location_id,
    'boolean': boolean,
    'file_upload': file_upload,
    'money': money
}     