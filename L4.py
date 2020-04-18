import requests


response = requests.get("https://bitbay.net/API/Public/BTCUSD/ticker.json")
data = response.json()
buy_bitbay = data['ask']
sell_bitbay = data['bid']
print('bitbay \nbuy:', buy_bitbay, 'sell:', sell_bitbay)

response = requests.get("https://blockchain.info/ticker")
data = response.json()
buy_blockchain = data['USD']['buy']
sell_blockchain = data['USD']['sell']
print('\nblockchain \nbuy:', buy_blockchain, 'sell:', sell_blockchain)

response = requests.get("https://cex.io/api/ticker/BTC/USD")
data = response.json()
buy_cex = data['ask']
sell_cex = data['bid']
print('\ncex \nbuy:', buy_cex, 'sell:', sell_cex)

response = requests.get("https://www.bitstamp.net/api/ticker/")
data = response.json()
buy_bitstamp = data["high"]
sell_bitstamp = data["low"]
print('\nbitstamp \nbuy:', buy_bitstamp, 'sell:', sell_bitstamp)


name = ['bitbay', 'blockchain', 'cex', 'bitstamp']
buy = [buy_bitbay, buy_blockchain, float(buy_cex), float(buy_bitstamp)]
sell = [sell_bitbay, sell_blockchain, sell_cex, float(sell_bitstamp)]
print(buy)
print(sell)
count = 0
for i in range(len(buy)):
    for j in range(len(sell)):
        if buy[i] < sell[j] and i != j:
            print('na giełdzie ',name[i],'można kupić 1 BTC po kursie', buy[i], 'i sprzedać na giełdzie ', name[j], 'po kursie ',sell[j], 'zyskując ',sell[j] - buy[i])
            count += 1
if count == 0:
    print('brak możliwości arbitrażu')

