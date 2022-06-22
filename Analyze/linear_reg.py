import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression

#path = r'C:\Users\Jouni Kinnunen\Documents\Python Scripts\Master data_työversio 1_modified.csv'
path = r'C:\Users\Jouni Kinnunen\Documents\Python Scripts\Master data_työversio_din_iso_modified_modified.csv'

data = pd.read_csv(path)
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

data['Std match'] = ''
for i in range(len(data)):
        x = data['Tekstinsyotto'][i]
        if x[0:3] == data['Orig standard'][i]:
                data['Std match'][i] = 'ok'
        else:
                data['Std match'][i] = 'mismatch'

x = data['Std match'].value_counts()
ex = x.plot(kind='bar',color=['green','red'], ax=ax1)
for p in ex.patches:
    ex.annotate(s=np.round(p.get_height(), decimals=2),
                xy=(p.get_x()+p.get_width()/2., p.get_height()),
                ha='center',
                va='center',
                xytext=(0, 11),
                textcoords='offset points')

ax1.tick_params(axis="x",rotation = 0)

ax1.set_title('Onko luodun rivin standardi sama kuin Item description',y=1.05)

x = data.loc[(data['Std match'] == 'mismatch') & (data['Orig standard'])]
x = x['Orig standard'].value_counts()
ex = x.plot(kind='bar',ax=ax2)

for p in ex.patches:
    ex.annotate(s=np.round(p.get_height(), decimals=2),
                xy=(p.get_x()+p.get_width()/2., p.get_height()),
                ha='center',
                va='center',
                xytext=(0, 11),
                textcoords='offset points')

ax2.set_title('Arvo joka on item description mutta ei generoidussa nimessä',y=1.05)
ax2.tick_params(axis="x",rotation = 0)

fig.subplots_adjust(top=0.9, wspace=0.3, hspace=0.3)
plt.show()