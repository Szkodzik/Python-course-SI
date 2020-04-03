import requests




response = requests.get("https://bitbay.net/API/Public/BTCPLN/ticker.json")
data = response.json()
best_bid=data['bid']
best_ask=data['ask']
print('bid:',best_bid,'ask:',best_ask)

response = requests.get("https://blockchain.info/ticker")
data = response.json()
best_bid_new=data['PLN']['buy']
best_ask_new=data['PLN']['sell']
print('bid:',best_bid_new,'ask:',best_ask_new)

x = 'bitbay'
y = 'blockchain'


print('Obecnie na',y if best_bid > best_bid_new else x,'jest lepiej kupić, a na',x if best_ask > best_ask_new else y,'lepiej sprzedać')

