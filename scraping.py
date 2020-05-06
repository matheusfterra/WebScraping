from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

class WebScraping():
    def __init__(self):
        print("Inicializando Software")
        global driver
        driver = webdriver.Chrome()

    def access_page(self):
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('headless')
        #user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
        #chrome_options.add_argument(f'user-agent={user_agent}')



        PROXY = "161.35.68.165:3128"

        chrome_options.add_argument('--proxy-server=%s' % PROXY)
        driver = webdriver.Chrome(options=chrome_options)
        #chrome = webdriver.Chrome(chrome_options=chrome_options)

        driver.get('http://matheusterra.com/scraping/')
        time.sleep(10)

if __name__=='__main__':
    ws=WebScraping()
    ws.access_page()