import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import re
import seaborn as sns

#path = r'E:\koodit\Git\Master data_työversio_din_iso_modified.csv'
path = r"E:\koodit\Git\Master data_työversio_din_iso.xlsx"
col_list = ["Item No.", "Item description (local 1)","Specification (local 2)","Part Description","Item Group",
            "Part Description Spec","MrtlSubGroup","Cert Purchase Doc Description","Item type 1"]
df = pd.read_excel(path, usecols=col_list)
#df.drop(['Lisainfo','Syotetyt','Unnamed: 0','Tekstinsyotto','Luetut', 'Orig standard'], axis=1, inplace=True)
#print(df.columns)
indexi = df.index
rivit = len(indexi) #tiedoston rivimäärä
print("rivien maara=",rivit)
data = []

for i in df.columns:
    temp =[i,df[i].isnull().sum()]
    data.append(temp)

data = pd.DataFrame(data)

ex = data.plot(kind='bar',x=data.columns[0],legend=False)
for p in ex.patches:
    ex.annotate(text=np.round(p.get_height(), decimals=2),
                xy=(p.get_x()+p.get_width()/2., p.get_height()),
                ha='center',
                va='center',
                xytext=(0, 11),
                textcoords='offset points')

totaali = data[1].sum()
totaali = str(totaali)

#plt.xticks(rotation = 50)
plt.title("Total "+totaali+" blank fields")
plt.tight_layout()
plt.show()
