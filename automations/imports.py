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

def form_XPATH(type, slug):
    string = ''
    print(slug)
    if 'dropdown' in type:
        string = '//select[@data-handle="dropdown-general.' + slug + '"]'
    elif 'textbox' in type:
        string = "applicant." + slug 
    else:
        string = 'hello'
    print(string)
##https://costumer-facing1-production.up.railway.app
##https://costumer-facing1-automations-pr-6.up.railway.app
##http://127.0.0.1:5000