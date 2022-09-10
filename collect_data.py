from bs4 import BeautifulSoup
import pandas as pd

with open('html.txt', 'r') as file:
    html = file.read().replace('\n', '')

soup = BeautifulSoup(html, 'html.parser')

result=[]
tactic =[]

tactic_ele = soup.select('#yw1 > table > tbody > tr > td:nth-child(10)')
result_ele = soup.select('#yw1 > table > tbody > tr > td.zentriert.hauptlink')

for i in range(len(result_ele)):
    result.append(result_ele[i].text)
    tactic.append(tactic_ele[i].text)

information = {
    'result':result,
    'tactic':tactic,
}
df = pd.DataFrame(information)
df.to_excel('data.xlsx',index=False)