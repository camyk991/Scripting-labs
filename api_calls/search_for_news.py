import requests
import argparse

parser = argparse.ArgumentParser("Wyszukiwarka artykułów. Należy podać temat i nacisnąć enter")
args = parser.parse_args()

print("Podaj temat: ")
subject = input()

url = f'https://newsapi.org/v2/everything?q={subject}&sortBy=publishedAt&apiKey=4eea569493164a78b91ed6188377b655'

data = requests.get(url)

jsonData = data.json()

for article in jsonData['articles']:
    print(f"tytuł: {article['title']}")
    print(f"url: {article['url']}")
    print('\n')
