import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import re
import seaborn as sns

#path = r'C:\Users\Jouni Kinnunen\Documents\Python Scripts\Master data_työversio 1_modified.csv'
path = r'E:\koodit\Git\Master data_työversio_din_iso_modified.csv'
#col_list = ["Syotetyt","Luetut"]
data = pd.read_csv(path)
data['Syotetyt mean'] = [data['Syotetyt'].mean() for i in range(len(data))]
data['Syotetyt std'] = [data['Syotetyt'].std() for i in range(len(data))]
data['Luetut mean'] = [data['Luetut'].mean() for i in range(len(data))]
data['Luetut std'] = [data['Luetut'].std() for i in range(len(data))]

ax = plt.gca()
ax_plt = plt.gca()
fig = plt.figure()

data.plot(kind='line',color='blue',y='Luetut',grid=True,linewidth=1,ax=ax)
data.plot(kind='line',color='red',y='Syotetyt',grid=True,linewidth=1,ax=ax)

ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
#ax3 = fig.add_subplot(213)
#ax4 = fig.add_subplot(214)

data.plot(color=['red','green'],y=['Syotetyt','Syotetyt mean'],grid=True,ax=ax1)

data.plot(color=['blue','green'],y=['Luetut','Luetut mean'],grid=True,ax=ax2)



lista ={'col_1':['mean','std','min','10%','50%','90%','max'],
        'Syotetyt':[data['Syotetyt'].mean(),data['Syotetyt'].std(),data['Syotetyt'].min(),data['Syotetyt'].quantile(0.10),data['Syotetyt'].quantile(0.50),data['Syotetyt'].quantile(0.90),data['Syotetyt'].max()],
        'Luetut':[data['Luetut'].mean(),data['Luetut'].std(),data['Luetut'].min(),data['Luetut'].quantile(0.10),data['Luetut'].quantile(0.50),data['Luetut'].quantile(0.90),data['Luetut'].max()]}

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
#data.plot(kind='scatter',x='Luetut',y='Syotetyt',grid=True)



x = data[["Luetut"]].values
y = data[["Syotetyt"]].values

regressor = LinearRegression()
regressor.fit(x, y)

y_pred = regressor.predict(x)
col =['red','green']
sns.scatterplot(data["Luetut"],data["Syotetyt"],color='r')
sns.kdeplot(data["Luetut"],data["Syotetyt"],c='b',levels=3)
plt.plot(x, y_pred,c='green')

plt.title('Luetut vs Syotetyt')
plt.xlabel('Luetut')
plt.ylabel('Syotetyt')

print("Luetut",data['Luetut'].describe())
print("Syotetyt",data['Syotetyt'].describe())
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
#data.to_csv(r'E:\koodit\Git\data.csv')
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

ex.set_title('Onko luodun rivin standardi sama kuin Item description',y=1.05)

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

ex.set_title('Mismatchien erottelu',y=1.05)
ex.tick_params(axis="x",rotation = 0)

#fig.subplots_adjust(top=0.9, wspace=0.3, hspace=0.3)
plt.tight_layout()
plt.show()