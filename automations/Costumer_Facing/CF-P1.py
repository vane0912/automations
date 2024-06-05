from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import automations.Global_Variables as Global_Variables
import time, pyautogui


def CF_P1():
    ## Open Ivisa page with selenium
    browser = webdriver.Chrome()
    browser.get(Global_Variables.url)
    time.sleep(4) 
    ## Move mouse to center of the screen
    pyautogui.click(Global_Variables.screen_size.width / 2, Global_Variables.screen_size.height / 2) 
    ## Screen full size
    pyautogui.hotkey('command', 'ctrl', 'f') 
    time.sleep(2)
    ## Accept cookies
    accept_cookies = browser.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
    accept_cookies.click()
    ## Open the inspector 
    time.sleep(2)
    pyautogui.hotkey('command', 'optionleft', 'i', interval = 0.25) 
    time.sleep(2)
    ## Toogle device tool bar
    pyautogui.hotkey('command','shift', 'm')
    ## Open Spotlight and search for OBS
    pyautogui.hotkey('command', 'space')
    pyautogui.write('OBS', interval=0.25)
    pyautogui.press('enter')
    time.sleep(10)
    ## Switch from Chrome to OBS
    pyautogui.keyDown('command')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
    pyautogui.keyUp('command')
    time.sleep(3)
    ## Start recording
    pyautogui.keyDown('option')
    pyautogui.keyDown('g')
    pyautogui.keyUp('option')
    pyautogui.keyUp('g')
    ## Mobile 320px resolution
    pyautogui.click(Global_Variables.mobile_320)
    pyautogui.hotkey('command','r')
    time.sleep(2)
    ## Scroll down
    pyautogui.moveTo(433,352)
    pyautogui.click()
    pyautogui.hotkey('option','up')
    for x in range(4):
        time.sleep(0.5)
        pyautogui.hotkey('option','down')
    ## Most popular destinations
    drag_position_x, drag_position_y = pyautogui.position()
    pyautogui.moveTo(drag_position_x, drag_position_y + 150)
    pyautogui.drag(-250, 0, 1, button='left')
    ## Keep scrolling
    for x in range(7):
        time.sleep(0.5)
        pyautogui.hotkey('option','down')
    ## Go to top of page
    time.sleep(0.5)
    pyautogui.hotkey('command', 'up')
    time.sleep(0.5)
    ## Mobile 375px
    pyautogui.click(Global_Variables.mobile_375)
    time.sleep(0.5)
    pyautogui.moveTo(433,352)
    pyautogui.click()
    for x in range(12):
        time.sleep(0.5)
        pyautogui.hotkey('option','down')
    ## Go to top of page
    time.sleep(0.5)
    pyautogui.hotkey('command', 'up')
    time.sleep(0.5)
    ## Mobile 425px
    pyautogui.click(Global_Variables.mobile_425)
    time.sleep(0.5)
    pyautogui.moveTo(433,352)
    pyautogui.click()
    for x in range(13):
        time.sleep(0.5)
        pyautogui.hotkey('option','down')
    ## Go to top of page
    time.sleep(0.5)
    pyautogui.hotkey('command', 'up')
    time.sleep(0.5)
    ## Tablet 768px
    pyautogui.click(Global_Variables.tablet_768)
    time.sleep(0.5)
    pyautogui.moveTo(433,352)
    pyautogui.click()
    for x in range(10):
        time.sleep(0.5)
        pyautogui.hotkey('option','down')
    ## Go to top of page
    time.sleep(0.5)
    pyautogui.hotkey('command', 'up')
    time.sleep(0.5)
    ## Desktop 1024px, 1440px, 2560px
    pyautogui.moveTo(Global_Variables.desktop_resolutions)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(433,352)
    pyautogui.click()
    for x in range(8):
        time.sleep(0.5)
        pyautogui.hotkey('option','down')
    ## Go to top of page
    time.sleep(0.5)
    pyautogui.hotkey('command', 'up')
    time.sleep(0.5)
    # 1440
    pyautogui.moveTo(Global_Variables.desktop_resolutions)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(433,352)
    pyautogui.click()
    for x in range(5):
        time.sleep(0.5)
        pyautogui.hotkey('option','down')
    ## Go to top of page
    time.sleep(0.5)
    pyautogui.hotkey('command', 'up')
    time.sleep(0.5)
    # 2560
    pyautogui.moveTo(Global_Variables.desktop_resolutions)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(433,280)
    pyautogui.click()
    for x in range(2):
        time.sleep(0.5)
        pyautogui.hotkey('option','down')
    ## Go to top of page
    time.sleep(0.5)
    pyautogui.hotkey('command', 'up')
    time.sleep(0.5)
    
    ## Ivisa Plus
    browser.get(Global_Variables.url + "/plus")
    ## Scroll page
    pyautogui.click()
    for x in range(2):
        time.sleep(0.5)
        pyautogui.hotkey('option','down')
    time.sleep(0.5)
    ## Mobile 320
    pyautogui.click(Global_Variables.mobile_320)
    pyautogui.hotkey('command','r')
    time.sleep(2)
    ## Scroll down
    pyautogui.moveTo(433,352)
    pyautogui.click()
    pyautogui.hotkey('option','up')
    for x in range(8):
        time.sleep(0.5)
        pyautogui.hotkey('option','down')
    ## Go to top of page
    time.sleep(0.5)
    pyautogui.hotkey('command', 'up')
    time.sleep(0.5)
    ## Mobile 375
    pyautogui.click(Global_Variables.mobile_375)
    time.sleep(0.5)
    pyautogui.moveTo(433,352)
    pyautogui.click()
    for x in range(7):
        time.sleep(0.5)
        pyautogui.hotkey('option','down')
    ## Go to top of page
    time.sleep(0.5)
    pyautogui.hotkey('command', 'up')
    time.sleep(0.5)
    ## Mobile 425
    pyautogui.click(Global_Variables.mobile_425)
    time.sleep(0.5)
    pyautogui.moveTo(433,352)
    pyautogui.click()
    for x in range(7):
        time.sleep(0.5)
        pyautogui.hotkey('option','down')
    ## Go to top of page
    time.sleep(0.5)
    pyautogui.hotkey('command', 'up')
    time.sleep(0.5)
    ## tablet 768
    pyautogui.click(Global_Variables.tablet_768)
    time.sleep(0.5)
    pyautogui.moveTo(433,352)
    pyautogui.click()
    for x in range(6):
        time.sleep(0.5)
        pyautogui.hotkey('option','down')
    ## Go to top of page
    time.sleep(0.5)
    pyautogui.hotkey('command', 'up')
    time.sleep(0.5)
    ## Desktop
    pyautogui.moveTo(Global_Variables.desktop_resolutions)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(433,352)
    pyautogui.click()
    for x in range(4):
        time.sleep(0.5)
        pyautogui.hotkey('option','down')
    ## Go to top of page
    time.sleep(0.5)
    pyautogui.hotkey('command', 'up')
    time.sleep(0.5)
    # 1440
    pyautogui.moveTo(Global_Variables.desktop_resolutions)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(433,352)
    pyautogui.click()
    for x in range(2):
        time.sleep(0.5)
        pyautogui.hotkey('option','down')
    ## Go to top of page
    time.sleep(0.5)
    pyautogui.hotkey('command', 'up')
    time.sleep(0.5)

    ## Passport Renewals 
    browser.get(Global_Variables.url + "/passport-renewal/united-states")
    ## Mobile 320px resolution
    pyautogui.click(Global_Variables.mobile_320)
    pyautogui.hotkey('command','r')
    time.sleep(2)
    ## Scroll down
    pyautogui.moveTo(433,352)
    pyautogui.click()
    pyautogui.hotkey('option','up')
    for x in range(9):
        time.sleep(0.5)
        pyautogui.hotkey('option','down')
    ## Go to top of page
    time.sleep(0.5)
    pyautogui.hotkey('command', 'up')
    time.sleep(0.5)
    ## Mobile 375px
    pyautogui.click(Global_Variables.mobile_375)
    time.sleep(0.5)
    pyautogui.moveTo(433,352)
    pyautogui.click()
    for x in range(9):
        time.sleep(0.5)
        pyautogui.hotkey('option','down')
    ## Go to top of page
    time.sleep(0.5)
    pyautogui.hotkey('command', 'up')
    time.sleep(0.5)
    ## Mobile 425px
    pyautogui.click(Global_Variables.mobile_425)
    time.sleep(0.5)
    pyautogui.moveTo(433,352)
    pyautogui.click()
    for x in range(9):
        time.sleep(0.5)
        pyautogui.hotkey('option','down')
    ## Go to top of page
    time.sleep(0.5)
    pyautogui.hotkey('command', 'up')
    time.sleep(0.5)
    ## Tablet 768px
    pyautogui.click(Global_Variables.tablet_768)
    time.sleep(0.5)
    pyautogui.moveTo(433,352)
    pyautogui.click()
    for x in range(7):
        time.sleep(0.5)
        pyautogui.hotkey('option','down')
    ## Go to top of page
    time.sleep(0.5)
    pyautogui.hotkey('command', 'up')
    time.sleep(0.5)
    ## Desktop 1024px, 1440px, 2560px
    pyautogui.moveTo(Global_Variables.desktop_resolutions)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(433,352)
    pyautogui.click()
    for x in range(7):
        time.sleep(0.5)
        pyautogui.hotkey('option','down')
    ## Go to top of page
    time.sleep(0.5)
    pyautogui.hotkey('command', 'up')
    time.sleep(0.5)
    # 1440
    pyautogui.moveTo(Global_Variables.desktop_resolutions)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(433,352)
    pyautogui.click()
    for x in range(5):
        time.sleep(0.5)
        pyautogui.hotkey('option','down')
    ## Go to top of page
    time.sleep(0.5)
    pyautogui.hotkey('command', 'up')
    time.sleep(0.5)
    # 2560
    pyautogui.moveTo(Global_Variables.desktop_resolutions)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(433,280)
    pyautogui.click()
    for x in range(2):
        time.sleep(0.5)
        pyautogui.hotkey('option','down')
    ## Go to top of page
    time.sleep(0.5)
    pyautogui.hotkey('command', 'up')
    time.sleep(0.5)

    ## About Us
    browser.get(Global_Variables.url + "/about-us")
    ## Mobile 320px resolution
    pyautogui.click(Global_Variables.mobile_320)
    pyautogui.hotkey('command','r')
    time.sleep(2)
    ## Scroll down
    pyautogui.moveTo(433,352)
    pyautogui.click()
    pyautogui.hotkey('option','up')
    for x in range(9):
        time.sleep(0.5)
        pyautogui.hotkey('option','down')
    ## Go to top of page
    time.sleep(0.5)
    pyautogui.hotkey('command', 'up')
    time.sleep(0.5)
    ## Mobile 375px
    pyautogui.click(Global_Variables.mobile_375)
    time.sleep(0.5)
    pyautogui.moveTo(433,352)
    pyautogui.click()
    for x in range(9):
        time.sleep(0.5)
        pyautogui.hotkey('option','down')
    ## Go to top of page
    time.sleep(0.5)
    pyautogui.hotkey('command', 'up')
    time.sleep(0.5)
    ## Mobile 425px
    pyautogui.click(Global_Variables.mobile_425)
    time.sleep(0.5)
    pyautogui.moveTo(433,352)
    pyautogui.click()
    for x in range(9):
        time.sleep(0.5)
        pyautogui.hotkey('option','down')
    ## Go to top of page
    time.sleep(0.5)
    pyautogui.hotkey('command', 'up')
    time.sleep(0.5)
    ## Tablet 768px
    pyautogui.click(Global_Variables.tablet_768)
    time.sleep(0.5)
    pyautogui.moveTo(433,352)
    pyautogui.click()
    for x in range(7):
        time.sleep(0.5)
        pyautogui.hotkey('option','down')
    ## Go to top of page
    time.sleep(0.5)
    pyautogui.hotkey('command', 'up')
    time.sleep(0.5)
    ## Desktop 1024px, 1440px, 2560px
    pyautogui.moveTo(Global_Variables.desktop_resolutions)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(433,352)
    pyautogui.click()
    for x in range(4):
        time.sleep(0.5)
        pyautogui.hotkey('option','down')
    ## Go to top of page
    time.sleep(0.5)
    pyautogui.hotkey('command', 'up')
    time.sleep(0.5)
    # 1440
    pyautogui.moveTo(Global_Variables.desktop_resolutions)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(433,352)
    pyautogui.click()
    for x in range(2):
        time.sleep(0.5)
        pyautogui.hotkey('option','down')
    ## Go to top of page
    time.sleep(0.5)
    pyautogui.hotkey('command', 'up')
    time.sleep(0.5)
    # 2560
    pyautogui.moveTo(Global_Variables.desktop_resolutions)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(433,280)
    pyautogui.click()
    for x in range(2):
        time.sleep(0.5)
        pyautogui.hotkey('option','down')
    ## Go to top of page
    time.sleep(0.5)
    pyautogui.hotkey('command', 'up')
    time.sleep(0.5)

    ## Contact Us
    browser.get(Global_Variables.url + "/contact-us")
    ## Mobile 320px resolution
    pyautogui.click(Global_Variables.mobile_320)
    pyautogui.hotkey('command','r')
    time.sleep(8)
    pyautogui.click(570, 257)
    time.sleep(2)
    ## Scroll down
    pyautogui.moveTo(433,352)
    pyautogui.click()
    pyautogui.hotkey('option','up')
    for x in range(6):
        time.sleep(0.5)
        pyautogui.hotkey('option','down')
    ## Go to top of page
    time.sleep(0.5)
    pyautogui.hotkey('command', 'up')
    time.sleep(0.5)
    ## Mobile 375px
    pyautogui.click(Global_Variables.mobile_375)
    time.sleep(0.5)
    pyautogui.moveTo(433,352)
    pyautogui.click()
    for x in range(6):
        time.sleep(0.5)
        pyautogui.hotkey('option','down')
    ## Go to top of page
    time.sleep(0.5)
    pyautogui.hotkey('command', 'up')
    time.sleep(0.5)
    ## Mobile 425px
    pyautogui.click(Global_Variables.mobile_425)
    time.sleep(0.5)
    pyautogui.moveTo(433,352)
    pyautogui.click()
    for x in range(5):
        time.sleep(0.5)
        pyautogui.hotkey('option','down')
    ## Go to top of page
    time.sleep(0.5)
    pyautogui.hotkey('command', 'up')
    time.sleep(0.5)
    ## Tablet 768px
    pyautogui.click(Global_Variables.tablet_768)
    time.sleep(0.5)
    pyautogui.moveTo(433,352)
    pyautogui.click()
    for x in range(5):
        time.sleep(0.5)
        pyautogui.hotkey('option','down')
    ## Go to top of page
    time.sleep(0.5)
    pyautogui.hotkey('command', 'up')
    time.sleep(0.5)
    ## Desktop 1024px, 1440px, 2560px
    pyautogui.moveTo(Global_Variables.desktop_resolutions)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(433,352)
    pyautogui.click()
    for x in range(3):
        time.sleep(0.5)
        pyautogui.hotkey('option','down')
    ## Go to top of page
    time.sleep(0.5)
    pyautogui.hotkey('command', 'up')
    time.sleep(0.5)
    # 1440
    pyautogui.moveTo(Global_Variables.desktop_resolutions)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(433,352)
    pyautogui.click()
    for x in range(2):
        time.sleep(0.5)
        pyautogui.hotkey('option','down')
    ## Go to top of page
    time.sleep(0.5)
    pyautogui.hotkey('command', 'up')
    time.sleep(0.5)
    # 2560
    pyautogui.moveTo(Global_Variables.desktop_resolutions)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(433,280)
    pyautogui.click()
    for x in range(1):
        time.sleep(0.5)
        pyautogui.hotkey('option','down')
    ## Go to top of page
    time.sleep(0.5)
    pyautogui.hotkey('command', 'up')
    time.sleep(0.5)
    ## Stop recording
    pyautogui.keyDown('option')
    pyautogui.keyDown('s')
    pyautogui.keyUp('option')
    pyautogui.keyUp('s')
    while(True):
       pass
CF_P1()




