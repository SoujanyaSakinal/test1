# #1. Basic Selenium Script (Open Google & Search)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome()
# driver.get("https://www.google.com")

# search = driver.find_element(By.NAME, "q")
# search.send_keys("Selenium Python")
# search.send_keys(Keys.ENTER)

# print("Title:", driver.title)
# driver.quit()

#2. Login Form Automation (Example: Facebook Login Page)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
# driver.get("https://www.facebook.com")

# wait = WebDriverWait(driver, 10)

# email = wait.until(EC.presence_of_element_located((By.ID, "email")))
# password = wait.until(EC.presence_of_element_located((By.ID, "pass")))
# text_area=driver.find_element(By.CLASS_NAME,"_8eso")

# # Double click on email field
# actions = ActionChains(driver)
# actions.double_click(text_area).perform()

# email.send_keys("test@gmail.com")
# password.send_keys("Password123")

# login_btn = driver.find_element(By.NAME, "login")
# login_btn.click()




#3. Checkbox Automation

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/checkboxes")

# cb1 = driver.find_element(By.XPATH, "//input[1]")//*[@id="checkboxes"]/input[1]
# cb2 = driver.find_element(By.XPATH, "//input[2]")//*[@id="checkboxes"]/input[2]

# cb1.click()
# time.sleep(1)
# cb2.click()

# driver.quit()

#4. Dropdown (Select Class)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# import time

# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/dropdown")

# dropdown = Select(driver.find_element(By.ID, "dropdown"))

# dropdown.select_by_visible_text("Option 1")
# time.sleep(1)
# dropdown.select_by_index(2)

# driver.quit()

# 5. Mouse Hover (ActionChains)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# import time

# driver = webdriver.Chrome()
# driver.get("https://imcc.mespune.in/")

# menu = driver.find_element(By.XPATH, "//li[@id='menu-item-4383']")//*[@id="menu-item-4383"]/a/span
# actions = ActionChains(driver)

# actions.move_to_element(menu).perform()
# time.sleep(3)

# driver.quit()

# 8. Drag and Drop

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# import time

# driver = webdriver.Chrome()
# driver.get("https://demoqa.com/droppable")

# source = driver.find_element(By.ID, "draggable")
# target = driver.find_element(By.ID, "droppable")

# actions = ActionChains(driver)
# actions.drag_and_drop(source, target).perform()

# time.sleep(2)
# driver.quit()

#9. Handling Alerts

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# alert1_btn = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
# alert1_btn.click()

# alert = driver.switch_to.alert
# print("Alert 1 text:", alert.text)
# alert.accept()
# time.sleep(1)

# alert2_btn = driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")
# alert2_btn.click()

# alert = driver.switch_to.alert
# print("Alert 2 text:", alert.text)
# alert.dismiss()       # cancel (use alert.accept() for OK)
# time.sleep(1)

# alert3_btn = driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']")
# alert3_btn.click()

# alert = driver.switch_to.alert
# print("Alert 3 text:", alert.text)
# alert.send_keys("Hello from Selenium!")   # type into the prompt
# alert.accept()
# time.sleep(1)
# driver.quit()

# 10. Handling iFrame

# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/iframe")

# driver.switch_to.frame("mce_0_ifr")
# body = driver.find_element(By.TAG_NAME, "p")
# body.clear()
# body.send_keys("Hello from inside iframe!")

# driver.switch_to.default_content()
# driver.quit()

# 11. Multiple Windows Handling

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/windows")

# driver.find_element(By.LINK_TEXT, "Click Here").click()
# time.sleep(2)

# windows = driver.window_handles
# driver.switch_to.window(windows[1])

# print("New window title:", driver.title)
# driver.quit()


# 55.Multi-Select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/select-menu")
driver.maximize_window()

# Locate MULTI-SELECT dropdown
multi_select_element = driver.find_element(By.ID, "cars")
multi_select = Select(multi_select_element)

# Select "Volvo"
multi_select.select_by_visible_text("Volvo")

# Deselect "Volvo"
multi_select.deselect_by_visible_text("Volvo")

# Select by index (Saab = index 1)
multi_select.select_by_index(1)

# Select by value (Audi = 'audi')
multi_select.select_by_value("audi")

# Get all selected options
all_selected_opt_list = multi_select.all_selected_options
for opt in all_selected_opt_list:
    print(opt.text)

# Deselect by index (removes Saab)
multi_select.deselect_by_index(1)

# Deselect by value (removes Audi)
multi_select.deselect_by_value("audi")
# Deselect all
multi_select.deselect_all()

time.sleep(5)
driver.quit()







