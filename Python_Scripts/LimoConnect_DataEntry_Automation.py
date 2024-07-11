#!/usr/bin/env python
# coding: utf-8

# In[3]:

#I think the big flaw in this script is that it would only work in my model computer as its pixel based, but i didnt find consistent HTML tags to base it on. There has to be even better way though

#Packages
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import getpass 
import pandas as pd
import numpy as np
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import xlrd
import pyautogui
from selenium.webdriver.chrome.options import Options


# In[4]:


#Functions
#Clicks at Pixel Coordinate
def clickAB(a, b):
    pyautogui.click(a,b, duration=.10)

#Double click at coordinate    
def doubleClickAB(a, b, c=2):
    for x in range(c):
        pyautogui.click(a,b, duration=.09)

#Current Position 
def current():
    return pyautogui.position()

#Pass a simulated type value 
def keys(a):
    pyautogui.typewrite(str(a))

#Scroll Down set amount 
def scroll(a):
    pyautogui.scroll(a)   
    
#Move Mouse 
def mouseAB(a,b):
    pyautogui.moveTo(a, b)


# In[5]:


#Page Load wait
options = Options()
options.add_argument("--start-maximized")
browser = webdriver.Chrome(options=options)
browser.implicitly_wait(10) # seconds
browser.get("https://nuride.limoconnect247.net/#logout")
myDynamicElement = browser.find_element_by_id("username")


# In[6]:


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
    if(passCheck == 0):
        break   


# In[7]:


#Sizing
WebDriverWait(browser, 60).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="header"]')))
time.sleep(5)
clickAB(1898,53)
time.sleep(2)
doubleClickAB(1767,245)
clickAB(85,54)


# In[8]:


#Explicit wait navigation
WebDriverWait(browser, 60).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="header"]')))
time.sleep(10)
mouseAB(268,134)
time.sleep(1)
clickAB(279,156)


# In[68]:


print("")
input("Enter Dates and Press Enter to continue...")
print("")


# In[66]:


#Filters by company
time.sleep(5)
WebDriverWait(browser, 60).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="btnRefresh"]')))
clickAB(573,205)
time.sleep(2)
clickAB(577,229)
time.sleep(2)
keys("Affiliate")
time.sleep(6)
clickAB(633,208)


# In[6]:


#Code that reads spreadsheet info 
data = pd.read_excel(r'C:\Users\jparedes\Desktop\Carey Report 1020.xlsx', sheet_name='AutoTest')


# In[ ]:


data.head()


# In[1]:


#List of entries
goodEntr = []
noRecErr = []
discErr = [] 


# In[14]:


#Code that reads spreadsheet info 
#data = pd.read_excel(r'C:\Users\Jesus\Desktop\Carey Report 1020.xlsx', sheet_name='AutoTest')
#data.head()


# In[67]:


#Data pricing loop 
time.sleep(8)
for x in range(10):
    #Variables
    searchVar = data.iloc[x,0]
    rateVar = data.iloc[x,2]
    tollsVar = data.iloc[x,3]
    gratVar = data.iloc[x,4]
    surVar = data.iloc[x,5]
    #Enter Value in Search 
    WebDriverWait(browser, 60).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="search"]')))
    browser.find_element_by_xpath('//*[@id="search"]').clear()
    clickAB(523,204)
    keys(searchVar)
    clickAB(614,202)
    mouseAB(848,553)
    #Click first row in search
    WebDriverWait(browser, 60).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="btnRefresh"]')))
    time.sleep(8)
    clickAB(784,250) 
    #Try Except handles there being no records. It looks for an element in form which will fail if not present 
    try:
        #Have to make the scroll sleep in testing in order for it to not zoom in with ctrl 
        WebDriverWait(browser, 25).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="cancelProcessTrip"]')))
        time.sleep(5)
        scroll(-600)
        #First Row, Pass value and save
        doubleClickAB(388,831)
        keys(1)
        doubleClickAB(432,830)
        keys(rateVar)
        clickAB(868,835)
        #Clear Second Row 
        doubleClickAB(388,859)
        keys(1)
        doubleClickAB(429,858)
        keys(0)
        clickAB(868,857)
        #Tolls entry 
        doubleClickAB(390,883)
        keys(1)
        doubleClickAB(432,884)
        keys(tollsVar)
        clickAB(866,885)
        #Gratuity Entry
        doubleClickAB(389,935)
        keys(1)
        doubleClickAB(435,937)
        keys(gratVar)
        clickAB(867,937)
        #Surcharge Entry 
        doubleClickAB(390,961)
        keys(1)
        doubleClickAB(434,962)
        keys(surVar)
        clickAB(867,963)
        #Refresh Total
        clickAB(1797,736)
        #Should be a check here with the total to make sure that the the amounts match up. Else its an error  
        checkBox = browser.find_element_by_xpath('//*[@id="nonfleet"]').is_selected()
        if checkBox == 1:
            clickAB(1808,205)
            time.sleep(6)
        elif checkBox == 0:
            clickAB(1620,205)
            time.sleep(6)
        #Close and List?
        clickAB(1907,207)
        time.sleep(5)
    except:
        erorr1 = searchVar, rateVar, tollsVar, gratVar, surVar
        noRecErr.append(error1)
#Save
#clickAB(1852,207)
#WebDriverWait(browser, 60).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="btnUpdateTrip"]')))
#time.sleep(5)


# In[53]:


#List of Entries based on category of success or failure 
print("No Records")
print()
print(*noRecErr,sep="\n")


# In[ ]:


#I have to find some way to compare totals and once I do that I can see if the entry of correct or not 
#Some way to compare values and if they are not the same then store in a discrepancy list
#doubleClickAB(745,1013)
#pyautogui.hotkey('ctrl', 'c')
#test1 = float(pyperclip.paste())

