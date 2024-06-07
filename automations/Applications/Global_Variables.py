import time, pyautogui
url = 'https://deploy-20240610--73a8cdd1.visachinaonline.com'
#Screen sizes
screen_size = pyautogui.size()
mobile_320 = (448, 174)
mobile_375 = (618, 177)
mobile_425 = (641,177)
tablet_768 = (679,181)
desktop_resolutions = (853, 178)
# Personal Data
country = "MX"
email_txt = "test1@mailinator.com"
first_name_txt = "Pedro"
last_name_txt = "Gonzalez"
passport_num = "123456789"

values = {
    'Country': "MX",
    'Email': "test@mailinator.com",
    'First_name' : 'Pedro',
    'Last_name' : 'Gonzalez',
    'Passport_num' : '123456789'   
}