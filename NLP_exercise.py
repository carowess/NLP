'''Use this text file  - book of John text.txt to create a wordcloud of the top 15 words that are the most recurring. 
Make sure to remove all stop words. Use only noun words for this analysis. 
To get a good idea of what the book of John is about, it would be better to eliminate additional 
stop words that are found in the context of the Bible. Please eliminate these additional words from your WordCloud:

thy, ye, verily, thee, hath, say, thou, art, shall '''

from nltk.corpus import stopwords
import nltk
from pathlib import Path
from wordcloud import WordCloud
from textblob import TextBlob

blob = TextBlob(Path('book of John text.txt').read_text())

#nltk.download("stopwords")
stops = stopwords.words("english")
more_stops = ['thy', 'ye', 'verily', 'thee', 'hath', 'say', 'thou', 'art', 'shall']
stops += more_stops

noun_phrases = blob.noun_phrases

items = blob.word_counts.items()
clean_items = [word for word in items if word[0] not in stops if word[0] in noun_phrases]

from operator import itemgetter
sorted_list = sorted(clean_items, key=itemgetter(1), reverse=True)

top15 = sorted_list[:15]
print(top15)


for i in top15:
    top15_wordcloud = [x[0] for x in top15]

print(top15_wordcloud)

string_for_wordcloud = " ".join(top15_wordcloud)
print(string_for_wordcloud)

wordcloud = WordCloud(colormap='Blues',background_color='gray')
wordcloud = wordcloud.generate(string_for_wordcloud)
wordcloud = wordcloud.to_file("BookOfJohnWordCloud.png")

