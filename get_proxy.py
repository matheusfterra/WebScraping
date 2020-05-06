from bs4 import BeautifulSoup as soup
import requests
import time
from random import randint

def get_proxies():
    proxy_web_site = 'https://free-proxy-list.net/'
    response = requests.get(proxy_web_site)
    page_html = response.text
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.find_all("div", {"class": "table-responsive"})[0]
    ip_index = [8 * k for k in range(80)]
    proxies = set()

    for i in ip_index:
        ip = containers.find_all("td")[i].text
        port = containers.find_all("td")[i + 1].text
        https = containers.find_all("td")[i + 6].text
        # print("\nip address : {}".format(ip))
        # print("port : {}".format(port))
        # print("https : {}".format(https))

        if https == 'yes':
            proxy = ip + ':' + port
            proxies.add(proxy)

    return proxies

def check_proxies():
    working_proxies = set()
    proxies = get_proxies()
    test_url = 'https://httpbin.org/ip'

    for i in proxies:
        print("\nTrying to connect with proxy: {}".format(i))
        try:
            response = requests.get(test_url, proxies={'https':'https://{}'.format(i),'http':'http://{}'.format(i)}, timeout=6)

            print(response.json())
            print("This proxy is added to the list. Have a lovely day!")
            working_proxies.add(i)

        except:
            print("Skipping. Connnection error")

    return working_proxies


def scrape_website(url):
    global working_proxies
    print("Início de acesso ao site!")
    for prox in list(working_proxies):

        try:
            html_code = requests.get(url, proxies={"http": "http://{}".format(prox), "https": "https://{}".format(prox)}).text
            page_soup = soup(html_code, "html.parser")
            print(page_soup)

            ''' add a module here to target specific data points from the website
          and record it '''

            time.sleep(randint(3, 6))

        except:

            working_proxies.remove(prox)
            print("{} proxy removed from the list".format(prox))

            # update proxy list if you run out of proxies
            if len(working_proxies) < 3:
                working_proxies = check_proxies()



url = 'https://intoli.com/blog/making-chrome-headless-undetectable/chrome-headless-test.html'
working_proxies = check_proxies()
while(1):
    scrape_website(url)