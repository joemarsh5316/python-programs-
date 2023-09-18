import pandas as pd
my_converter = {'gamerscore.csv': str}
df = pd.read_csv('gamerscore.csv', header=0, sep="\t",  escapechar='\\', converters=my_converter)
df.columns = ['UserName', 'HighScore']
gamerscore.sort_values('Score', ascending=False, inplace=True)
print(df.to_string())
