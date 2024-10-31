from ..imports import *
def doc_upload(url):
    chrome_options = Options()
    #chrome_options.add_argument('--headless') 
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

        info_details = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@data-handle="dl-info-title"]')))
        info_details.click()
        browser.save_screenshot('/Users/Chapis/Desktop/Automation/Automation/automations/Admin/Orders_page/' + 'see_user_order_2.png')
        info_user = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@data-handle="applicant-details"]')))
        info_user.click()
        user_doc_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-handle="show-docs-applicant-0"]')))
        user_doc_btn.click()
        
        doc_type = Select(wait.until(EC.element_to_be_clickable((By.XPATH, '//select[@data-handle="upload-docs-0"]'))))
        doc_type.select_by_index(2)

        input_file = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@data-handle="deliverable-upload-applicant-0"]')))
        get_image = os.path.abspath('automations/Applications/uploads/Applicant-Photo.jpg')
        input_file.send_keys(get_image)

        upload_file = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-handle="save-uploaded-docs-0"]')))
        upload_file.click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@data-handle="deliverable-upload-applicant-0"]')))
        send_result('Success', '')
    except Exception as e:
        browser.save_screenshot('/Users/Chapis/Desktop/Automation/Automation/automations/Admin/Errors/' + 'error_images.png')
        send_result('Error', e)