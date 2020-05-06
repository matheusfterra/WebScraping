from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import get_proxy
import requests

class WebScraping():
    def __init__(self):
        print("Inicializando Software")
        proxys= get_proxy.check_proxies()
        while len(proxys)==0:
            print("Proxy não encontrado....Reiniciando busca!")
            proxys = get_proxy.check_proxies()
        self.access_page(proxys)

    def access_page(self, working_proxies):
        url = 'https://httpbin.org/ip'
        #url = 'https://matheusterra.com/scraping/'
        print("Início de acesso ao site!")
        for prox in list(working_proxies):
            print("Proxy atual:",prox)
            try:
                page_test= requests.get(url, proxies={"http": "http://{}".format(prox), "https": "https://{}".format(prox)})

                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument('--proxy-server=%s' % prox)
                driver = webdriver.Chrome(options=chrome_options)
                driver.get(url)
                time.sleep(10)
                driver.close()
            except:
                working_proxies.remove(prox)
                print("{} proxy removed from the list. Working_proxies: {}".format(prox,len(working_proxies)))

                # update proxy list if you run out of proxies
                if len(working_proxies) < 3:
                    working_proxies = get_proxy.check_proxies()
                    while len(working_proxies) == 0:
                        print("Proxy não encontrado....Reiniciando busca!")
                        working_proxies = get_proxy.check_proxies()

if __name__=='__main__':
    ws=WebScraping()
    #ws.access_page()