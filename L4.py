import requests


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