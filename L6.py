import requests
import pandas as pd


def price(Currency):
    response = requests.get("https://www.bitstamp.net/api/v2/ticker/{}{}/".format(Currency.lower(), 'usd'))
    data = response.json()['bid']
    return float(data)

def price24(Currency):
    response = requests.get("https://www.bitstamp.net/api/v2/transactions/{}{}/".format(Currency.lower(), 'usd'),
                            params={'time': 'day'})
    data = response.json()[-1]['price']

    return float(data)

def main(option):
    data = pd.read_csv('wallet.csv')
    data_currency = []
    for i in range(len(data['Currency'])):
        data_currency.append(data['Currency'][i])

    if option == 1:
        data['Value now'] = round(data['Currency'].apply(price) * data['Volume'], 2)
        data['Value 24h ago'] = round(data['Currency'].apply(price24) * data['Volume'], 2)
        data['Profit'] = data['Value now'] - data['Value 24h ago']
        data['Profit %'] = round((data['Value now'] - data['Value 24h ago']) / data['Value now'] * 100, 2)
        print(data)

    elif option == 2:
        currency = input('Podaj nazwe zasobu: ')
        try:
            price(currency)
            volume = input('Podaj ilość zasobu: ')
            data = data.append({'Currency': currency.upper(), 'Volume': volume}, ignore_index=True)
        except:
            print('Zasób nie istnieje w bazie')



    elif option == 3:
        delete = input('Podaj nazwe zasobu do usunięcia: ')
        if delete in data_currency:
            data.drop(data.loc[data['Currency'] == delete.upper()].index, inplace=True)
        else:
            print('Nie ma takiego zasobu')

    elif option == 4:
        currency = input('Podaj nazwe zasobu: ')
        if currency in data_currency:
            volume = input('Podaj zaktualizowaną ilość zasobu: ')
            data.at[data['Currency'] == currency.upper(), 'Volume'] = volume
        else:
            print('Nie ma takiego zasobu')


    data.to_csv('wallet.csv', index=False)

while True:
    print("Co chcesz zrobić:\n 1. Sprawdź zmiane posiadanych zasobów\n 2. Dodaj zasób\n 3. Usuń zasób\n 4. Zmień ilość zasobu \n 5. Zakończ")
    try:
        option = int(input())
        if option == 5:
            break
        main(option)
    except ValueError:
        print('Podaj liczbę całkowitą z zakresu 1-5')




