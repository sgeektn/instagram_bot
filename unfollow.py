#!/bin/python3

import instaloader
from selenium import webdriver
import time



def login_instagram(driver,username,password):
    
    driver.get("https://www.instagram.com/accounts/login/")

    try:
        driver.find_element_by_xpath("/html/body/div[4]/div/div/button[1]").click()
    except:
        pass

    time.sleep(3)

    username_field = driver.find_element_by_name("username")
    username_field.send_keys(username)
    password_field = driver.find_element_by_name("password")
    password_field.send_keys(password)
    password_field.submit()

    time.sleep(4)
    


def unfollow_instagram_account(driver,account):
    driver.get("https://www.instagram.com/"+account+"/")
    time.sleep(2)
    driver.find_element_by_xpath("//*[contains(@aria-label, 'Abonné(e)')]").click()
    driver.find_element_by_xpath("//*[text() = 'Se désabonner']").click()
    time.sleep(2)


options = webdriver.ChromeOptions()
options.add_argument("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox/94.0")
driver = webdriver.Chrome(chrome_options=options)

#driver = webdriver.Chrome()

print(login_instagram(driver,'sami_fakhfakh','zatla123birra'))

users = []
# read and delete first 30 lines from result.txt
accounts = open("unfollow.txt", "r")
with open('unfollow.txt', 'r') as f:
    lines = f.readlines()
    users = lines[:100]
    lines = lines[100:]
    with open('unfollow.txt', 'w') as f:
        f.writelines(lines)

i = 0
for user in users:
    print("Unfollowing user: "+str(i))
    i+=1
    try:
        unfollow_instagram_account(driver,user)
    except:
        # write to unfollow_exception.txt
        with open('unfollow_exception.txt', 'a') as f:
            f.write(user)

    
        
   