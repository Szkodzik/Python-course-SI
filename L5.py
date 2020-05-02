import requests

response = requests.get("https://bitbay.net/API/Public/BTCUSD/ticker.json")
data = response.json()
BTC_min = data['min']
BTC_max = data['max']
response = requests.get("https://bitbay.net/API/Public/BCCUSD/ticker.json")
data = response.json()
BCC_min = data['min']
BCC_max = data['max']
response = requests.get("https://bitbay.net/API/Public/LTCUSD/ticker.json")
data = response.json()
LTC_min = data['min']
LTC_max = data['max']
response = requests.get("https://bitbay.net/API/Public/ETHUSD/ticker.json")
data = response.json()
ETH_min = data['min']
ETH_max = data['max']
response = requests.get("https://bitbay.net/API/Public/XRPUSD/ticker.json")
data = response.json()
XRP_min = data['min']
XRP_max = data['max']

name = ['BTC', 'BCC', 'LTC', 'ETH', 'XRP']
data_min = [BTC_min, BCC_min, LTC_min, ETH_min, XRP_min]
data_max = [BTC_max, BCC_max, LTC_max, ETH_max, XRP_max]

print(data_min)
print(data_max)
difference = []
for i in range(len(data_min)):
    difference.append(round(((data_max[i] - data_min[i]) / data_min[i] * 100), 2))

print(difference)

for i in range(len(difference) - 1):
    for j in range(len(difference) - 1 - i):
        if difference[j+1] > difference[j]:
            difference[j+1], difference[j] = difference[j], difference[j+1]
            name[j+1], name[j] = name[j], name[j+1]
print(name)
print(difference)

for i in range(len(name)):
    if difference[i] >= 0:
        print(name[i], '+', difference[i], '%')
    else:
        print(name[i], difference[i], '%')
