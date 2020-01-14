import pandas as pd
import yaml

dict_file=[]
df = pd.read_excel("Book1.xlsx")

for i in range(df.shape[1]):
    name = df.columns.values[i]
    dict_file.append((df[name]).tolist())

# print(dict_file)
x = df.columns.values
x = dict(zip(x, dict_file))

# print(x)
with open(r'ip.yaml', 'w') as file:
    documents = yaml.dump(x, file)
