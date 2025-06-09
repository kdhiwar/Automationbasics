


from time import sleep
import selenium
from scipy.constants import value
from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Edge()
driver.maximize_window()
driver.get("https://saucedemo.com/")
sleep(2)

#by id_________________________________________________________________________
#username=driver.find_element(By.ID,"user-name")

#absolute xpath
#username=driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input')

#relative xpath
#username=driver.find_element(By.XPATH,'//input[@placeholder="Username"] ')

#using contains when long value
#username=driver.find_element(By.XPATH,'//input[contains(@id,"user-name")] ')

#relative xpath using and -both attribute are mandatory
#username=driver.find_element(By.XPATH,'//input[@placeholder="Username" and @type="text"] ')

#relative xpath using or  -any 1 attribute
#username=driver.find_element(By.XPATH,'//input[@placeholder="Username" or @type="text"] ')

#relative xpath using index
#username=driver.find_element(By.XPATH,'(//input[@class="input_error form_input"] )[1] ')


#By CSS selectors by tag name selects 1st occurance
#username=driver.find_element(By.CSS_SELECTOR,"input")
#By CSS selectors by id
#username=driver.find_element(By.CSS_SELECTOR,'#user-name')
#By CSS selectors by attribute
#username=driver.find_element(By.CSS_SELECTOR,'input[type="text"]')
#By CSS selectors by parent > child
#username=driver.find_element(By.CSS_SELECTOR,'div>input[id="user-name"]')
#By CSS selectors by descendant
username=driver.find_element(By.CSS_SELECTOR,'form input[id="user-name"]')

username.send_keys("error_user")
#------------------------------------------------------------------------------------------------
#byname
password=driver.find_element(By.NAME,"password")

password.send_keys("secret_sauce")
#--------------------------------------------------------------------------------------------------
#by classname
#submit=driver.find_element(By.CLASS_NAME,"submit-button")

#CSS by class name
#submit=driver.find_element(By.CSS_SELECTOR,".btn_action")
#CSS by combination tag name+ class name
submit=driver.find_element(By.CSS_SELECTOR,"input.btn_action")
submit.click()
sleep(3)
#---------------------------------------------------------------------------------------------------
#open product by linktext
#product_select= driver.find_element(By.LINK_TEXT, "Sauce Labs Backpack")

#open product by partial linktext
#product_select= driver.find_element(By.PARTIAL_LINK_TEXT, "Backpack")

#open product by text method inside xpath
product_select= driver.find_element(By.XPATH, '//div[text()= "Sauce Labs Backpack"]')
product_select.click()
sleep(3)
driver.quit()

