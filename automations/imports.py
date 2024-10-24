from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging, time, re, requests,json, traceback, os, chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

Global_Variables = {
    'url': 'https://deploy-20240619--079f7edd.visachinaonline.com',
    'applicants': 5,
    'Country': "US",
    'Email': "",
    'First_name' : 'Pedro',
    'Last_name' : 'Gonzalez',
    'Passport_num' : '123456789',
    'N. Orders': 0,
    'Order_Numbers': [],
    'App_Version': '',
    'Status': ''
}

def date_selector(wait, slug):
    if slug == 'dob':
        dob_day = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + slug + '.day'))))
        dob_day.select_by_value('10')
        dob_month = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + slug + '.month'))))
        dob_month.select_by_value('10')
        dob_year = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + slug + '.year'))))
        dob_year.select_by_value("2000") 
def take_screenshot(driver, step):
    driver.save_screenshot(os.getcwd() + f'/automations/Applications/saved_screenshots/Correct/screenshot_{step}.png')
def setArguments(data):
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
        if x['type'] == 'App':
            Global_Variables['App_Version'] = x['value']

def try_multiple_selectors(driver, slug, action, *action_args):
    attempts = 0
    max_attempts = 3
    while max_attempts > attempts:
        if attempts == 0:
            try:
                WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.NAME, 'applicant.0.' + slug)))
                element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + slug)))
                action_method = getattr(element, action)
                action_method(*action_args)
                return True
            except:
                attempts += 1
        elif attempts == 1:
            try:
                WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.NAME, 'general.' + slug)))
                element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.NAME, 'general.' + slug)))
                action_method = getattr(element, action)
                action_method(*action_args)
                return True
            except:
                attempts += 1
        else:
            return True
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

def send_result(result, e):
    if result == 'Success':
        automation_results = {
            'Order_numbers' : Global_Variables['Order_Numbers'],
            'Status' : 'Success',
            'order_status' : Global_Variables['Status'],
            'email' : Global_Variables['Email'],
        }
        requests.post('http://127.0.0.1:5000' + '/check-automation-status',json=automation_results, headers={'Content-type': 'application/json', 'Accept': 'text/plain'})
    else:
        requests.post('http://127.0.0.1:5000' + '/check-automation-status',json={'ERROR': str(e).splitlines()[0], 'Status' : 'Failed'}, headers={'Content-type': 'application/json', 'Accept': 'text/plain'})
        logging.debug('Debug message: %s', e)
        logging.error('Error occurred: %s', traceback.format_exc())
        print(str(e).splitlines()[0])

def app_questions(url, product_num, app_version):
    response = requests.post(url + '/mobile_api/product/'+ str(product_num) +'/product_questions', headers={
        'mobile-app-version': app_version,
        'Device-OS-Version':'13',
        'Device-Platform':'ios',
        'Cookie':'remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=1693eyJpdiI6IjRnRjFyeUpBb2x1ZkYyeVJzV0J6d3c9PSIsInZhbHVlIjoiMnc3TGtYbmlvbnZ3KzFmSFAzSm4waUY2WWptSkJtMERCM2FPWjA2aFlGYUNrQ1JZandZYW9NRTZKRnEyZWVJRWY0UlQwNGYrMjFTY3d5aGVXNjFta0ZjeFFNVFVjaFdQZE1DVVRSb1BVdkd1WEVwc09qSzAwUk92a2VuaW1MZml2c1JBRVJxUzVSREhFM0J0WjRPQzI1cVgxVzRWeTQvZWdxanNybGVEam4wcW9WcHhXQU1xa3NySHR6RHFrbzUxak5JS0hyK1NlNzArKzVaY2NWOWdVNVZoSU9FVGdoSklLbHFTVU1GMm90QT0iLCJtYWMiOiJlMjQ4MmFiYTgyMWFlODY5YzFlZmRhYWRhYzA2ZDE3YzQ4NWVkZGM1OTdhZTYyOWE5NTY0YzVhZjhmMmUxNDZiIiwidGFnIjoiIn0=',
        'mobile-app-type':'visa',
        'Accept':'application/json'
    })
    data = json.loads(response.content)
    return data

def step_1_dates(wait, slug, browser):
    dates_calendar = wait.until(EC.element_to_be_clickable((By.NAME, "general." + slug)))
    dates_calendar.click()
    svg_locator = (By.CSS_SELECTOR, "div.is-right svg")
    if slug == 'arrival_date':
        day_month = (By.CSS_SELECTOR, "div.day-13")
    else:
        day_month = (By.CSS_SELECTOR, "div.day-18")
    safe_element_click(browser, svg_locator)
    safe_element_click(browser, day_month)

