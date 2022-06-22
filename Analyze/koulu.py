import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression

#path = r'C:\Users\Jouni Kinnunen\Documents\Python Scripts\Master data_työversio 1_modified.csv'
path = r'C:\Users\Jouni Kinnunen\Documents\Python Scripts\Master data_työversio_din_iso_modified_modified.csv'
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
#ax3 = fig.add_subplot(221)

data.plot(color=['red','green'],y=['Syotetyt','Syotetyt mean'],grid=True,ax=ax1)

data.plot(color=['blue','green'],y=['Luetut','Luetut mean'],grid=True,ax=ax2)



lista ={'col_1':['mean','std','min','max'],
        'Syotetyt':[data['Syotetyt'].mean(),data['Syotetyt'].std(),data['Syotetyt'].min(),data['Syotetyt'].max()],
        'Luetut':[data['Luetut'].mean(),data['Luetut'].std(),data['Luetut'].min(),data['Luetut'].max()]}

df = pd.DataFrame.from_dict(lista)
ex = df.plot(kind='bar',x='col_1',color=['red','blue'])
for p in ex.patches:
    ex.annotate(s=np.round(p.get_height(), decimals=2),
                xy=(p.get_x()+p.get_width()/2., p.get_height()),
                ha='center',
                va='center',
                xytext=(0, 10),
                textcoords='offset points')

plt.xticks(rotation = 45)
plt.figure()
#data.plot(kind='scatter',x='Luetut',y='Syotetyt',grid=True)



X = data[["Luetut"]]
y = data[["Syotetyt"]]

regressor = LinearRegression()
regressor.fit(X, y)

y_pred = regressor.predict(X)

plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'green')
plt.title('Luetut vs Syotetyt')
plt.xlabel('Luetut')
plt.ylabel('Syotetyt')

print("Luetut",data['Luetut'].describe())
print("Syotetyt",data['Syotetyt'].describe())
plt.figure()

data['Std match'] = ''
for i in range(len(data)):
        x = data['Tekstinsyotto'][i]
        if x[0:3] == data['Orig standard'][i]:
                data['Std match'][i] = 'ok'
        else:
                data['Std match'][i] = 'mismatch'

#x = data['Std match'].value_counts().['ok']
#y = data['Std match'].value_counts().['mismatch']
x = data['Std match'].value_counts()
x.plot(kind='bar',color=['green','red'])
plt.xticks(rotation = 0)
plt.title('Onko luodun rivin standardi sama kuin Item description')
plt.xlabel('mismatch = Ei täsmää')


plt.show()
