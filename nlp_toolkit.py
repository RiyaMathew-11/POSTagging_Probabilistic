from nltk.corpus import gutenberg
from nltk.tokenize import word_tokenize, sent_tokenize, RegexpTokenizer, BlanklineTokenizer
my_corpus = gutenberg.raw('bible-kjv.txt')

# Tokenization
# Sentence tokenization
tokenize_text = sent_tokenize(my_corpus)
for element in tokenize_text[0:10]:
    print(element)

# Word Tokenisation
word_tokens = []
for sentence in tokenize_text[0:10]:
    tokenize_words = word_tokenize(sentence)
    for word in tokenize_words:
            word_tokens.append(word)

    # for element in tokenize_words:
    #     print(element[0:], end='   ')
    # print('\n')

print(word_tokens)
# Regular Expression Tokenizer

caps_tokenizer = RegexpTokenizer('[A-Z]\w+')

tokenize_regex = caps_tokenizer.tokenize(my_corpus)

# for token in tokenize_regex:
#     print(token, end='\t')

# Blankline Tokenizer

sample = '''Hi, I am Riya and I am gonna write some code.
Coding is my favourite activity to do.
I love coding in python.
Python is a scripting language


Natural Language Toolkit

NLTK is a powerful Python package that contains several algorithms to help computers
preprocess, analyse, and understand natural languages and written texts

 - Tokenization
 - POS Tagging
 - Named Entity Recognition

Corpora

A corpus is a huge collection of written texts. A compilation of corpus is called a Corpora
It is a body of written or spoken texts used in linguistic analysis and development of
NLP tools.'''

tokens_Blankline = BlanklineTokenizer().tokenize(sample)
# for ele in tokens_Blankline:
#     print(ele, end='\n\n\n\n\n\n')