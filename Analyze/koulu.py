import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import re
import seaborn as sns

#path = r'C:\Users\Jouni Kinnunen\Documents\Python Scripts\Master data_työversio 1_modified.csv'
path = r'E:\koodit\Git\Master data_työversio_din_iso_modified.csv'
#col_list = ['Output','Input']
data = pd.read_csv(path)
data['Output mean'] = [data['Output'].mean() for i in range(len(data))]
data['Output std'] = [data['Output'].std() for i in range(len(data))]
data['Input mean'] = [data['Input'].mean() for i in range(len(data))]
data['Input std'] = [data['Input'].std() for i in range(len(data))]

ax = plt.gca()
ax_plt = plt.gca()
fig = plt.figure()

data.plot(kind='line',color='blue',y='Input',grid=True,linewidth=1,ax=ax)
data.plot(kind='line',color='red',y='Output',grid=True,linewidth=1,ax=ax)

ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
#ax3 = fig.add_subplot(213)
#ax4 = fig.add_subplot(214)

data.plot(color=['red','green'],y=['Output','Output mean'],grid=True,ax=ax1)

data.plot(color=['blue','green'],y=['Input','Input mean'],grid=True,ax=ax2)



lista ={'col_1':['mean','std','min','10%','50%','90%','max'],
        'Output':[data['Output'].mean(),data['Output'].std(),data['Output'].min(),data['Output'].quantile(0.10),data['Output'].quantile(0.50),data['Output'].quantile(0.90),data['Output'].max()],
        'Input':[data['Input'].mean(),data['Input'].std(),data['Input'].min(),data['Input'].quantile(0.10),data['Input'].quantile(0.50),data['Input'].quantile(0.90),data['Input'].max()]}

df = pd.DataFrame.from_dict(lista)
ex = df.plot(kind='bar',x='col_1',color=['red','blue'])
for p in ex.patches:
    ex.annotate(text=np.round(p.get_height(), decimals=2),
                xy=(p.get_x()+p.get_width()/2., p.get_height()),
                ha='center',
                va='center',
                xytext=(0, 10),
                textcoords='offset points')

plt.xticks(rotation = 45)
plt.figure()
#data.plot(kind='scatter',x='Input',y='Output',grid=True)



x = data[['Input']].values
y = data[['Output']].values

regressor = LinearRegression()
regressor.fit(x, y)

y_pred = regressor.predict(x)
col =['red','green']
sns.scatterplot(data['Input'],data['Output'],color='r')
sns.kdeplot(data['Input'],data['Output'],c='b',levels=3)
plt.plot(x, y_pred,c='green')

plt.title('Input vs Output')
plt.xlabel('Input')
plt.ylabel('Output')

#print('Input',data['Input'].describe())
#print('Output',data['Output'].describe())
plt.figure()
plt.subplot(2, 1, 1)

data = pd.read_csv(path)
data['Std match'] = ''
for i in range(len(data)):
        x = data['Tekstinsyotto'][i]
        x = re.search(x[0:3],data['Orig standard'][i])
        if bool(x):
                if x[0] == 'ANS':
                        data['Std match'][i] = 'ANSI'
                else:
                        data['Std match'][i] = 'ok'
        else:
                data['Std match'][i] = 'mismatch'
data.to_csv(r'E:\koodit\Git\data.csv')
x = data['Std match'].value_counts()
ex = x.plot(kind='bar',color=['green','red','grey'])
for p in ex.patches:
        ex.annotate(text=np.round(p.get_height(), decimals=2),
                xy=(p.get_x()+p.get_width()/2., p.get_height()),
                ha='center',
                va='center',
                xytext=(0, 11),
                textcoords='offset points')

ex.tick_params(axis="x",rotation = 0)

ex.set_title('Is the standard same as Item Description',y=1.05)

plt.subplot(2, 1, 2)

x = data.loc[(data['Std match'] == 'mismatch') & (data['Orig standard'])]
x = x['Orig standard'].value_counts()
ex = x.plot(kind='bar')

for p in ex.patches:
    ex.annotate(text=np.round(p.get_height(), decimals=2),
                xy=(p.get_x()+p.get_width()/2., p.get_height()),
                ha='center',
                va='center',
                xytext=(0, 11),
                textcoords='offset points')

ex.set_title('Closer look of mismatches',y=1.05)
ex.tick_params(axis="x",rotation = 0)

#fig.subplots_adjust(top=0.9, wspace=0.3, hspace=0.3)
plt.tight_layout()
plt.show()