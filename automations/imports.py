from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging, time, re, requests,json, traceback, os, chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, ElementClickInterceptedException, TimeoutException, ElementNotInteractableException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
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

def success_request():
    automation_results = {
        'Order_numbers' : Global_Variables['Order_Numbers'],
        'Status' : 'Success',
        'order_status' : Global_Variables['Status'],
        'email' : Global_Variables['Email'],
    }
    requests.post('http://127.0.0.1:5000' + '/check-automation-status',json=automation_results, headers={'Content-type': 'application/json', 'Accept': 'text/plain'})

def failed_request(e):
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


def questions_loop(product_num, browser, wait, num_order_loop):
    questions = app_questions(Global_Variables['url'], product_num, Global_Variables['App_Version'])
    sections_arr = []
    values_arr = []
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
            elif question['slug'] == 'email' and num_order_loop == 0:
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
            elif question['field_type'] == 'phone':
                wait.until(EC.visibility_of_element_located((By.NAME, "general." + question['slug'])))
                input_field = wait.until(EC.element_to_be_clickable((By.NAME, 'telephone')))
                input_field.send_keys('11111111') 
                input_field.send_keys(Keys.ENTER)
                wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-handle="boolean-I do not wish to receive text messages"]'))).click()
            elif question['field_type'] == 'dropdown' and question['show_if'] is None:
                if len(question['options']) > 5:
                    dropdown_general = wait.until(EC.element_to_be_clickable((By.NAME, 'general.' + question['slug'])))
                    dropdown_general.click()
                    dropdown_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@data-handle="dropdown-general.' + question['slug'] + '"]')))
                    dropdown_input.send_keys(Keys.ARROW_DOWN)
                    dropdown_input.send_keys(Keys.ENTER)
                
            elif 'expiration' in question['slug']:
                passport_expiration_day = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'] + '.day'))))
                passport_expiration_day.select_by_value('10')
                passport_expiration_month = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'] + '.month'))))
                passport_expiration_month.select_by_value('10')
                passport_expiration_year = Select(wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'] + '.year'))))
                passport_expiration_year.select_by_value("2028") 
            elif question['slug'] == 'appointment_location_id':
                time.sleep(3)
                input_field_speciality = wait.until(EC.element_to_be_clickable((By.NAME, 'applicant.0.' + question['slug'] + '_autocomplete')))
                browser.execute_script("arguments[0].value = 'New York, EE. UU';", input_field_speciality)
                input_field_speciality.click()
                input_field_speciality.send_keys(Keys.SPACE)
                api_google = wait.until(EC.visibility_of_element_located((By.ID, 'autocomplete_results')))
                select_option = api_google.find_elements(By.TAG_NAME, 'li')
                select_option[0].click()
                try:
                    runner_pilot = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-handle="boolean-No, I want to go to the embassy myself"]')))
                    runner_pilot.click()
                except:
                    passport_expiration_year = Select(wait.until(EC.element_to_be_clickable((By.XPATH, '//select[@data-handle="dropdown-applicant.0.runner_pilot"]'))))
                    passport_expiration_year.select_by_value("No") 
        if "review" in current_url:
            try:
                WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, 'app'), 'Possible Duplicate'))
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
            wait.until(EC.element_to_be_clickable((By.ID, "btnContinueUnderSection"))).click() 
            wait.until(lambda driver: driver.current_url != current_url) 
        else:
            continue_sidebar = wait.until(EC.visibility_of_element_located((By.ID, "btnContinueSidebar")))
            continue_sidebar.click() if continue_sidebar.is_enabled() else wait.until(EC.element_to_be_clickable((By.ID, "btnContinueSidebar"))).click()
            wait.until(lambda driver: driver.current_url != current_url) 
##https://costumer-facing1-production.up.railway.app
##https://costumer-facing1-automations-pr-6.up.railway.app
##http://127.0.0.1:5000