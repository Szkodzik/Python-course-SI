import requests
import time

def profit(money):
    while True:
        response = requests.get("https://bitbay.net/API/Public/BTCUSD/ticker.json")
        data = response.json()
        BTC_min = data['min']
        BTC_max = data['max']
        BTC_vol = data['volume']
        response = requests.get("https://bitbay.net/API/Public/BCCUSD/ticker.json")
        data = response.json()
        BCC_min = data['min']
        BCC_max = data['max']
        BCC_vol = data['volume']
        response = requests.get("https://bitbay.net/API/Public/LTCUSD/ticker.json")
        data = response.json()
        LTC_min = data['min']
        LTC_max = data['max']
        LTC_vol = data['volume']
        response = requests.get("https://bitbay.net/API/Public/ETHUSD/ticker.json")
        data = response.json()
        ETH_min = data['min']
        ETH_max = data['max']
        ETH_vol = data['volume']
        response = requests.get("https://bitbay.net/API/Public/XRPUSD/ticker.json")
        data = response.json()
        XRP_min = data['min']
        XRP_max = data['max']
        XRP_vol = data['volume']

        name = ['BTC', 'BCC', 'LTC', 'ETH', 'XRP']
        data_min = [BTC_min, BCC_min, LTC_min, ETH_min, XRP_min]
        data_max = [BTC_max, BCC_max, LTC_max, ETH_max, XRP_max]
        volume = [BTC_vol, BCC_vol, LTC_vol, ETH_vol, XRP_vol]

        difference = []
        for i in range(len(data_min)):
            difference.append(round(((data_max[i] - data_min[i]) / data_min[i] * 100), 2))

        data = []
        for i in range(len(name)):
            data.append([name[i], data_min[i], data_max[i], volume[i], difference[i]])

        for i in range(len(data) - 1):
            for j in range(len(data) - 1 - i):
                if data[j + 1][4] > data[j][4]:
                    data[j + 1], data[j] = data[j], data[j + 1]

        for i in range(len(data)):
            if data[i][4] >= 0:
                print(data[i][0], '+', data[i][4], '%')
            else:
                print(data[i][0], data[i][4], '%')

        for i in range(len(data)):
            if money > 0 and data[i][3] * data[i][1] <= money:
                price = data[i][3] * data[i][1]
                money = money - price
                print("Kupiłeś", data[i][0], 'za', '%.2f' % price, 'USD\n','Pozostało', money, 'USD')
            elif money == 0:
                print('Brak pieniędzy')

        print('\n', 30 * '-', '\n')
        time.sleep(300)


money = 1000
profit(money)