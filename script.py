import requests
from bs4 import BeautifulSoup
import re

url = input("paste the url that you want to extract things from...")

headers = {
    'User-Agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,'
        ' like Gecko) Chrome/120.0.0.0 Safari/537.36'
    )
}


html_url = requests.get(url, headers=headers)
response = html_url.text
soup = BeautifulSoup(response,'lxml')

for script in soup(["script", "style", "noscript"]):
  script.decompose()


def finding(keyword):
 result = soup.find_all(string = re.compile(keyword , re.IGNORECASE))
 return result

while True :
    keyword = input("enter the keyword you wanna search or type exit to exit !")

    if keyword.lower() == 'exit':
        print("exiting the script....")
        print("byeeeee !!!1")
        break
    matches = finding(keyword)
    print(f"Matches found are {len(matches)}")

    for match in matches:
       clean_text = " ".join(match.split())
       if clean_text:
         print(clean_text)
