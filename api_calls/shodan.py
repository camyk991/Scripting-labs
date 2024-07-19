import shodan
import argparse

parser = argparse.ArgumentParser("Program do sprawdzania otwartych portów za pomocą Shodan API")
parser.parse_args()

def shodan_ip_info(api_key, ip_address):
    # Inicjalizacja klienta Shodan
    api = shodan.Shodan(api_key)

    # Pobranie informacji na temat adresu IP
    host = api.host(ip_address)


    print(f"Organizacja: {host['org']}")
    print(f"Pochodzenie: {host['country_name']}")
    print(f"Miasto: {host['city']}")

    print("Otwarte porty:")
    for port in host['ports']:
        print(f" - {port}")




api_key = 'jtmzwhxHT1CRUm5vQcmNTbQr8keMDOyS'
ip_address = input("Podaj adres IP: ")

shodan_ip_info(api_key, ip_address)


