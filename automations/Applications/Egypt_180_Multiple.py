from ..imports import *
def EG_180_Multiple(data):
    setArguments(data)
    
    Global_Variables['Order_Numbers'] = []
    chrome_options = Options()
    chrome_options.add_argument('--headless') 
    chrome_options.add_argument('window-size=1920,1080')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    wait = WebDriverWait(browser, 60)
    try:
        for order in range(int(Global_Variables['N. Orders'])):
            browser.get(Global_Variables['url'] + '/egypt/apply-now')
            current_url = browser.current_url
            if order == 0:
                nationality = wait.until(EC.element_to_be_clickable((By.NAME, 'general.common_nationality_country')))
                nationality.click()
                nationality_values = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@data-handle='dropdown-general.common_nationality_country']")))
                nationality_values.send_keys(Global_Variables['Country'], Keys.ENTER)
            product = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-handle="vt-17"]')))
            product.click()
            #wait.until(EC.element_to_be_clickable((By.ID, "btnContinueUnderSection"))).click() 
            wait.until(lambda driver: driver.current_url != current_url) 
            try:
                questions_loop(10115, browser, wait, order, 1)
                send_result('Success', '')
            except Exception as e:
                browser.get_screenshot_as_file(os.getcwd() + '/automations/Applications/saved_screenshots/Error/error.png')
                send_result('Failed',e)
                break
    except Exception as e:
        send_result('Failed',e)