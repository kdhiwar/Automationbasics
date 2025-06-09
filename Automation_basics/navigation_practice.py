from time import sleep
import selenium
from selenium import webdriver
print(selenium.__version__)   # this will tell your selenium version
driver = webdriver.Chrome() #instantiate webdriver
driver.maximize_window()    #maximize the browser window
driver.get("http://www.google.com") # opening the Url
sleep(3)                            # make driver wait to load page
driver.get("http://www.youtube.com")
sleep(3)
driver.back() # navigate back
sleep(3)
driver.forward() # navigate forward
sleep(3)
driver.minimize_window() #minimize the browser window
sleep(3)
driver.refresh()     #refresh page
sleep(2)
driver.quit()        #close driver




