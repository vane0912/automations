import logging, time, re, requests,json
from .Global_Variables import values, safe_element_click
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, ElementClickInterceptedException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select

def test(test1):
    chrome_options = Options()
    #chrome_options.add_argument('--headless') 
    chrome_options.add_argument('window-size=1920,1080')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    wait = WebDriverWait(browser, 150, ignored_exceptions=(NoSuchElementException,StaleElementReferenceException))
    
    response = requests.post('https://deploy-20240711--086a1fb5.visachinaonline.com/mobile_api/product/10845/product_questions', headers={
        'mobile-app-version':'4.5.5',
        'Device-OS-Version':'13',
        'Device-Platform':'ios',
        'Cookie':'remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=1693eyJpdiI6IjRnRjFyeUpBb2x1ZkYyeVJzV0J6d3c9PSIsInZhbHVlIjoiMnc3TGtYbmlvbnZ3KzFmSFAzSm4waUY2WWptSkJtMERCM2FPWjA2aFlGYUNrQ1JZandZYW9NRTZKRnEyZWVJRWY0UlQwNGYrMjFTY3d5aGVXNjFta0ZjeFFNVFVjaFdQZE1DVVRSb1BVdkd1WEVwc09qSzAwUk92a2VuaW1MZml2c1JBRVJxUzVSREhFM0J0WjRPQzI1cVgxVzRWeTQvZWdxanNybGVEam4wcW9WcHhXQU1xa3NySHR6RHFrbzUxak5JS0hyK1NlNzArKzVaY2NWOWdVNVZoSU9FVGdoSklLbHFTVU1GMm90QT0iLCJtYWMiOiJlMjQ4MmFiYTgyMWFlODY5YzFlZmRhYWRhYzA2ZDE3YzQ4NWVkZGM1OTdhZTYyOWE5NTY0YzVhZjhmMmUxNDZiIiwidGFnIjoiIn0=',
        'mobile-app-type':'visa',
        'Accept':'application/json'
    })
    data = json.loads(response.content)
    arr = []
    browser.get(values['url'] + '/china/apply-now')
    
    nationality = wait.until(EC.element_to_be_clickable((By.NAME, 'general.common_nationality_country')))
    nationality.click()
    nationality_values = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@data-handle='dropdown-general.common_nationality_country']")))
    nationality_values.send_keys(values['Country'], Keys.ENTER)
    product = Select(wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@data-handle='dropdown-general.visa_type_id']"))))
    product.select_by_index(0)
    div_continue_btn = wait.until(EC.visibility_of_element_located((By.ID, "btnContinueUnderSection")))
    
    div_continue_btn.find_element(By.TAG_NAME, 'button').click() if div_continue_btn.find_element(By.TAG_NAME, 'button').is_enabled() else wait.until(EC.element_to_be_clickable((div_continue_btn.find_element(By.TAG_NAME, 'button')))).click()

    for key,value in data['questions'].items():
        if value.get('multipart_section') == 'step_1':
            arr.append(value)

    return arr

##requests.post('http://127.0.0.1:5000' + '/check-automation-status',
    ##json={'Status': 'Failed'}, 
    ##headers={'Content-type': 'application/json', 'Accept': 'text/plain'})