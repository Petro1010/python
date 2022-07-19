# we can use the pandas library to extract tables from web pages
import pandas as pd

simpsonsEpis = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)') #returns a list with multiple tables

print(len(simpsonsEpis))

print(simpsonsEpis[1])

#then covert it to json or something
simpsonsEpis[1].to_json()