#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import getpass 
from bs4 import BeautifulSoup


# In[2]:


#browser = webdriver.Chrome() #replace with .Firefox(), or with the browser of your choice
#url = "https://nuride.limoconnect247.net/fleetconnect/Index.htm#logout"
#browser.get(url) #navigate to the page


# In[3]:


browser = webdriver.Chrome()
browser.implicitly_wait(10) # seconds
browser.get("https://nuride.limoconnect247.net/fleetconnect/Index.htm#logout")
myDynamicElement = browser.find_element_by_id("username")


# In[4]:


while True: 
    username = browser.find_element_by_id("username")
    password = browser.find_element_by_id("password")
    user = getpass.getpass("Username: ")
    passwd = getpass.getpass("Password for " + user + ":")
    browser.find_element_by_id("username").clear()
    browser.find_element_by_id("password").clear()
    username.send_keys(user)
    password.send_keys(passwd)
    submitButton = browser.find_element_by_id("login-button") 
    submitButton.click()
    time.sleep(5)
    try:
        passCheck = browser.find_element_by_class_name("alert").value_of_css_property("display")
    
        if passCheck == 'block' or 'none':
            passCheck = 1
            print()
            print('Wrong Credentials')
    except:
            passCheck = 0
    if(passCheck==0):
        break


# In[ ]:




