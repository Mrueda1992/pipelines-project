import pandas as pd
import json
import requests

def pointers(df, points):
    df = df.groupby('Player')[points].sum().sort_values(ascending=False)
    return df

def shooters (df, shoots):
    df = df.groupby('Player')[shoots].sum().sort_values(ascending=False)
    return df

def accurates(df, pointers, shooters):
    df = round(pointers/shooters,3)
    return df

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