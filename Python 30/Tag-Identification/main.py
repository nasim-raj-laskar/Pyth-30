import urllib.request
from bs4 import BeautifulSoup
import nltk
import matplotlib.pyplot as plt

nltk.download('stopwords')
from nltk.corpus import stopwords

response = urllib.request.urlopen('https://en.wikipedia.org/wiki/Apple')
html = response.read()

soup = BeautifulSoup(html, 'html5lib')
text = soup.get_text(strip=True)

tokens = text.split()
stop_words = set(stopwords.words('english'))

clean_tokens = [token for token in tokens if token.isalnum() and token.lower() not in stop_words]

freq = nltk.FreqDist(clean_tokens)

top_words = freq.most_common(20)

print("Top 20 most frequent words:")
for word, count in top_words:
    print(f"{word}: {count}")

words, counts = zip(*top_words)
plt.figure(figsize=(10, 6))
plt.bar(words, counts, color='skyblue')
plt.xlabel('Words', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title('Top 20 Most Frequent Words', fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
