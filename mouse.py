import pyautogui
im1 = pyautogui.screenshot(region=(0,0,500,400))
im1.save('my_screenshot2.png')
print('screenshot taken')