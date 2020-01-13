import pandas as pd
import yaml

dict_file=[]
df = pd.read_excel("Book1.xlsx")
for i in range(df.shape[0]):
    dict_file.append((df.loc[i].values).tolist())
x = df.columns.values
x = dict(zip(x, dict_file))
with open(r'ip.yaml', 'w') as file:
    documents = yaml.dump(x, file)