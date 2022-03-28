

from matplotlib import pyplot as plt
import urllib.request
import json
from time import sleep
# from p_tqdm import p_map

btc_prices = []


for i in range(5):  
    url="https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC&tsyms=EUR&e=CCCAGG"
    with urllib.request.urlopen(url) as response:
        html = response.read()
    data = json.loads(html)
    btc_prices.append(data['BTC']['EUR'])
    sleep(2)

fig = plt.figure(figsize=(10, 7))
plt.bar(list(range(1,6)), btc_prices)
plt.show()  