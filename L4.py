import requests

response = requests.get("https://bitbay.net/API/Public/BTCUSD/ticker.json")
data = response.json()
buy_bitbay = data['ask']
sell_bitbay = data['bid']
taker_bitbay = 1.03
print('bitbay \nbuy:', buy_bitbay, 'sell:', sell_bitbay)

response = requests.get("https://blockchain.info/ticker")
data = response.json()
buy_blockchain = data['USD']['buy']
sell_blockchain = data['USD']['sell']
taker_blockchain = 1.024
print('\nblockchain \nbuy:', buy_blockchain, 'sell:', sell_blockchain)

response = requests.get("https://cex.io/api/ticker/BTC/USD")
data = response.json()
buy_cex = data['ask']
sell_cex = data['bid']
taker_cex = 1.05
print('\ncex \nbuy:', buy_cex, 'sell:', sell_cex)

response = requests.get("https://www.bitstamp.net/api/ticker/")
data = response.json()
buy_bitstamp = data["high"]
sell_bitstamp = data["low"]
taker_bitstamp = 1.025
print('\nbitstamp \nbuy:', buy_bitstamp, 'sell:', sell_bitstamp, '\n')

taker = [taker_bitbay, taker_blockchain, taker_cex, taker_bitstamp]
name = ['bitbay', 'blockchain', 'cex', 'bitstamp']
buy = [buy_bitbay, buy_blockchain, buy_cex, float(buy_bitstamp)]
sell = [sell_bitbay, sell_blockchain, sell_cex, float(sell_bitstamp)]

count = 0
amount_BTC = 0.1
possible_transactions = []
profits = []
for i in range(len(taker)):
    buy[i] = buy[i] * taker[i] * amount_BTC
    sell[i] = sell[i] * taker[i] * amount_BTC

for i in range(len(buy)):
    for j in range(len(sell)):
        if buy[i] < sell[j] and i != j:
            profit = sell[j] - buy[i]
            print('Na giełdzie', name[i], 'można kupić', amount_BTC, 'BTC po kursie', '%.2f' % buy[i], 'i sprzedać na giełdzie',
                  name[j], 'po kursie', '%.2f' % sell[j], 'zyskując', '%.2f' % profit, 'USD')
            possible_transactions.append([name[i], name[j]])
            profits.append(profit)
            count += 1
if count == 0:
    print('brak możliwości arbitrażu')
else:
    best = profits.index(max(profits))
    print("\nZostała przeprowadzona najlepsza z możliwych tranzakcji: \n"
          "Kupno na girłdzie", possible_transactions[best][0], 'i sprzedaż na giełdzie', possible_transactions[best][1],
          '\nzyskując:', '%.2f' % profits[best], 'USD')





