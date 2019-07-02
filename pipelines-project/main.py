import pandas as pd
import acquisition
import cleaning
import analysis


def lectura(data):
    read = acquisition.load_data(data)
    return read


my_data = lectura("nba-stats.csv")
my_data = my_data[['Year', 'Player', 'Pos', 'Tm', '3PAr', '3P', '3PA', '3P%']]

def clean(my_data):
    #my_data = cleaning.drop_nulls (my_data, '3P')
    my_data = cleaning.rename(my_data, 'Pos', 'Position')
    my_data = cleaning.rename(my_data, 'Tm', 'Team')
    return my_data

print (my_data)

def analyze (my_data):
    my_data = analysis.pointers(my_data, '3P')
    my_data = analysis.shooters (my_data, '3PA')

def main():
    my_data = acquisition()
    my_data = cleaning(my_data)
    my_data = analysis(my_data)


if __name__== "__main__":
    main()

