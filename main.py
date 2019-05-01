import pyautogui as pag

def ImNotARobot():
    #pag.screenshot('Images/sight.png')
    location = pag.locateCenterOnScreen('Images/vivaldi.png')
    pag.moveTo(location.x, location.y, duration=0.5)
    pag.click(button='left', duration=0.1)
    #pag.screenshot('Images/sight.png')
    location = pag.locateCenterOnScreen('Images/imNotARobot.png')
    pag.moveTo(location.x, location.y, duration=0.5)
    pag.click(button='left', duration=0.1)

ImNotARobot()