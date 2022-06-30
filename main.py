from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import keyboard
from selenium.webdriver.common.by import By

chrome_driver_path = 'chromedriver.exe'     # change this to the path of chromedriver in your system

browser = webdriver.Chrome(chrome_driver_path)      

browser.get('https://www.google.co.in')

searchbox = browser.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')

google_search_text = 'cats'     #change this to the word/words that you want to search for

searchbox.send_keys(google_search_text)
searchbox.send_keys(Keys.ENTER)

google_images = browser.find_element(by=By.XPATH, value='//*[@id="hdtb-msb"]/div[1]/div/div[2]/a') 

google_images.click()

first_height = browser.execute_script('return document.body.scrollHeight')

# this loop is to scroll down all the way to the bottom of the images so that all the pictures are loaded on to the page beforehand and there is no error when taking a screenshot of the image
while True:

    try:
        more = browser.find_element(by=By.XPATH, value='//*[@id="islmp"]/div/div/div/div[1]/div[2]/div[2]/input')
        more.click() 

    except:
        pass


    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    time.sleep(2)

    new_height = browser.execute_script('return document.body.scrollHeight')

    
    if (new_height==first_height):
        break

    
    first_height=new_height


cnt=0
i=1

# this loop is to go through all the pictures available for that particular google search and either use or discard them as the user wishes
while True:

    xp = '//*[@id="islrg"]/div[1]/div[' + str(i) + ']/a[1]/div[1]/img'

    try:
        pic = browser.find_element(by=By.XPATH, value=xp)
        time.sleep(1)
        pic.click()

        if (keyboard.read_key()=='y'):

            cnt = cnt + 1
            side_frame = browser.find_element(by=By.XPATH, value='//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img')
            path_for_images = 'C:/Users/Rushendra Sidibomma/Documents/Using google as dataset/images/cat'   # change this to the path of the folder where you want to save the pictures
            FORMAT = '.png'
    
            side_frame.screenshot(path_for_images + str(cnt) + FORMAT)

        if (keyboard.read_key()=='q'):
            break
            
        i = i+1
        

    except:
        break


#################################################################

