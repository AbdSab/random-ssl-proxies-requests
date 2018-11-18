import requests
from bs4 import BeautifulSoup
import random

class Proxy:
    ip = []
    def __init__(self):
        res = requests.get("https://www.sslproxies.org/")
        content = BeautifulSoup(res.content, "html.parser")
        table = content.find("table", {"id":"proxylisttable"})
        tr = table.find_all("tr")[1:][:-1]
        for t in tr:
            _ip = t.find_all("td")[0].text
            _port = t.find_all("td")[1].text
            self.ip.append({_ip:_port})
    def getProxy(self):
        return random.choice(self.ip)
    

x = Proxy()
print x.getProxy()