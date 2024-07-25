
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#url = 'https://deploy-20240610--73a8cdd1.visachinaonline.com'
#Screen sizes
#screen_size = pyautogui.size()
#mobile_320 = (448, 174)
#mobile_375 = (618, 177)
#mobile_425 = (641,177)
#tablet_768 = (679,181)
#desktop_resolutions = (853, 178)
## Personal Data
#country = "MX"
#email_txt = "test2@mailinator.com"
#first_name_txt = "Pedro"
#last_name_txt = "Gonzalez"
#passport_num = "123456789"


Global_Variables = {
    'url': 'https://deploy-20240619--079f7edd.visachinaonline.com',
    'applicants': 5,
    'Country': "MX",
    'Email': "",
    'First_name' : 'Pedro',
    'Last_name' : 'Gonzalez',
    'Passport_num' : '123456789',
    'N. Orders': 0,
    'Order_Numbers': [],
    'Status': ''
}
def safe_element_click(driver, locator):
    attempts = 0
    max_attempts = 3  
    while attempts < max_attempts:
        try:
            element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
            element.click()
            return True  # Click successful, return True
        except EC.StaleElementReferenceException:
            print(f"StaleElementReferenceException occurred, retrying attempt {attempts + 1}")
            attempts += 1
    print(f"Failed to click element after {max_attempts} attempts")
    return False 
