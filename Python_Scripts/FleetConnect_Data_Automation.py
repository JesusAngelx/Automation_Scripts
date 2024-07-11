#This was an automation script to automate data entries that I did not want to manually do. 
#I was given thousands of raows and was expected to amnually enter them but iknew there was a better way to do this using an automation script
#After many attempts this is what I came up with



#packages
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import getpass 
import pandas as pd
import xlrd
import numpy as np


# In[2]:


#Page Load wait
browser = webdriver.Chrome()
browser.implicitly_wait(10) # seconds
browser.get("https://nuride.limoconnect247.net/fleetconnect/Index.htm#logout")
myDynamicElement = browser.find_element_by_id("username")


# In[3]:


#Password loop
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
    time.sleep(3)
    try:
        passCheck = browser.find_element_by_class_name("alert").value_of_css_property("display")
    
        if passCheck == 'block' or 'none':
            passCheck = 1
            print()
            print('Wrong Credentials, Enter again')
            print()
            
    except:
            passCheck = 0
    if(passCheck==0):
        break


# In[3]:


#Navigation
time.sleep(8)
browser.find_element_by_xpath('//*[@id="header"]/div[3]/ul/li[2]').click()
browser.find_element_by_xpath('//*[@id="header"]/div[3]/ul/li[2]/ul/li[3]').click()
browser.find_element_by_xpath('//*[@id="header"]/div[3]/ul/li[2]/ul/li[3]/ul/li[1]/a').click()
time.sleep(5)


# In[4]:


#This will depend on where the file is 
data = pd.read_excel(r'C:\Users\Jesus\Desktop\Fleet Connect Data Automation.xlsx', sheet_name='Driver')


# In[5]:


#formatting 
cols = ['Driver (#)', 'Odometer', 'Quantity']
data[cols] = data[cols].applymap(np.int64)

data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%y').dt.strftime('%m/%d/%Y')


# In[6]:


data.head()


# In[8]:


#Counts the rows
countRow = len(data.index)


# In[9]:


#List of lists missing entries
missing = []


# In[14]:


#Data entry loop
#Next make one fail and store it in a var 
browser.find_element_by_xpath('//*[@id="fuellogtab"]/li[2]/span').click()

for x in range(countRow):
    pasteVar = data.iloc[x,0]
    pasteVar1 = data.iloc[x,1]
    pasteVar2 = data.iloc[x,2]
    pasteVar3 = data.iloc[x,3]
    pasteVar4 = data.iloc[x,4]
    pasteVar5 = data.iloc[x,5]
    pasteVar6 = data.iloc[x,6]
    pasteVar7 = data.iloc[x,7]
    pasteVar8 = data.iloc[x,8]
    browser.find_element_by_id('outlogdate_new').send_keys(pasteVar)
    browser.find_element_by_id('outlogtime_new').send_keys(pasteVar1)
    browser.find_elements_by_id('txtVehicle')[1].click()
    browser.find_elements_by_id('txtVehicle')[1].send_keys(pasteVar2)
    time.sleep(.4)
    browser.find_elements_by_id('txtDriver')[1].send_keys(str(pasteVar3))
    time.sleep(.4)
    browser.find_element_by_id('txtOdometer').send_keys(str(pasteVar5))
    browser.find_element_by_id('txtVendor').send_keys(pasteVar6)
    time.sleep(.4)
    browser.find_element_by_id('txtCostUnit').send_keys(str(pasteVar7))
    browser.find_element_by_id('txtQuantity').send_keys(str(pasteVar8))
    #testing variables 
    lisence = browser.find_elements_by_id('txtVehicle')[1].get_attribute('value')
    driver = browser.find_elements_by_id('txtDriver')[1].get_attribute('value')
    #if one feild empty store in var missing append list and close 
    if lisence=='' or driver=='':
        var = pasteVar, pasteVar2, pasteVar4, pasteVar7
        missing.append(var)
        browser.find_element_by_id('close').click()
        browser.find_element_by_xpath('//*[@id="fuellogtab"]/li[2]/span').click()
    else:
        browser.find_element_by_id('btnUpdate').click()
        browser.find_element_by_xpath('//*[@id="fuellogtab"]/li[2]/span').click()

        
        
#Close      
browser.find_element_by_id('close').click()
        
        


# In[11]:


#Finally print the Values not entered 
print('Errors or Not entered:')
print('')
print(*missing, sep = "\n") 


# In[ ]:





