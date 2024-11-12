from .global_imports import *

def take_screenshot(driver, step):
    driver.save_screenshot(os.getcwd() + f'/automations/Applications/saved_screenshots/Correct/screenshot_{step}.png')
def MIN(orders_num, url):
    chrome_options = Options()
    chrome_options.add_argument('--headless') 
    chrome_options.add_argument('window-size=1920,1080')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    wait = WebDriverWait(browser, 60)
    browser.get(url + '/admin')
    login_email = wait.until(EC.visibility_of_element_located((By.ID, 'email_login_input')))
    login_email.send_keys('test@admin.com')
    continue_btn = wait.until(EC.element_to_be_clickable((By.ID, 'continue_button')))
    continue_btn.click()
    login_password = wait.until(EC.visibility_of_element_located((By.ID, 'password_login_input')))
    login_password.send_keys('testivisa5!')
    login_btn = wait.until(EC.element_to_be_clickable((By.ID, 'log_in_button')))
    login_btn.click()

    for order in orders_num:
        search_order = wait.until(EC.element_to_be_clickable((By.XPATH, '//li[@onclick="searchOrderID();"]')))
        search_order.click()
        send_order_num = Alert(browser)
        send_order_num.send_keys(order[0])
        send_order_num.accept()
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'h1')))
        take_screenshot(browser, "admin_1")
        info_details = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@data-handle="dl-info-title"]')))
        info_details.click()
        info_user = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@data-handle="applicant-details"]')))
        info_user.click()
        min_first_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@data-handle="min_checkbox_first_name"]')))
        min_first_name.click()
        take_screenshot(browser, "admin_2")
        select_min_reason = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[@data-handle="Non-English characters"]')))
        select_min_reason.click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//label[@data-handle="Non-English characters"]')))
        take_screenshot(browser, "admin_3")
        close_modal = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-handle="close-modal"]')))
        close_modal.click()
        wait.until(EC.element_to_be_clickable((By.NAME, 'change-status')))
        take_screenshot(browser, "admin_4")
        Select(browser.find_element(By.NAME, 'change-status')).select_by_value("info_needed")
        
        go_trough_MIN = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-handle="minModalYes"]')))
        go_trough_MIN.click()
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'textarea')))
        take_screenshot(browser, "admin_5")
        submit_Min = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-handle="submitChangeStatus"]')))
        submit_Min.click()
        take_screenshot(browser, "admin_6")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@data-vue-component="filterable-list"]')))
        take_screenshot(browser, "admin_7")

status_func = {
    'MIN': MIN,
    #'Wog': WOG,
    #'Scheduling': Scheduling,
    #'Scheduled': Scheduled,
    #'Incomplete': Incomplete,
}