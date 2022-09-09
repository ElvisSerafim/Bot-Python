from itertools import count
from random import randint
from threading import Thread
from fake_useragent import UserAgent
import threading
from multiprocessing import Pool
import pyautogui
import requests
import base64
import undetected_chromedriver.v2 as uc
import time
from seleniumwire.undetected_chromedriver.v2 import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


toEncode = "london1.thesocialproxy.com:10000@8gxdbuerslyki2t7:na65c1m3vwrupqob"
message_bytes = toEncode.encode()
base64_bytes = base64.b64encode(message_bytes)
countProxy = 0

url = "https://thesocialproxy.com/wp-json/lmfwc/v2/licenses/customer/user-licenses/?consumer_key=ck_2ba76769a4bb1e6259f6b634e54820b965abfb00&consumer_secret=cs_75fadf1fd77bab27e4bb90ed5ef1670a0cc66bd8"
url2 = "https://thesocialproxy.com/wp-json/lmfwc/v2/licenses/rotate-proxy/bG9uZG9uMS50aGVzb2NpYWxwcm94eS5jb206MTAwMDBAOGd4ZGJ1ZXJzbHlraTJ0NzpuYTY1YzFtM3Z3cnVwcW9i/?consumer_key=ck_930d4ca351aac8fe499b96f39224accae1008b06&consumer_secret=cs_1eac3701d7f16f8908392120af0a11d645aafba8"
url3 = "https://thesocialproxy.com/wp-json/lmfwc/v2/licenses/proxy-logs/bG9uZG9uMS50aGVzb2NpYWxwcm94eS5jb206MTAwMDBAOGd4ZGJ1ZXJzbHlraTJ0NzpuYTY1YzFtM3Z3cnVwcW9i/?consumer_key=ck_930d4ca351aac8fe499b96f39224accae1008b06&consumer_secret=cs_1eac3701d7f16f8908392120af0a11d645aafba8"


payload={}
headers = {
  'Content-Type': 'application/json'
}


def enter_proxy_auth(proxy_username, proxy_password):
    time.sleep(1)
    pyautogui.typewrite(proxy_username)
    pyautogui.press('tab')
    pyautogui.typewrite(proxy_password)
    pyautogui.press('enter')


def open_a_page(driver, url):
    driver.get(url)
    driver.maximize_window()



def create_driver(lines):
    global countProxy
    if(countProxy == 10):
        countProxy = 0
    options = uc.ChromeOptions()
    ua = UserAgent()
    userAgent = ua.chrome
    PROXY = lines[countProxy]
    print(f"Proxy sendo utilizado: {PROXY}")
    options = {
    'proxy': {
        'http': f'http://{PROXY}',
        'https': f'http://{PROXY}',
        'no_proxy': 'localhost,127.0.0.1'
        }
    }
    #string para https da proxyrack: f'http://{proxyAuth}:6f12ac-f98244-071260-b189ac-f6a7ac@{PROXY}'
    # options.add_argument(f'user-agent={userAgent}')
    # print(userAgent)
    # chrome = uc.Chrome(options=options)
    # chrome.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": userAgent})
    chrome = Chrome(seleniumwire_options=options)
    # print(dir(chrome))
    countProxy = countProxy + 1
    return chrome

def agora_vai(driver):
    proxy_username = "8gxdbuerslyki2t7"
    proxy_password = "na65c1m3vwrupqob"
    open_a_page(driver, "https://bit.ly/3uU05LI")
    time.sleep(30)

    if(driver.current_url == "https://wisdomcoin.net/"):
        print("na funcao")
        time.sleep(30)
        try: 
            driver.find_element(By.CLASS_NAME, "random-post").click()
            time.sleep(20)
            element_present = EC.presence_of_element_located((By.CLASS_NAME, 'random-post'))
            WebDriverWait(driver, 30).until(element_present)
            driver.find_element(By.CLASS_NAME, "random-post").click()
            time.sleep(20)
            for i in range(20): # adjust integer value for need
                driver.execute_script("window.scrollBy(0, 250)")
                time.sleep(3)
            time.sleep(35)
        except:
            print("Erro ao encontrar random post")

    driver.close()




if __name__ == '__main__':
    hostname = "HOST_NAME"
    port = "PORT"
    number_of_threads = 6
    threads = []
    drivers = []
    #proxies = { 'https' : 'https://mateusll-country-us:6f12ac-f98244-071260-b189ac-f6a7ac@private.residential.proxyrack.net:10000' }
    #testan = requests.get('https://ipinfo.io', proxies=proxies)
    #print(testan.text)
    with open("proxies.txt", "r") as tf:
        lines = tf.readlines()
    
    
    #for line in lines:
        #print(line)

    while True:
        for _ in range(number_of_threads):
            dr = create_driver(lines)
            drivers.append(dr)
  
        for i in range(number_of_threads):
            print(drivers[i])
            testing = drivers[i]
            t = threading.Thread(target=agora_vai, args=(drivers[i], ))
            threads.append(t)

        for thr in threads:
            thr.start()

        for t in threads:
            t.join()
        
        drivers.clear()
        threads.clear()
