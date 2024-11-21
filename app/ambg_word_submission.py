import pandas as pd  

df = pd.read_csv('./ambg_words.csv')
df[['word', 'eraab']].to_csv('./ambg_words_final.csv', index=None, header=False)