from ..imports import *
from ..status_functions import *
def TR_App_P2(data):
    setArguments(data)
    
    Global_Variables['Order_Numbers'] = []
    chrome_options = Options()
    chrome_options.add_argument('--headless') 
    chrome_options.add_argument('window-size=1920,1080')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    wait = WebDriverWait(browser, 50)
    
    try:
        for order in range(int(Global_Variables['N. Orders'])):
            browser.get(Global_Variables['url'] + '/turkey/apply-now')
            current_url = browser.current_url
            if order == 0:
                nationality = wait.until(EC.element_to_be_clickable((By.NAME, 'general.common_nationality_country')))
                nationality.click()
                nationality_values = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@data-handle='dropdown-general.common_nationality_country']")))
                nationality_values.send_keys('MX', Keys.ENTER)
            product = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-handle="vt-38"]')))
            product.click()
            #wait.until(EC.element_to_be_clickable((By.ID, "btnContinueUnderSection"))).click() 
            wait.until(lambda driver: driver.current_url != current_url) 
            try:
                questions_loop(10135, browser, wait, order, 1)
                if order == 0:
                    browser.get(Global_Variables['url'] + '/account/settings/security')
                    password = wait.until(EC.visibility_of_element_located((By.ID, 'new_password')))
                    password.send_keys('testivisa5!')
                    password_repeat = wait.until(EC.visibility_of_element_located((By.ID, 'password_repeat')))
                    password_repeat.send_keys('testivisa5!')
                    confirm_password = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-handle="updatePasswordBtn"]')))
                    confirm_password.click()
                    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'swal-modal')))
                if order == int(Global_Variables['N. Orders']) - 1:
                    MIN(Global_Variables['Order_Numbers'])
                    send_result('Success', '')
        
            except Exception as e:
                browser.get_screenshot_as_file(os.getcwd() + '/automations/Applications/saved_screenshots/Error/error.png')
                send_result('Failed',e)
                break
    except Exception as e:
        send_result('Failed',e)