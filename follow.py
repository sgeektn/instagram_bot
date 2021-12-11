#!/bin/python3

import instaloader
from requests.api import options
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
    


def follow_instagram_account(driver,account):
    driver.get("https://www.instagram.com/"+account+"/")
    time.sleep(2)
    driver.find_element_by_xpath("//*[text() = 'S’abonner']").click()
    time.sleep(2)

options = webdriver.ChromeOptions()
options.add_argument("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox/94.0")
driver = webdriver.Chrome(chrome_options=options)

print(login_instagram(driver,'sami_fakhfakh','zatla123birra'))

users = []
# read and delete first 30 lines from result.txt
accounts = open("result.txt", "r")
with open('result.txt', 'r') as f:
    lines = f.readlines()
    users = lines[:30]
    lines = lines[30:]
    with open('result.txt', 'w') as f:
        f.writelines(lines)

i=0
for user in users:
    print("following user: "+str(i))
    i+=1
    try:
        follow_instagram_account(driver,user)
        with open('unfollow.txt', 'a') as f:
            f.write(user)
    except:
        print("error flollowing user")
        with open('follow_exception.txt', 'a') as f:
            f.write(user)


    # write user to unfollow.txt
    
