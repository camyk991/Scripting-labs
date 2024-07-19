import requests

def get_currency_data(currency_code):
    URL = f"http://api.nbp.pl/api/exchangerates/rates/A/{currency_code}/last/5/"
    response = requests.get(URL)
    data = response.json()
    dates = []
    currencies = []

    for line in data['rates']:
        dates.append(line['effectiveDate'])
        currencies.append(line['mid'])

    return dates, currencies

def calculate_differences(values):
    differences = [values[i] - values[i-1] for i in range(1, len(values))]
    return differences

def main():
    currency_code = input("Podaj kod waluty (np. USD, EUR): ").upper()

    dates, values = get_currency_data(currency_code)

    print(f"Kursy waluty {currency_code} z ostatnich 5 dni:")
    for date, value in zip(dates, values):
        print(f"{date}: {value}")

    differences = calculate_differences(values)
    print("\nRóżnice między kolejnymi dniami:")
    for date, difference in zip(dates[1:], differences):
        print(f"{date}: {difference}")

if __name__ == "__main__":
    main()