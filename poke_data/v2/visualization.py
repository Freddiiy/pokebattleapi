import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path


def specific_pokemon(name: str, color: str = None):

    hp = df[df['Name'] == name]['HP']
    attack = df[df['Name'] == name]['Attack']
    defense = df[df['Name'] == name]['Defense']
    sp_attack = df[df['Name'] == name]['Sp_Attack']
    sp_defense = df[df['Name'] == name]['Sp_Defense']
    speed = df[df['Name'] == name]['Speed']

    sum_stats = df[df['Name'] == name]['Sum_stats'].values[0]

    x = ['HP','Attack','Defense','Sp. Attack','Sp. Defense','Speed']
    y = [hp, attack, defense, sp_attack, sp_defense, speed]

    #fig, ax = plt.subplots()
    #ax.plot(x,y)
    plt.plot(x,y,label=f'{name}, {sum_stats}', color=color)


def average_stats():

    avg_hp = hp.mean()
    avg_attack = attack.mean()
    avg_defense = defense.mean()
    avg_sp_attack = sp_attack.mean()
    avg_sp_defense = sp_defense.mean()
    avg_speed = speed.mean()


    avg_pokemon_stats_fig = plt.figure(2)	#identifies the figure
    plt.title("Stat size for given Pokemon v2", fontsize='16')	#title
    x = ['HP','Attack','Defense','Sp. Attack','Sp. Defense','Speed']
    y = [avg_hp, avg_attack, avg_defense, avg_sp_attack, avg_sp_defense, avg_speed]
    plt.plot(x,y,linestyle='dashed', color='black')	#plot the points
    specific_pokemon('chansey', color='magenta')
    specific_pokemon('charizard', color='red')
    specific_pokemon('mewtwo', color='purple')
    specific_pokemon('cloyster', color='cyan')
    specific_pokemon('pidgey', color='brown')
    plt.xlabel("Type of Stat",fontsize='13')	#adds a label in the x axis
    plt.ylabel("Size of Stat",fontsize='13')	#adds a label in the y axis
    plt.ylim(-10,260)
    plt.legend()
    plt.savefig('plots/specific_pokemon_stats.png')	#saves the figure in the present directory
    plt.grid()	#shows a grid under the plot
    plt.show()


if __name__ == '__main__':

    df = pd.read_csv('./poke_data/data/pokemon.csv')
    df_matches = pd.read_csv('./poke_data/data/v2/match.csv')

    hp = pd.Series(df['HP'])
    attack = pd.Series(df['Attack'])
    defense = pd.Series(df['Defense'])
    sp_attack = pd.Series(df['Sp_Attack'])
    sp_defense = pd.Series(df['Sp_Defense'])
    speed = pd.Series(df['Speed'])

    pokemon_stats_fig = plt.figure(1)	#identifies the figure
    plt.title("Stat size per Pokemon", fontsize='16')	#title
    plt.plot(['HP','Attack','Defense','Sp. Attack','Sp. Defense','Speed'],[hp, attack, defense, sp_attack, sp_defense, speed])	#plot the points
    plt.xlabel("Type of Stat",fontsize='13')	#adds a label in the x axis
    plt.ylabel("Size of Stat",fontsize='13')	#adds a label in the y axis
    plt.ylim(-10,260)
    plt.savefig('plots/pokemon_stats.png')	#saves the figure in the present directory
    plt.grid()	#shows a grid under the plot
    plt.show()
    average_stats()

    counts = df_matches['Winner'].value_counts().sort_index()
    pokemons = pd.concat([df_matches['Poke_1'],df_matches['Poke_2']]).unique()
    plt.bar(pokemons,counts,width=0.4)
    plt.title('Win Counts for each Pokemon v2', fontsize='16')
    plt.xlabel("Pokemon ID",fontsize='13')
    plt.ylabel("Win count",fontsize='13')
    plt.ylim(0,310)
    plt.savefig('plots/win_counts.png')	#saves the figure in the present directory
