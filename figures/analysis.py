import pandas as pd

df = pd.read_csv("C:/Users/77192/.vscode/Python/Git-Study/Pokemon.csv")
df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('.', '', regex=False)

print(df.shape)
print(df.columns.tolist())