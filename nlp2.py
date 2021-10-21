from nltk.corpus import stopwords
from textblob import TextBlob
import nltk
from pathlib import Path
import pandas as pd

#nltk.download("stopwords")

stops = stopwords.words("english")

#print(stops)

blob = TextBlob("Today is a beautiful day.")

print(blob.words)

cleanlist = [word for word in blob.words if word not in stops]

print(cleanlist)

blob = TextBlob(Path("RomeoandJuliet.txt").read_text())

print(blob.words.count("joy"))

print(blob.word_counts["juliet"])

#print(blob.noun_phrases.count("lady capulet"))

print(blob.words.count("thou"))

more_stops = ["thee","thou","thy"]

stops += more_stops

items = blob.word_counts.items()

#print(items)

clean_items = [i for i in items if i[0] not in stops]

print(clean_items[:10])

from operator import itemgetter

sorted_list = sorted(clean_items, key=itemgetter(1), reverse=True)

print(sorted_list[:10])

top20 = sorted_list[:20]

df = pd.DataFrame(top20, columns=["word","count"])

print(df)

import matplotlib.pyplot as plt

df.plot.bar(x="word",y="count",legend=False, color=["y", "c", "m", "b", "g", "r"])

plt.gcf().tight_layout()

plt.show()
