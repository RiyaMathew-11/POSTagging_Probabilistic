import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nlp_toolkit import word_tokens
from nltk.probability import FreqDist

# Removing stopwords
filtered_tokenized = []
stop_words = set(stopwords.words("english"))
for word in word_tokens:
    if word not in stop_words and len(word) > 1:
        filtered_tokenized.append(word)

# Finding the frequency of the most common words using the FreqDist class
freq_distr = FreqDist(filtered_tokenized)
print(freq_distr.most_common(10))

# Segregating items
dict = {}
dict_frequency = {}
for element in freq_distr.most_common(10):
    tup = list(element)
    dict = {tup[0]: tup[1]}
    dict_frequency.update(dict)

words = list(dict_frequency.keys())
frequency = list(dict_frequency.values())

# Plotting a line graph
plt.bar(words, frequency, align='center', width=0.6)
plt.show()
