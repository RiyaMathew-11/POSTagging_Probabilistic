import matplotlib.pyplot as plt
from nltk.probability import FreqDist
# Concept of Bigrams, Trigrams and N-grams

# Bi-grams are two consecutive occurring in a corpus
# Creating bigrams using 'webtext corpus'

from nltk.corpus import webtext, stopwords, gutenberg
from nltk import bigrams,trigrams, ngrams

print('\nBigrams')
words_in_text = [w.lower() for w in webtext.words('pirates.txt')]

# Removing stopwords
stop_words = set(stopwords.words('english'))
filter_words = [w for w in words_in_text if w not in stop_words and len(w)>3]

#Generating Bi-grams
bi_grams = bigrams(filter_words)
freq_dist = FreqDist(bi_grams)
print(freq_dist.most_common(10))


# Trigrams are 3 consecutive words that occur in a corpus

print('\nTrigrams')
words2_in_text = [w.lower() for w in webtext.words('grail.txt')]

# Removing stopwords
filter_words2 = [w for w in words2_in_text if w not in stop_words and len(w)>3]

# Generating Trigrams
tri_grams = trigrams(filter_words2)
freq_dist = FreqDist(tri_grams)
print(freq_dist.most_common(10))

# N-grams are N-continuous words in corpus

print('\nN-grams')
words3_in_text = [w.lower() for w in gutenberg.words('shakespeare-hamlet.txt')]
filter_words3 = [w for w in words3_in_text if w not in stop_words and len(w)>3]

n_grams = ngrams(filter_words3,4)
freq_dist = FreqDist(n_grams)
print(freq_dist.most_common(10))
