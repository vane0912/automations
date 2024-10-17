from ..imports import *
def check_orders(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless') 
    chrome_options.add_argument('window-size=1920,1080')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    wait = WebDriverWait(browser, 60)
    try:
        browser.get(url + '/admin')
        login_email = wait.until(EC.visibility_of_element_located((By.ID, 'email_login_input')))
        login_email.send_keys('test@admin.com')
        continue_btn = wait.until(EC.element_to_be_clickable((By.ID, 'continue_button')))
        continue_btn.click()
        login_password = wait.until(EC.visibility_of_element_located((By.ID, 'password_login_input')))
        login_password.send_keys('testivisa5!')
        login_btn = wait.until(EC.element_to_be_clickable((By.ID, 'log_in_button')))
        login_btn.click()

        orders_dropdown = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-handle="Orders"]')))
        orders_dropdown.click()
        see_all_orders_page = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@data-handle="All Orders"]')))
        see_all_orders_page.click()
        filter_component = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@data-vue-component="filterable-list"]')))
        browser.save_screenshot('/Users/Chapis/Desktop/Automation/Automation/automations/Admin/Orders_page/' + 'see_all_orders_page.png')
        get_tables = filter_component.find_elements(By.TAG_NAME, 'table')
        get_rows = get_tables[1].find_elements(By.TAG_NAME, 'tr')
        get_td = get_rows[0].find_elements(By.TAG_NAME, 'td')
        go_to_order_num = get_td[0].find_element(By.TAG_NAME, 'a')
        go_to_order_num.click()
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'h1')))
        browser.save_screenshot('/Users/Chapis/Desktop/Automation/Automation/automations/Admin/Orders_page/' + 'see_user_order_1.png')
        order_details = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@data-handle="dl-order-details-title"]')))
        order_details.click()
        payment_details = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@data-handle="dl-payment-details-title"]')))
        payment_details.click()
        status_details = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@data-handle="dl-status-changes-title"]')))
        status_details.click()
        order_data_details = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@data-handle="dl-order-data-changes-title"]')))
        order_data_details.click()
        order_annotations_details = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@data-handle="dl-order-annotations-title"]')))
        order_annotations_details.click()
        csa_details = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@data-handle="dl-csa-info-title"]')))
        csa_details.click()
        notes_details = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@data-handle="dl-notes-title"]')))
        notes_details.click()
        info_details = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@data-handle="dl-info-title"]')))
        info_details.click()
        browser.execute_script("window.scrollTo(0, 400)")
        browser.save_screenshot('/Users/Chapis/Desktop/Automation/Automation/automations/Admin/Orders_page/' + 'see_user_order_2.png')
        browser.execute_script("window.scrollTo(0, 800)")
        browser.save_screenshot('/Users/Chapis/Desktop/Automation/Automation/automations/Admin/Orders_page/' + 'see_user_order_3.png')
        browser.execute_script("window.scrollTo(0, 1500)")
        browser.save_screenshot('/Users/Chapis/Desktop/Automation/Automation/automations/Admin/Orders_page/' + 'see_user_order_4.png')
        browser.execute_script("window.scrollTo(0, 2200)")
        browser.save_screenshot('/Users/Chapis/Desktop/Automation/Automation/automations/Admin/Orders_page/' + 'see_user_order_5.png')
        browser.execute_script("window.scrollTo(0, 2700)")
        browser.save_screenshot('/Users/Chapis/Desktop/Automation/Automation/automations/Admin/Orders_page/' + 'see_user_order_6.png')
        send_result('Success', '')
    except Exception as e:
        browser.save_screenshot('/Users/Chapis/Desktop/Automation/Automation/automations/Admin/Errors/' + 'error_images.png')
        send_result('Error', e)