# https://pythonspot.com/nltk-stop-words/
import nltk
nltk.download('punkt')
nltk.download('stopwords')

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

# test 1
data = "All work and no play makes jack dull boy. All work and no play makes jack a dull boy."
words = word_tokenize(data)
print(words)

# test 2
data = "All work and no play makes jack dull boy. All work and no play makes jack a dull boy."
stopWords = set(stopwords.words('english'))
words = word_tokenize(data)
wordsFiltered = []

for w in words:
    if w not in stopWords:
        wordsFiltered.append(w)

print(wordsFiltered)

# test 3
data = "Стэмминг — процесс приведения слова к основе (отрезание окончания и формообразующего суффикса), грубо, но быстро."
stopWords = set(stopwords.words('russian'))
words = word_tokenize(data)
wordsFiltered = []

for w in words:
    if w not in stopWords:
        wordsFiltered.append(w)

print(wordsFiltered)