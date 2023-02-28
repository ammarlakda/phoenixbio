import pandas as pd
df = pd.read_csv('/Users/ammarlakdawala/Documents/phoenixbio/Phoenix Bioinformatics/IF Code/FinalDatasets/phyb_100.csv')
df=df['abstract']
print(df[1].type())