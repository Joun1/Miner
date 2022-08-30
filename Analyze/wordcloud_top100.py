import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import re
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
from wordcloud import STOPWORDS

path = r'E:\koodit\Git\Master data_työversio_din_iso_modified.csv'
data = pd.read_csv(path)

data_old = data['Item description (local 1)']
data_new = data['Tekstinsyotto']
text = " ".join(review for review in data_new.astype(str))

text = text.split()
for i in text:
        i = i.strip()
        if len(i) == 0:
                text.pop(text.index(i))
text.pop(0)
text_len = len(text)
data['words'] = ''

for i in range(text_len):
#        if i == 50:
#                break
        data['words'][i] = text[i]
df1 = pd.DataFrame(data['words'])

df1['count'] = 1
df1 = df1.groupby(['words']).count()['count']
df1 = df1.reset_index()

new_data = df1.set_index('words').to_dict()['count']

stopwords = set(STOPWORDS)
stopwords.update(["''"])
wc = WordCloud(width=800, height=600, max_words=100).generate_from_frequencies(new_data)
#print(text)
#print ("There are {} words in the combination of all cells in column YOUR_COLUMN_NAME.".format(len(text)))
#wordcloud = WordCloud(stopwords=stopwords,max_words=2000,background_color="black", width=800, height=400).generate_from_frequencies(text)
plt.axis("off")
plt.figure(figsize=(20,10))
plt.tight_layout(pad=0)
plt.imshow(wc, interpolation='bilinear')
plt.show()