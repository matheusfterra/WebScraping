from bs4 import BeautifulSoup as soup
import requests
from proxy_requests import ProxyRequests

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
    print(len(proxies))
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

working_proxies = check_proxies()



