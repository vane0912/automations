from ..imports import *
from ..status_functions import *
def India_Business_eVisa(data):
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
            try:
                run_orders(browser, wait, order, 10120, '22', Global_Variables['Country'], '/india/apply-now')
            except Exception as e:
                browser.get_screenshot_as_file(os.getcwd() + '/automations/Applications/saved_screenshots/Error/error.png')
                send_result('Failed',e)
    except Exception as e:
        browser.get_screenshot_as_file(os.getcwd() + '/automations/Applications/saved_screenshots/Error/error.png')
        send_result('Failed',e)