def questions_loop(product_num, browser, wait, num_order_loop, applicants):
    questions = app_questions(Global_Variables['url'], product_num, Global_Variables['App_Version'])
    sections_arr = []
    values_arr = []
    num_screenshot = 0
    for key,value in questions['questions'].items():
        values_arr.append(value)
        sections_arr.append(value.get('multipart_section'))
    for section in sections_arr:
        current_url = browser.current_url
        if "=" in current_url:
            arr_section_questions = [item for item in values_arr if item["multipart_section"] in current_url]
        else:
            arr_section_questions = [item for item in values_arr if item["multipart_section"] in "general_after_payment"]
        for question in arr_section_questions: 
            num_screenshot += 1
            take_screenshot(browser, str(num_screenshot))
            if question['slug'] == 'arrival_date':
                step_1_dates(wait, question['slug'], browser)
            elif question['slug'] == 'departure_date': 
                step_1_dates(wait, question['slug'], browser)
            elif question['field_type'] == 'email':
                try: 
                    if len(browser.find_elements(By.NAME, 'applicant.0.' + question['slug'])) > 0:
                        email = WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'])))
                        email.send_keys(Global_Variables['Email'])
                    else: 
                        email = WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.NAME, 'general.' + question['slug'])))
                        email.send_keys(Global_Variables['Email'])
                except:
                    pass
            elif question['slug'] == 'dob':
                date_selector(wait, question['slug'])
            elif question['field_type'] == 'textbox':
                try_multiple_selectors(browser, question['slug'], 'send_keys', 'aaaaaa')
            elif question['slug'] == 'passport_num':
                try_multiple_selectors(browser, question['slug'], 'send_keys', 'aaaaaa')
            elif question['field_type'] == 'fieldset_repeat':
                attempts = 0
                max_attempts = 2  
                while attempts < max_attempts:
                    if attempts == 0:
                        try:
                            WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, '//div[@data-ivisa-question-selector="applicant' + '.0.' + question['slug'] + '"]')))
                            for field in question['fieldset']:
                                if field['field_type'] == 'textbox':
                                    input_field = wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'] + '.0.'+ field['slug'])))
                                    input_field.send_keys('aaaaa')
                                if field['field_type'] == 'dropdown' or field['field_type'] == 'dropdown_country':
                                    dropdown_general = wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'] + '.0.'+ field['slug'])))
                                    dropdown_general.click()
                                    dropdown_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@data-handle="dropdown-applicant.' + '0.' + question['slug'] + '.0.'+ field['slug'] + '"]')))
                                    dropdown_input.send_keys(Keys.ARROW_DOWN)
                                    dropdown_input.send_keys(Keys.ENTER)
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
                                elif 'dob' in field['slug']:
                                    dob_day = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant' + '.0.' + question['slug'] + '.0.' + field['slug'] + '.day'))))
                                    dob_day.select_by_value('10')
                                    dob_month = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant' + '.0.' + question['slug'] + '.0.' + field['slug'] + '.month'))))
                                    dob_month.select_by_value('10')
                                    dob_year = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant' + '.0.' + question['slug'] + '.0.' + field['slug'] +'.year'))))
                                    dob_year.select_by_value("2000") 
                            attempts = 2 
                        except:
                            attempts += 1
                    elif attempts == 1:
                        try:
                            WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, '//div[@data-ivisa-question-selector="general.' + question['slug'] + '"]')))
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
                            attempts = 2
                        except:
                            attempts += 1
            elif question['field_type'] == 'phone':
                attempts = 0
                max_attempts = 2
                while max_attempts > attempts:
                    if attempts == 0: 
                        try:
                            WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.NAME, "general." + question['slug'])))
                            wait.until(EC.visibility_of_element_located((By.XPATH,'//div[@data-handle="filter-value"]'))).click()
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
                            WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.NAME, "applicant" + '.0.' + question['slug'])))
                            wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@name="applicant.0.'+ question['slug'] + '"]' + '//div[@data-handle="filter-value"]'))).click()
                            input_code = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@data-handle="dial-codes"]')))
                            input_code.send_keys("+52")
                            input_code.send_keys(Keys.ARROW_DOWN)
                            input_code.send_keys(Keys.ENTER)
                            input_field = wait.until(EC.element_to_be_clickable((By.NAME, 'telephone')))
                            input_field.send_keys('11111111') 
                            input_field.send_keys(Keys.ENTER)
                            attempts = 2
                        except: 
                            attempts = 2
            elif question['field_type'] == 'dropdown' or question['field_type'] == 'dropdown_country' and question['multipart_section'] != 'step_3c':
                attempts = 0
                max_attempts = 4 
                while attempts < max_attempts:
                    if question['options'] and len(question['options']) >= 5:
                        if attempts == 0:
                            try:
                                dropdown_general = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, '//select[@data-handle="dropdown-general.' + question['slug'] + '"]')))
                                if question['prevent_submission_if'] == None:
                                    Select(dropdown_general).select_by_index(0)
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
                                    Select(dropdown_general).select_by_index(0)
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
                                attempts = 4
            elif question['slug'] == "gender" and "continue" in current_url:
                WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, '//div[@data-ivisa-question-selector="applicant' + '.0.' + question['slug'] + '"]')))
                div_dropdown = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@data-ivisa-question-selector="applicant' + '.0.' + question['slug'] + '"]')))
                options_inside = div_dropdown.find_elements(By.TAG_NAME, 'button')
                options_inside[0].click()
            elif 'expiration' in question['slug'] or 'departure_date' in question['slug']:
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
                            passport_expiration_year.select_by_value("2025") 
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
                            passport_expiration_year.select_by_value("2025") 
                            attempts = 2 
                        except:
                            attempts += 1
            elif question['field_type'] == "address":
                if question['show_if'] is None:
                    time.sleep(2)
                    input_field = wait.until(EC.element_to_be_clickable((By.NAME, 'applicant' + '.0.' + question['slug'])))
                    browser.execute_script("arguments[0].value = '136 West 40th Street';", input_field)
                    input_field.click()
                    input_field.send_keys(Keys.SPACE)
                    api_google = wait.until(EC.visibility_of_element_located((By.ID, 'autocomplete_results')))
                    select_option = api_google.find_elements(By.TAG_NAME, 'li')
                    select_option[0].click()
                    time.sleep(2)
                else:
                    try:
                        time.sleep(2)
                        input_field =  WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.NAME, 'applicant' + '.0.' + question['slug'])))
                        browser.execute_script("arguments[0].value = '136 West 40th Street';", input_field)
                        input_field.click()
                        input_field.send_keys(Keys.SPACE)
                        api_google = wait.until(EC.visibility_of_element_located((By.ID, 'autocomplete_results')))
                        select_option = api_google.find_elements(By.TAG_NAME, 'li')
                        select_option[0].click()
                        time.sleep(2)
                    except:
                        pass
            elif question['slug'] == 'appointment_location_id':
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
            elif question['field_type'] == "boolean":
                attempts = 0
                max_attempts = 2
                while attempts < max_attempts:
                    if attempts == 0:
                        try: 
                            boolean = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.NAME, "applicant.0." + question["slug"])))
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
                            boolean = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.NAME, "general." + question["slug"])))
                            buttons_inside = boolean.find_elements(By.TAG_NAME, "button")
                            if question['prevent_submission_if'] == None:
                                buttons_inside[1].click()
                            else:
                                prevent_values = question["prevent_submission_if"]["value"]
                                buttons_inside[0].click() if prevent_values[0] == "No" else buttons_inside[1].click()
                            attempts = 2
                        except:
                            attempts += 1
            elif question['field_type'] == 'file_upload' and question['slug'] == "passport_photo":
                try:
                    file_upload_button = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.ID, "btn-applicant.0." + question["slug"])))
                    file_upload_button.click()
                    time.sleep(3)
                    file_upload_in = browser.find_elements(By.NAME, 'applicant.0.' + question["slug"])
                    get_image = os.path.abspath('automations/Applications/uploads/Applicant-Photo.jpg')
                    file_upload_in[0].send_keys(get_image)
                    accept_upload = WebDriverWait(browser, 120).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-handle="acceptFileUploadBtn"]')))
                    accept_upload.click()
                except:
                    pass
            elif question['field_type'] == 'file_upload':
                try: 
                    file_upload_button = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.ID, "btn-applicant.0." + question["slug"])))
                    file_upload_button.click()
                    time.sleep(3)
                    file_upload_in = browser.find_elements(By.NAME, 'applicant.0.' + question["slug"])
                    get_image = os.path.abspath('automations/Applications/uploads/1.jpg')
                    file_upload_in[0].send_keys(get_image)
                    accept_upload = WebDriverWait(browser, 120).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-handle="acceptFileUploadBtn"]')))
                    accept_upload.click()
                except:
                    pass
            elif 'issued' in question['slug']:
                if question['show_if'] is None:
                    try:
                        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.NAME, 'applicant.0.' + question['slug'] + '.day')))
                        for user_expiration in range(applicants):
                            passport_expiration_day = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant' + '.' + str(user_expiration) + '.' + question['slug'] + '.day'))))
                            passport_expiration_day.select_by_value('10')
                            passport_expiration_month = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant' + '.' + str(user_expiration) + '.' + question['slug'] + '.month'))))
                            passport_expiration_month.select_by_value('10')
                            passport_expiration_year = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant' + '.' + str(user_expiration) + '.' + question['slug'] + '.year'))))
                            passport_expiration_year.select_by_value("2020") 
                    except:
                        pass
                else:
                    try:
                        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.NAME, 'applicant.0.' + question['slug'] + '.day')))
                        for user_expiration in range(applicants):
                            passport_expiration_day = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant' + '.' + str(user_expiration) + '.' + question['slug'] + '.day'))))
                            passport_expiration_day.select_by_value('10')
                            passport_expiration_month = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant' + '.' + str(user_expiration) + '.' + question['slug'] + '.month'))))
                            passport_expiration_month.select_by_value('10')
                            passport_expiration_year = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant' + '.' + str(user_expiration) + '.' + question['slug'] + '.year'))))
                            passport_expiration_year.select_by_value("2020") 
                    except:
                        pass
        if "review" in current_url:
            try:
                WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element((By.ID, 'app'), 'Possible Duplicate'))
                btn_disclaimer = wait.until(EC.element_to_be_clickable((By.ID, "btnDisclaimerNext")))
                btn_disclaimer.click()
                continue_sidebar = wait.until(EC.visibility_of_element_located((By.ID, "btnContinueSidebar")))
                continue_sidebar.click() if continue_sidebar.is_enabled() else wait.until(EC.element_to_be_clickable((By.ID, "btnContinueSidebar"))).click()
                btn_submit_payment = wait.until(EC.element_to_be_clickable((By.ID, "btnSubmitPayment")))
                btn_submit_payment.click()
                wait.until(lambda driver: driver.current_url != current_url) 
            except: 
                continue_sidebar = wait.until(EC.visibility_of_element_located((By.ID, "btnContinueSidebar")))
                continue_sidebar.click() if continue_sidebar.is_enabled() else wait.until(EC.element_to_be_clickable((By.ID, "btnContinueSidebar"))).click()
                btn_submit_payment = wait.until(EC.element_to_be_clickable((By.ID, "btnSubmitPayment")))
                btn_submit_payment.click()
                wait.until(lambda driver: driver.current_url != current_url) 
        elif "continue" in current_url:
            try: 
                WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.ID, "btnContinueUnderSection"))).click() 
                num_screenshot += 1
                take_screenshot(browser, str(num_screenshot))
                wait.until(lambda driver: driver.current_url != current_url) 
            except:
                wait.until(EC.element_to_be_clickable((By.ID, "btnSubmitApplication"))).click() 
                wait.until(lambda driver: driver.current_url != current_url)
                wait.until(EC.element_to_be_clickable((By.ID, "btnDismissAppDownload"))).click() 
                wait.until(lambda driver: driver.current_url != current_url)
                order_num = wait.until(EC.visibility_of_element_located((By.ID, "h1-tag-container")))
                Global_Variables['Order_Numbers'].append(re.findall(r'\d+', order_num.text))
                num_screenshot += 1
                take_screenshot(browser, str(num_screenshot))
                break
        else:
            continue_sidebar = wait.until(EC.visibility_of_element_located((By.ID, "btnContinueSidebar")))
            continue_sidebar.click() if continue_sidebar.is_enabled() else wait.until(EC.element_to_be_clickable((By.ID, "btnContinueSidebar"))).click()
            num_screenshot += 1
            take_screenshot(browser, str(num_screenshot))
            wait.until(lambda driver: driver.current_url != current_url) 
##https://costumer-facing1-production.up.railway.app
##https://costumer-facing1-automations-pr-6.up.railway.app
##http://127.0.0.1:5000