import requests
import json
import matplotlib.pyplot as plt
import random

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

if month != 12:
    next_month = month + 1
else:
    next_month = 1

year = str(year)

if month < 10:
    month = '0' + str(month)
else:
    month = str(month)

if next_month < 10:
    next_month = '0' + str(next_month)
else:
    next_month = str(next_month)

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

#pred = predict(data, price, list_data, list_price)
pred = predict_100(data, price, list_data, list_price)
for i in range(len(pred)):
    price.append(pred[i])
print(price)
print(len(price))
d = []

for i in range(60):

    d.append(-30+i)

plt.figure()
plt.plot(d,price)
plt.title('Wykres')
plt.show()


#przedstawić wykresy
