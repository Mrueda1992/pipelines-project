import pandas as pd 
import json
import requests

#Load data
def load_data(data):
    df = pd.read_csv(data, encoding="ISO-8859-1")
    return df

#Clean data
def drop_nulls(df):
    #df = df[df[cols].notnull()]
    df = df.fillna("0")
    return df

def rename (df, col, new_col):
    df.rename (columns= {col: new_col}, inplace=True)
    return df

#Analyse data

def pointers(df, points):
    df = df.groupby('Player')[points].sum().sort_values(ascending=False)
    return df

def shooters (df, shoots):
    df = df.groupby('Player')[shoots].sum().sort_values(ascending=False)
    return df

def accurates(df, pointers, shooters):
    df = round(pointers/shooters,3)
    return df

#Call API

def getAPI():
    url = "https://www.balldontlie.io/api/v1/stats?seasons[]=2018&seasons[]=2019&player_ids[]=115"
    res = requests.get(url)
    text = res.json()
    return text

def curry_stats():
    data = text['data'][0].keys()
    dic_aux=[]
    for e in data['data']:
        dic = {
            'Minutes per game':e['min'], 'Three_Effectivity':e['fg3_pct'],
            'Three_Attempts':e['fg3a'], 'Three_In': e['fg3m'],
            'Points':e['pts']
            }
        dic_aux.append(dic)
    df = pd.DataFrame(dic_aux)
    df = df[['Minutes per game','Three_In','Three_Attempts','Three_Effectivity','Points']]
    return df

#main_file

def lectura(da):
    read= load_data(da)
    return read

my_data= lectura("nba-stats.csv")
my_data = my_data[['Year','Player','Pos','Tm','3PAr','3P','3PA','3P%']]

def clean(my_data):
    my_data = drop_nulls (my_data, '3P')
    my_data = rename (my_data, 'Pos', 'Position')
    my_data = rename (my_data, 'Tm', 'Team')
    return my_data

def analyze (my_data):
    my_data = pointers(my_data, '3P')
    my_data = shooters (my_data, '3PA')



if __name__== "__main__":
    main()








