import pandas as pd

#Reading a .csv from a URL


df_prem21 = pd.read_csv('https://www.football-data.co.uk/mmz4281/2122/E0.csv') #reading a csv off an internet link
#rename the columns of the data frame
df_prem21.rename(columns={'FTHG': 'Home_Goals', 'FTAG': 'Away_Goals'}, inplace=True)
print(df_prem21)

