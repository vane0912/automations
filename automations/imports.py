from .selector_functions import selectors
from .status_functions import status_func
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
from selenium.webdriver.common.alert import Alert


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
    'App_Version': '4.8.2',
    'Status': ''
}

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

def run_orders(browser, wait, num_order, product_num, select_num, country, country_url):
    browser.get(Global_Variables['url'] + country_url)
    current_url = browser.current_url
    if num_order == 0:
        nationality = wait.until(EC.element_to_be_clickable((By.NAME, 'general.common_nationality_country')))
        nationality.click()
        nationality_values = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@data-handle='dropdown-general.common_nationality_country']")))
        nationality_values.send_keys(country, Keys.ENTER)
    Select(wait.until(EC.visibility_of_element_located((By.XPATH, '//select[@data-handle="dropdown-general.visa_type_id"]')))).select_by_value(select_num)
    # New design step_1 selector
    #product = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-handle="vt-22"]')))
    #product.click()
    try:
        wait.until(lambda driver: driver.current_url != current_url) 
    except:
        wait.until(EC.element_to_be_clickable((By.ID, "btnContinueUnderSection"))).click()
        wait.until(lambda driver: driver.current_url != current_url) 
    try:
        questions_loop(product_num, browser, wait, num_order, 1)
        if num_order == 0:
            browser.get(Global_Variables['url'] + '/account/settings/security')
            password = wait.until(EC.visibility_of_element_located((By.ID, 'new_password')))
            password.send_keys('testivisa5!')
            password_repeat = wait.until(EC.visibility_of_element_located((By.ID, 'password_repeat')))
            password_repeat.send_keys('testivisa5!')
            confirm_password = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-handle="updatePasswordBtn"]')))
            confirm_password.click()
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'swal-modal')))
        if num_order == int(Global_Variables['N. Orders']) - 1:
            if Global_Variables['Status'] in status_func:
                try:
                    status_func[Global_Variables['Status']](Global_Variables['Order_Numbers'], Global_Variables['url'])
                    send_result('Success', '')
                except Exception as e:
                    browser.get_screenshot_as_file(os.getcwd() + '/automations/Applications/saved_screenshots/Error/error.png')
                    send_result('Failed',e)
            else:
                send_result('Success', '')
    except Exception as e:
        browser.get_screenshot_as_file(os.getcwd() + '/automations/Applications/saved_screenshots/Error/error.png')
        send_result('Failed',e)
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
            if question['slug'] in selectors:
                selectors[question['slug']](question, wait, browser, Global_Variables)
            elif question['field_type'] in selectors:
                selectors[question['field_type']](question, wait, browser, Global_Variables)
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
                time.sleep(3)
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
