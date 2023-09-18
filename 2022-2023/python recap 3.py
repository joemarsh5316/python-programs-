import pandas as pd
df = pd.read_csv('gamerscore.csv', header =None)
df.columns = ['UserName', 'HighScore']
df.sorted('Score', ascending=False, inplace=True)
