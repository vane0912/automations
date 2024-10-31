from ..imports import *
from ..status_functions import *
def India_1y_Multiple(data):
    setArguments(data)
    
    Global_Variables['Order_Numbers'] = []
    chrome_options = Options()
    #chrome_options.add_argument('--headless') 
    chrome_options.add_argument('window-size=1920,1080')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    wait = WebDriverWait(browser, 90)
    try:
        for order in range(int(Global_Variables['N. Orders'])):
            browser.get(Global_Variables['url'] + '/india/apply-now')
            current_url = browser.current_url
            if order == 0:
                nationality = wait.until(EC.element_to_be_clickable((By.NAME, 'general.common_nationality_country')))
                nationality.click()
                nationality_values = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@data-handle='dropdown-general.common_nationality_country']")))
                nationality_values.send_keys(Global_Variables['Country'], Keys.ENTER)
            Select(wait.until(EC.visibility_of_element_located((By.XPATH, '//select[@data-handle="dropdown-general.visa_type_id"]')))).select_by_value('21')
            # New design step_1 selector
            #product = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-handle="vt-22"]')))
            #product.click()
            try:
                WebDriverWait(browser, 15).until(lambda driver: driver.current_url != current_url)  
            except:
                wait.until(EC.element_to_be_clickable((By.ID, "btnContinueUnderSection"))).click()
                wait.until(lambda driver: driver.current_url != current_url)
            try:
                questions_loop(10119, browser, wait, order, 1)
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
                    if Global_Variables['Status'] == 'MIN':
                        try:
                            MIN(Global_Variables['Order_Numbers'], Global_Variables['url'])
                            send_result('Success', '')
                        except Exception as e:
                            browser.get_screenshot_as_file(os.getcwd() + '/automations/Applications/saved_screenshots/Error/error.png')
                            send_result('Failed',e)
                            break
                    else:
                        send_result('Success', '')
            except Exception as e:
                browser.get_screenshot_as_file(os.getcwd() + '/automations/Applications/saved_screenshots/Error/error.png')
                send_result('Failed',e)
                break
    except Exception as e:
        browser.get_screenshot_as_file(os.getcwd() + '/automations/Applications/saved_screenshots/Error/error.png')
        send_result('Failed',e)