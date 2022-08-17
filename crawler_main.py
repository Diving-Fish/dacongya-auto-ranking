from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import time
from datetime import datetime
import json
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
client = webdriver.Chrome(options=chrome_options)
client.set_window_size(1920, 1080)

def init_main(username, passwd):
    client.get("https://www.maj-soul.net/dhs/#/login")
    client.find_element(By.ID, "username").send_keys(username)
    client.find_element(By.ID, "password").send_keys(passwd)
    sleep(0.2)
    client.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div[4]/div[2]').click()
    sleep(2)
    client.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/main/div[2]/ul/li/div/div[5]').click()

def refresh():
    client.find_element(By.XPATH, '//*[@id="root"]/div/header/div/div[1]/a/button').click()
    sleep(0.5)
    client.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/main/div[2]/ul/li/div/div[5]').click()
    sleep(0.5)
    client.find_element(By.XPATH, '//*[@id="root"]/div/header/div/div[3]/div/div/div/div/button[5]/span[1]/span').click()
    
    timeout = 0
    while True:
        try:
            table = client.find_element(By.TAG_NAME, 'tbody')
            break
        except Exception:
            timeout += 1
            sleep(0.5)
            if timeout > 60:
                return ""
            pass
    client.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/main/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div/div').click()
    sleep(0.2)
    client.find_element(By.XPATH, '//*[@id="menu-"]/div[2]/ul/li[3]').click()
    sleep(0.2)
    lines = table.text
    txt2 = ""
    with open("ranking_data.txt", 'r', encoding='utf-8') as f:
        txt = f.read()
    for line in lines.split('\n'):
        arr = line.split(' ')
        if len(arr) == 10:
            flag = True
            for line2 in txt.split('\n'):
                if line.strip() == line2.strip():
                    flag = False
                    break
            if flag:
                txt2 += line + '\n'
    if txt2 != "":
        print((datetime.now().strftime("%H:%M:%S") + " Update: \n" + txt2).strip())
    txt = txt2 + txt
    with open("ranking_data.txt", 'w', encoding='utf-8') as f:
        f.write(txt)

    return txt
    

init_main("username_here", "password_here")
count = 0
while True:
    try:
        if count > 100:
            print("Restart to free memory")
            break
        count += 1
        refresh()
        sleep(20)
    except Exception as e:
        print(e)
        break
client.close()
client.quit()
    
