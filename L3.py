import requests


response = requests.get("https://bitbay.net/API/Public/BTCPLN/orderbook.json")
data = response.json()
bid = data['bids']
ask = data['asks']
oferty_kupna = []
oferty_sprzedazy = []
for i in range(5):
    oferty_kupna.append(bid[i][0])
    oferty_sprzedazy.append(ask[i][0])

print('5 pierwszych ofert kupna: ', oferty_kupna, '\n5 pierwszych ofert sprzedaży: ', oferty_sprzedazy)
print('-'*30)
response = requests.get("https://bitbay.net/API/Public/BTCPLN/ticker.json")
data = response.json()
bid_bitbay = data['bid']
ask_bitbay = data['ask']
print('bitbay \nbid:', bid_bitbay, 'ask:', ask_bitbay)

response = requests.get("https://blockchain.info/ticker")
data = response.json()
bid_blockchain = data['PLN']['buy']
ask_blockchain = data['PLN']['sell']
print('\nblockchain \nbid:', bid_blockchain, 'ask:', ask_blockchain)

print('\nObecnie na', 'blockchain' if bid_bitbay > bid_blockchain else 'bitbay', 'jest lepiej kupić, a na', 'bitbay' if ask_bitbay > ask_blockchain else 'blockchain', 'lepiej sprzedać')

