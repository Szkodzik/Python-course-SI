import requests
import json
import matplotlib.pyplot as plt
import random
from copy import *

request = requests.get('https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=USD&apikey=DQHTDT7WB9NVTARN')
request = request.json()
data = json.dumps(request, sort_keys=(True), indent=4)
data = json.loads(data)
data = data['Time Series (Digital Currency Daily)']

list_data = list(data.keys())
list_price = []

for i in range(len(list_data)):
    list_price.append(float(data[list_data[i]]['4a. close (USD)']))

print("Podaj od której daty program ma przewidzieć kolejne 30 dni kursu BTC-USD")
year = int(input('podaj rok: '))
month = int(input('podaj miesiąc: '))
year = str(year)

if month < 10:
    month = '0' + str(month)
else:
    month = str(month)

dzien = '01'
start = year + '-' + month + '-01'

data = []
price = []
for i in range(len(list_data)):
    if start == list_data[i]:
        data.append(list_data[i:i+30])
        price.append(list_price[i:i+30])
data = data[0]
price = price[0]

def predict(data, price, list_data, list_price):
    pred = []
    for i in range(len(list_data)):
        if list_data[i] == data[0]:
            before = list_price[i-1]

    for i in range(len(price) - 1):
        if i == 0:
            roznica = price[i] - before
            roznica = roznica * random.random() * 2
            rand = random.random()
            if rand > 0.25:
                pred.append(price[-1] + roznica)
            else:
                pred.append(price[-1] - roznica)
        else:
            roznica = price[i+1] - price[i]
            roznica = roznica * random.random() * 2
            rand = random.random()
            if rand > 0.25:
                pred.append(pred[i - 1] + roznica)
            else:
                pred.append(pred[i - 1] - roznica)
    roznica = pred[0] - price[-1]
    roznica = roznica * random.random() * 2
    rand = random.random()
    if rand > 0.25:
        pred.append(pred[-1] + roznica)
    else:
        pred.append(pred[-1] - roznica)

    return pred

def predict_100(data, price, list_data, list_price):
    list_pred = []
    pred = []
    for i in range(100):
        list_pred.append(predict(data, price, list_data, list_price))

    for i in range(len(list_pred[0])):
        help = []
        for j in range(len(list_pred)):
            help.append(list_pred[j][i])
        pred.append(sum(help) / len(list_pred))
    return pred

pred = predict(data, price, list_data, list_price)
pred2 = predict_100(data, price, list_data, list_price)
price2 = copy(price)
for i in range(len(pred)):
    price.append(pred[i])
    price2.append(pred2[i])

days = []
for i in range(60):
    days.append(-30+i)

plt.figure()
plt.plot(days, price)
plt.title('Wykres z 1 symulacją')
plt.figure()
plt.plot(days, price2)
plt.title('Wykres z 100 symulacjami')
plt.show()


