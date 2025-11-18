#  1. FULL SCRIPT — Open Browser, Maximize, New Tab, Switch, Close

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start Chrome
driver = webdriver.Chrome()

# Maximize Browser Window
driver.maximize_window()

# Open first website
driver.get("https://www.google.com")
print("Opened Google")

time.sleep(2)

# Open new TAB
driver.switch_to.new_window("tab")
driver.get("https://www.facebook.com")
print("Opened Facebook in New Tab")

time.sleep(2)

# SWITCH BACK TO FIRST TAB
all_tabs = driver.window_handles
driver.switch_to.window(all_tabs[0])
print("Switched back to Google Tab")

time.sleep(2)

# CLOSE CURRENT TAB (Google Tab)
driver.close()
print("Closed Google Tab")

# Switch to remaining tab (Facebook)
driver.switch_to.window(all_tabs[1])
print("Now only Facebook tab is open")

# Print total tabs now
print("Total tabs open:", len(driver.window_handles))

time.sleep(2)

# Close the entire browser
driver.quit()
print("Browser closed successfully!")





