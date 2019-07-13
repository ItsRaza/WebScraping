import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get("https://www.whatmobile.com.pk/50000_to_350001_Mobiles")
soup = BeautifulSoup(r.text, "html.parser")
results = soup.find_all('a', attrs={'class': 'BiggerText'})
results2 = soup.find_all('span', attrs={'class': 'PriceFont'})
first = results[0]
first2 = results2[0]
record = []

for i, each in enumerate(results):
    Name = each.text[4:]
    for j, each in enumerate(results2):
        if j == i:
            Price = each.text[2:-1]
            break
    record.append((Name, Price))

print(record)

df = pd.DataFrame(record, columns=['Name', 'Price'])
df.to_csv('Mobiles.csv', index=False, encoding='utf-8')
