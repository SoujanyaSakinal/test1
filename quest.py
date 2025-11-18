# from selenium import webdriver
# import time
# options= webdriver.ChromeOptions()
# driver=webdriver.Chrome(options=options)
# driver.get("https://www.google.com")
# driver.maximize_window()
# print(driver.title)
# time.sleep(10)
# driver.close()

# # XPATH 
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# options= webdriver.ChromeOptions()
# driver=webdriver.Chrome(options=options)
# driver.get("https://www.wikipedia.org")
# driver.maximize_window()
# print(driver.title)
# btn1=driver.find_element(By.XPATH,"//button[@id='js-lang-list-button']")
# btn1.click()
# if not btn1.is_selected():
#     btn1.click()
# print("Button selected",btn1.is_selected())
# time.sleep(10)
# driver.close()

# # Checkbox Xpath
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# options= webdriver.ChromeOptions()
# driver=webdriver.Chrome(options=options)
# driver.get("https://the-internet.herokuapp.com/checkboxes")
# driver.maximize_window()
# print(driver.title)
# btn1=driver.find_element(By.XPATH,"//form[@id='checkboxes']/input[1]")
# btn2=driver.find_element(By.XPATH,"//form[@id='checkboxes']/input[2]")

# btn1.click()
# if not btn1.is_selected():
#     btn1.click()
# print("Button selected",btn1.is_selected())

# btn2.click()
# if not btn2.is_selected():
#     btn2.click()
# print("Button selected",btn2.is_selected())
# time.sleep(5)
# driver.close()

#Go to direct about page
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# import time
# options= webdriver.ChromeOptions()
# driver=webdriver.Chrome(options=options)
# driver.get("https://imcc.mespune.in/")
# driver.maximize_window()
# print(driver.title)
# program_menu=driver.find_element(By.XPATH,"//li[@id='menu-item-1193']//a[@class='menu-link'][normalize-space()='About Us']")
# actions=ActionChains(driver)
# actions.move_to_element(program_menu).perform()
# time.sleep(5)
# driver.close()

# # Different Tabs and Different Windows 
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# options= webdriver.ChromeOptions()
# driver=webdriver.Chrome(options=options)
# driver.get("https://www.google.com")

# driver.switch_to.new_window("window")
# driver.get("https://www.facebook.com")

# driver.switch_to.new_window("tab")
# driver.get("https://www.youtube.com")

# driver.maximize_window()
# print(driver.title)

# time.sleep(10)
# driver.close()


# #Search imcc automatically in search
# from selenium import webdriver
# from selenium.webdriver.common.by import By 
# from selenium.webdriver.common.keys import Keys
# import time
# driver = webdriver.Chrome() 
# driver.get("https://www.google.com/")
# search_txtbox = driver.find_element(By.XPATH,"//textarea[@name='q']")
# search_txtbox.send_keys('imcc')
# search_txtbox.send_keys(Keys.ENTER)
# # imcc_dropdown = driver.find_elements(By.XPATH, "//span[contains(normalize-space(), 'imcc')]")
# time.sleep(5)
# driver.close()

#Drag and Drop or move the image.logo
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.set_page_load_timeout(20)
driver.maximize_window()
driver.get("https://imcc.mespune.in/")
wait = WebDriverWait(driver, 15)
actions = ActionChains(driver)
header = wait.until(EC.presence_of_element_located((By.XPATH, "//h2[contains(normalize-space(.),'Prominent Recruiters')]")) )

logos = wait.until(
EC.presence_of_all_elements_located((By.XPATH,"//h2[contains(normalize-space(.), 'Prominent Recruiters')]/following::img")) )
print("Total logos found:", len(logos))
if len(logos) >= 3:
    third_logo = wait.until(EC.visibility_of(logos[2])) # index 2 => 3rd logo
    time.sleep(2)
    actions.click_and_hold(third_logo).move_by_offset(-100, 0).release().perform()
    #actions.drag_and_drop_by_offset(third_logo, -100, 0).perform()
    print("Dragged 3rd logo 100px to the left.")
    time.sleep(2)
else:
    print("Less than 3 logos found")
driver.quit()
