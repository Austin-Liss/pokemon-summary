import pandas as pd

df = pd.read_csv("C:/Users/77192/.vscode/Python/Git-Study/Pokemon.csv")
df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('.', '', regex=False)

# Counting Legendaries
print(df['legendary'].value_counts()) # Only 65 legendaries out of 800 Pokemons

# Comparing Legendary vs Non-Legendary
stats = (df.groupby('legendary')['total']
         .agg(n='count',mean='mean',median='median',deviation='std')
         .round(1)
         .rename(index={False:'Regular', True:'Legendary'})
         .rename_axis('group'))
print(stats.shape)

# compare all six stats.
STATS = ['hp', 'attack', 'defense', 'sp_atk', 'sp_def', 'speed']
mean = df.groupby('legendary')[STATS].mean().round(1)
gap = mean.loc[True] - mean.loc[False]
percentage =( (mean.loc[True] / mean.loc[False] -1) * 100).round(1)
table = (pd.DataFrame({
        'regular' : mean.loc[False],
        'Legendary' : mean.loc[True],
        'Gap' : gap,
        "Percentage" : percentage
}))
print(table)